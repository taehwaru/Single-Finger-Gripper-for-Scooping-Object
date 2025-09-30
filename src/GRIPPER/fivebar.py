import math

# ===== 기구 파라미터 (mm) =====
l1_left  = 49.75   # 왼쪽 proximal link 길이
l1_right = 49.75   # 오른쪽 proximal link 길이, |P_R - O|
l2_left  = 35.0   # 왼쪽 distal link 길이
l2_right = 35.0   # 오른쪽 distal link 길이, |E - P_R|
T_to_P_R = 127.37 # 오른쪽 Proximal link(P_R)에서 fingerTip(T)까지의 거리, |T - P_R|
T_to_E = 96.32    # diamond linkage Edge(E)에서 fingerTip(T)까지의 거리, |T - E|

# ===== 각도 제약 (사용자각=모터각, 도) =====
# 사용자각(=모터각): 수직↓=0°, θ1(왼쪽 기울수록 +), θ2(오른쪽 기울수록 +)
theta1_min_deg = -161.2
theta1_max_deg =   76.0
theta2_min_deg = -144.4
theta2_max_deg =   93.4

# 두 모터 각도 합 제약 (도):  SUM_MIN < θ1+θ2 < SUM_MAX
sum_min_deg = -70.0
sum_max_deg =  -7.0

# 허용오차(도)
eps_ang = 1e-6 # unit : degree
eps_len = 1e-9 # unit : mm

# ===== 유틸 =====
def _clamp(x, lo=-1.0, hi=1.0): return max(lo, min(hi, x))
def _wrap_pi(a): return (a + math.pi) % (2*math.pi) - math.pi   # [-π, π)
def _deg(r): return r * 180.0 / math.pi
def _wrap_deg(a): return (a + 180.0) % 360.0 - 180.0            # [-180, 180)
def _deg360(r): return (_deg(r)) % 360.0                        # [0, 360)

# 사용자 좌표(+x=왼, +y=아래) <-> 수학 좌표(+x=오른, +y=위)
def _user_to_math(xu, yu): return -xu, -yu

# 각 측의 반경(필요조건)
def _r_range_left():  return abs(l1_left  - l2_left),  (l1_left  + l2_left)
def _r_range_right(): return abs(l1_right - l2_right), (l1_right + l2_right)

# IK 후보(수학좌표)
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
    # 두 분기 (phi1=왼, phi2=오)
    return [(tm + alphaL, tm - alphaR), (tm - alphaL, tm + alphaR)]

# φ(수학각, rad) → θ(사용자/모터각, deg)
# (현재 보정: theta = base - 45°  — m1 0° ↔ φ1=-45°, m2 0° ↔ φ2=-45°)
def _phi_to_user_deg(phi1, phi2):
    theta1_base = -_wrap_pi(phi1 + math.pi/2.0)
    theta2_base =  _wrap_pi(phi2 + math.pi/2.0)
    theta1 = _wrap_deg(_deg(theta1_base) - 45.0)
    theta2 = _wrap_deg(_deg(theta2_base) - 45.0)
    return theta1, theta2

# 두 원의 교점 구하기
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
    if h < eps:  # 접점 1개
        return [(px, py)]
    return [(px + h*nx, py + h*ny), (px - h*nx, py - h*ny)]  # [left, right]

# 두 원의 교점 이용해 fingertip 좌표 바탕으로 5bar edge 구하기
def _ik_T_to_E(xT: float, yT: float, *, require_right: bool = True):
    """
    입력:  Fingertip(T) 좌표 T=(xT, yT)
    규칙:  PR_left = ⊙(O,l1_right) ∩ ⊙(T,T_to_P_R)의 (O→T 기준) left
          E_right = ⊙(T,T_to_E) ∩ ⊙(PR_left,l2_right)의 (T→PR_left 기준) right
    출력:  (x_edge, y_edge)
    정책:  E가 접점(교점 1개)이면 그 점을 그대로 반환(필터링 없음).
    """
    O = (0.0, 0.0)
    T = (xT, yT)

    # 1) PR_left
    PR_list = _circle_circle_intersections(O, l1_right, T, T_to_P_R)
    if not PR_list:
        raise ValueError("[E2T] PR 없음")
    PR_left = PR_list[0]  # 규칙상 [0]=left (접점이면 1개)

    # 2) E_right (접점이면 그 한 점 사용)
    E_list = _circle_circle_intersections(T, T_to_E, PR_left, l2_right)
    if not E_list:
        raise ValueError("[E2T] E 없음")
    if len(E_list) == 1:
        xE, yE = E_list[0]      # 접점 1개
    else:
        xE, yE = E_list[1]      # 규칙상 [1]=right

    return xE, yE

# ===== 공개 함수 =====
def ik_5bar_angles_deg(x_user, y_user):
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
        # --- (1) 프록시멀 각도 순서 제약 ---
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

        # --- (2) 사용자각(=모터각) ---
        th1_deg, th2_deg = _phi_to_user_deg(phi1, phi2)

        # --- (3) 개별 범위 ---
        if not (theta1_min_deg < th1_deg < theta1_max_deg):
            reasons.append(f"[IK] motor1 angle range (θ1 범위 위반) ({theta1_min_deg} < {th1_deg:.1f} < {theta1_max_deg})"); continue
        if not (theta2_min_deg < th2_deg < theta2_max_deg):
            reasons.append(f"[IK] motor2 angle range (θ2 범위 위반) ({theta2_min_deg} < {th2_deg:.1f} < {theta2_max_deg})"); continue

        # --- (4) 합 범위 ---
        s = th1_deg + th2_deg
        if not (sum_min_deg < s < sum_max_deg):
            reasons.append(f"[IK] motor angle sum range(θ1+θ2 합 범위 위반) ({sum_min_deg} < {s:.1f} < {sum_max_deg})"); continue

        # 통과 → 반환
        return th1_deg, th2_deg

    # 모든 후보 실패
    raise ValueError("; ".join(reasons) if reasons else "유효 해 없음")

def ik_fingerTip_to_Edge(x_fingertip, y_fingertip):
    """
    입력:  Fingertip(T) 좌표 T=(xT, yT)
    출력:  (theta1_deg, theta2_deg)  -- 모터각=사용자각(도)
    실패:  ValueError (사유 메시지 포함)
    """
    
    xE, yE = _ik_T_to_E(x_fingertip, y_fingertip)
    th1_deg, th2_deg = ik_5bar_angles_deg(xE, yE)

    return th1_deg, th2_deg