import math

# ===== 기구 파라미터 (mm) =====
l1_left  = 49.75   # 왼쪽 proximal link 길이
l1_right = 49.75   # 오른쪽 proximal link 길이, |P_R - O|
l2_left  = 35.0   # 왼쪽 distal link 길이
l2_right = 35.0   # 오른쪽 distal link 길이, |E - P_R|
T_to_P_R = 127.37 # 오른쪽 Proximal link(P_R)에서 fingerTip(T)까지의 거리, |T - P_R|
T_to_E = 96.32    # diamond linkage Edge(E)에서 fingerTip(T)까지의 거리, |T - E|
OFFSET_CW_DEG = 23.58 # 오른쪽 distal link의 방향벡터(E - P_R/|E - P_R|)에서 CW로 23.58 [deg] 만큼 회전해야 방향벡터 (T - P_R)/|T - P_R|

# ===== 각도 제약 (θ(사용자각 = 모터각, deg)) =====
# 사용자각(=모터각): 수직↓=0°, θ1(왼쪽 기울수록 +), θ2(오른쪽 기울수록 +)
theta1_min_deg = -161.2
theta1_max_deg =   76.0
theta2_min_deg = -144.4
theta2_max_deg =   93.4

# 두 모터 각도 합 제약 (deg): SUM_MIN < θ1+θ2 < SUM_MAX
sum_min_deg = -70.0
sum_max_deg =  -7.0

# 허용오차(deg)
eps_ang = 1e-6 # unit : degree
eps_len = 1e-9 # unit : mm

# ===== 유틸 =====
def _clamp(x, lo=-1.0, hi=1.0): return max(lo, min(hi, x))
def _wrap_pi(a): return (a + math.pi) % (2*math.pi) - math.pi   # [-π, π)
def _deg(r): return r * 180.0 / math.pi
def _wrap_deg(a): return (a + 180.0) % 360.0 - 180.0            # [-180, 180)
def _deg360(r): return (_deg(r)) % 360.0                        # [0, 360)

# 사용자 좌표(xu = [-1, 0, 0], yu = [0, -1, 0]) ↔ 수학 직교좌표계(xm = [1, 0, 0], ym = [0, 1, 0]) (ㅈ : 그냥 180도 도는 rotation matrix라고 생각하면 됨)
def _user_to_math(xu, yu): return -xu, -yu

# 각 측의 반경(필요조건)
def _r_range_left():  return abs(l1_left  - l2_left),  (l1_left  + l2_left)
def _r_range_right(): return abs(l1_right - l2_right), (l1_right + l2_right)

# IK 후보(직교좌표계)
def _ik_candidates_math(xm, ym, eps=eps_len):
    r = math.hypot(xm, ym)
    if r < eps: return []
    rL_min, rL_max = _r_range_left()
    rR_min, rR_max = _r_range_right()
    if not (rL_min <= r <= rL_max and rR_min <= r <= rR_max):
        return []
    cL = _clamp((l1_left*l1_left  + r*r - l2_left*l2_left ) / (2.0*l1_left*r),  -1.0, 1.0)
    cR = _clamp((l1_right*l1_right + r*r - l2_right*l2_right) / (2.0*l1_right*r), -1.0, 1.0)
    alphaL = math.acos(cL); alphaR = math.acos(cR)
    tm = math.atan2(ym, xm)
    # 두 분기 (phi1=왼쪽, phi2=오)
    return [(tm + alphaL, tm - alphaR), (tm - alphaL, tm + alphaR)]

# φ(수학각, rad) → θ(사용자/모터각, deg)
def _phi_to_user_deg(phi1, phi2):
    theta1_base = -_wrap_pi(phi1 + math.pi/2.0)
    theta2_base =  _wrap_pi(phi2 + math.pi/2.0)
    theta1 = _wrap_deg(_deg(theta1_base) - 45.0) # -45[deg] 보정 이유 : 모터에 -45 [deg]로 proximal link가 장착되어 있음
    theta2 = _wrap_deg(_deg(theta2_base) - 45.0)
    return theta1, theta2

# θ(사용자, deg) → φ(수학, rad)
def _user_deg_to_phi(theta1_deg, theta2_deg):
    tb1 = math.radians(_wrap_deg(theta1_deg + 45.0))
    tb2 = math.radians(_wrap_deg(theta2_deg + 45.0))
    phi1 = -tb1 - math.pi/2.0
    phi2 =  tb2 - math.pi/2.0
    return phi1, phi2

