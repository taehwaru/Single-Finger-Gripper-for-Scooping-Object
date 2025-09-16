import math

# ===== 기구 파라미터 (mm) =====
l1_left  = 50.0   # 왼쪽 proximal link 길이
l1_right = 49.5   # 오른쪽 proximal link 길이
l2_left  = 35.0   # 왼쪽 distal link 길이
l2_right = 35.0   # 오른쪽 distal link 길이

# ===== 각도 제약 (사용자각=모터각, 도) =====
# 사용자각(=모터각): 수직↓=0°, θ1(왼쪽 기울수록 +), θ2(오른쪽 기울수록 +)
THETA1_MIN_DEG = -161.2
THETA1_MAX_DEG =   76.0
THETA2_MIN_DEG = -144.4
THETA2_MAX_DEG =   93.4

# 두 모터 각도 합 제약 (도):  SUM_MIN < θ1+θ2 < SUM_MAX
SUM_THETA_MIN_DEG = -70.0
SUM_THETA_MAX_DEG =  -6.4

# 프록시멀 각 비교 허용오차(도)
ANG_TOL_DEG = 1e-6

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
def _ik_candidates_math(xm, ym, eps=1e-9):
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

# ===== 공개 함수 =====
def ik_5bar_angles_deg(x_user, y_user):
    """
    입력:  x_user, y_user  (사용자 좌표: +x=왼쪽, +y=아래)
    출력:  (theta1_deg, theta2_deg)  -- 모터각=사용자각(도)
    실패:  ValueError (사유 메시지 포함)
    """
    xm, ym = _user_to_math(x_user, y_user)
    cands = _ik_candidates_math(xm, ym)
    if not cands:
        r = math.hypot(xm, ym)
        rL_min, rL_max = _r_range_left(); rR_min, rR_max = _r_range_right()
        raise ValueError(
            f"작업공간 바깥 또는 특이점 (r={r:.1f}mm, "
            f"left∈[{rL_min:.1f},{rL_max:.1f}], right∈[{rR_min:.1f},{rR_max:.1f}])"
        )

    reasons = []
    for phi1, phi2 in cands:
        # --- (1) 프록시멀 각도 순서 제약 ---
        phi1_d = _deg360(phi1)
        phi2_d = _deg360(phi2)
        if (phi2_d - phi1_d > 0):
            if not (phi1_d + ANG_TOL_DEG < phi2_d):
                reasons.append(f"proximal angle order fail (φ1={phi1_d:.1f}° !< φ2={phi2_d:.1f}°)")
                continue
        else:
            if not (phi2_d + ANG_TOL_DEG < phi1_d):
                reasons.append(f"proximal angle order fail (φ1={phi1_d:.1f}° !< φ2={phi2_d:.1f}°)")
                continue

        # --- (2) 사용자각(=모터각) ---
        th1_deg, th2_deg = _phi_to_user_deg(phi1, phi2)

        # --- (3) 개별 범위 ---
        if not (THETA1_MIN_DEG < th1_deg < THETA1_MAX_DEG):
            reasons.append(f"θ1 범위 위반 ({THETA1_MIN_DEG} < {th1_deg:.1f} < {THETA1_MAX_DEG})"); continue
        if not (THETA2_MIN_DEG < th2_deg < THETA2_MAX_DEG):
            reasons.append(f"θ2 범위 위반 ({THETA2_MIN_DEG} < {th2_deg:.1f} < {THETA2_MAX_DEG})"); continue

        # --- (4) 합 범위 ---
        s = th1_deg + th2_deg
        if not (SUM_THETA_MIN_DEG < s < SUM_THETA_MAX_DEG):
            reasons.append(f"θ1+θ2 합 범위 위반 ({SUM_THETA_MIN_DEG} < {s:.1f} < {SUM_THETA_MAX_DEG})"); continue

        # 통과 → 반환
        return th1_deg, th2_deg

    # 모든 후보 실패
    raise ValueError("; ".join(reasons) if reasons else "유효 해 없음")