# 두 원의 교점 구하기(cosine 법칙 이용)
def _circle_circle_intersections(c1, r1, c2, r2, eps=eps_len):
    """
    두 원 (c1,r1), (c2,r2)의 교점 0/1/2개 반환.
    반환 순서(중요):
      u = (c2 - c1)/‖c2-c1‖,  n = (-u_y, u_x)
      → [ P + h*n,  P - h*n ]  == [left, right]  (c1→c2 기준)
    """
    x1, y1 = c1; x2, y2 = c2
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy)
    if d < eps or d > r1 + r2 + eps or d < abs(r1 - r2) - eps:
        return []
    a  = (r1*r1 - r2*r2 + d*d) / (2*d)
    h2 = max(r1*r1 - a*a, 0.0)
    h  = math.sqrt(h2)
    ux, uy = dx/d, dy/d
    px, py = x1 + a*ux, y1 + a*uy
    nx, ny = -uy, ux
    if h < eps:  # 두 원이 접하면 접점 한 개라 분기 선택 없어도 됨 → 점 하나(인덱스 0 한 개)
        return [(px, py)]
    return [(px + h*nx, py + h*ny), (px - h*nx, py - h*ny)]  # [left, right] → 기준 벡터의 왼쪽, 오른쪽 중 어느 점에 위치한 교점인지 → 점 두 개(인덱스 0, 1 두 개)

# 두 원의 교점 이용해 fingertip 좌표 바탕으로 5bar edge 구하기
def _ik_T_to_E(xT: float, yT: float, *, require_right: bool = True):
    """
    입력:  Fingertip(T) 좌표 T=(xT, yT)
    규칙:  PR_left = ⊙(O,l1_right) ∩ ⊙(T,T_to_P_R)의 (O→T 기준) left
          E_right = ⊙(T,T_to_E) ∩ ⊙(PR_left,l2_right)의 (T→PR_left 기준) right
    출력:  (x_edge, y_edge)
    정책:  E가 접점(교점 1개)이면 그 점을 그대로 반환(필터링 없음)
    """
    O = (0.0, 0.0)
    T = (xT, yT)

    # 1) PR_left
    PR_list = _circle_circle_intersections(O, l1_right, T, T_to_P_R)
    if not PR_list:
        raise ValueError("[E2T] PR 없음")
    PR_left = PR_list[0] # 규칙상(_circle_circle_intersection 참고) [0]=left (접점이면 1개)

    # 2) E_right (접점이면 그 한 점 사용)
    E_list = _circle_circle_intersections(T, T_to_E, PR_left, l2_right)
    if not E_list:
        raise ValueError("[E2T] E 없음")
    if len(E_list) == 1:
        xE, yE = E_list[0] # 접점 1개
    else:
        xE, yE = E_list[1] # 규칙상 [1]=right

    return xE, yE

# ===== 공개 함수 =====
def ik_5bar_Edge(x_user, y_user):
    """
    입력:  5bar linkage의  Edge 좌표
    출력:  (theta1_deg, theta2_deg)  -- 모터각=사용자각(도)
    실패:  ValueError (사유 메시지 포함)
    """
    xm, ym = _user_to_math(x_user, y_user)
    cands = _ik_candidates_math(xm, ym)
    if not cands:
        r = math.hypot(xm, ym)
        rL_min, rL_max = _r_range_left(); rR_min, rR_max = _r_range_right()
        raise ValueError(
            f"[IK] 작업공간 바깥 또는 특이점 (r={r:.1f}mm, "
            f"left∈[{rL_min:.1f},{rL_max:.1f}], right∈[{rR_min:.1f},{rR_max:.1f}])"
        )

    reasons = []
    for phi1, phi2 in cands:
        # (1) proximal link 순서 제약(ㅈ : motor1에 연결된 게 핑거팁에서 먼 쪽, motor2에 연결된 게 핑거팁에서 가까운 쪽의 proximal link여야 함)
        phi1_d = _deg360(phi1)
        phi2_d = _deg360(phi2)
        if (phi2_d - phi1_d > 0):
            if not (phi1_d + eps_ang < phi2_d):
                reasons.append(f"[IK] proximal angle order (φ1={phi1_d:.1f}° !< φ2={phi2_d:.1f}°)")
                continue
        else:
            if not (phi2_d + eps_ang < phi1_d):
                reasons.append(f"[IK] proximal angle order (φ1={phi1_d:.1f}° !< φ2={phi2_d:.1f}°)")
                continue

        # (2) 사용자각(=모터각)
        th1_deg, th2_deg = _phi_to_user_deg(phi1, phi2)

        # (3) 개별 범위
        if not (theta1_min_deg < th1_deg < theta1_max_deg):
            reasons.append(f"[IK] motor1 angle range (θ1 범위 위반) ({theta1_min_deg} < {th1_deg:.1f} < {theta1_max_deg})"); continue
        if not (theta2_min_deg < th2_deg < theta2_max_deg):
            reasons.append(f"[IK] motor2 angle range (θ2 범위 위반) ({theta2_min_deg} < {th2_deg:.1f} < {theta2_max_deg})"); continue

        # (4) 합 범위
        s = th1_deg + th2_deg
        if not (sum_min_deg < s < sum_max_deg):
            reasons.append(f"[IK] motor angle sum range(θ1+θ2 합 범위 위반) ({sum_min_deg} < {s:.1f} < {sum_max_deg})"); continue

        return th1_deg, th2_deg

    # 모든 후보 실패
    raise ValueError("; ".join(reasons) if reasons else "유효 해 없음")

def ik_5bar_fingerTip(x_fingertip, y_fingertip):
    """
    입력:  Fingertip(T) 좌표 T=(xT, yT)
    출력:  (theta1_deg, theta2_deg)  -- 모터각=사용자각(도)
    실패:  ValueError (사유 메시지 포함)
    """
    
    xE, yE = _ik_T_to_E(x_fingertip, y_fingertip)
    th1_deg, th2_deg = ik_5bar_Edge(xE, yE)

    return th1_deg, th2_deg

def fk_5bar_Edge(theta1_deg: float, theta2_deg: float):
    """
    입력: θ1, θ2 (사용자/모터 각, deg)
    출력: (xE_u, yE_u) — Edge E (사용자 좌표, mm)
    규칙: c1=PL, c2=PR로 원-원 교점 계산 → [left,right] 중 항상 right(=index 1) 선택
    """
    # (1) θ -> φ
    phi1, phi2 = _user_deg_to_phi(theta1_deg, theta2_deg)

    # (2) P_R 좌표
    PL_m = (l1_left  * math.cos(phi1), l1_left  * math.sin(phi1))
    PR_m = (l1_right * math.cos(phi2), l1_right * math.sin(phi2))

    # (3) 두 원 교점: [left, right]
    E_list = _circle_circle_intersections(PL_m, float(l2_left), PR_m, float(l2_right))

    if not E_list:
        raise ValueError("[FK-E] E 없음(조립 불가)")
    
    # if len(E_list) == 1:
    #     xE_m, yE_m = E_list[0] # 접점 1개
    # else:
    #     xE_m, yE_m = E_list[1] # 규칙상 [1] = right
   
    xE_m, yE_m = E_list[1] # 두 distal link가 수평이 돼서 distal link로 그린 두 원이 접할 정도로 proximal link가 벌어지지 않음. 만약 가능하면 위에 주석처리한 조건문 사용해야 함.

    xE_u, yE_u = _user_to_math(xE_m, yE_m)
    return xE_u, yE_u


def fk_5bar_fingerTip(theta1_deg: float, theta2_deg: float):
    """
    입력: θ1, θ2 (deg)
    출력: (xT_u, yT_u) — Fingertip T (사용자 좌표, mm)
    규칙: u = normalize(E-PR), w = R(CW 23.58°)*u, T = PR + T_to_P_R * w
    """
    # (1) θ → φ
    xE_u, yE_u = fk_5bar_Edge(theta1_deg, theta2_deg)
    xE_m, yE_m = _user_to_math(xE_u, yE_u)

    # (2) P_R 좌표
    _, phi2 = _user_deg_to_phi(theta1_deg, theta2_deg)
    xPR = l1_right * math.cos(phi2); yPR = l1_right * math.sin(phi2)

    # (3) distal link 방향벡터((E - P_R)/|E - P_R|) 구하기
    invR = 1.0 / float(l2_right)
    dx, dy = (xE_m - xPR)*invR, (yE_m - yPR)*invR

    # (4) CW 23.58 [deg] 회전 → (T - P_R)/|T - P_R|의 방향벡터 구하기
    ang = -math.radians(OFFSET_CW_DEG)
    c, s = math.cos(ang), math.sin(ang)
    ux, uy = c*dx - s*dy, s*dx + c*dy

    # (5) T = PR + T_to_P_R * u  → 사용자 좌표로 변환
    xT_m = xPR + T_to_P_R * ux
    yT_m = yPR + T_to_P_R * uy
    xT_u, yT_u = _user_to_math(xT_m, yT_m)
    return xT_u, yT_u
