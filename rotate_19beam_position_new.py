#!/usr/bin/env python3
import sys
import numpy as np
import ephem

D2R = np.pi / 180.0
R2D = 180.0 / np.pi


def fmt_ra_deg(ra_deg):
    """RA 角度(度) -> hh:mm:ss.sss，自动归一化到 [0,360)。"""
    ra_deg = ra_deg % 360.0
    h = ra_deg / 15.0
    hh = int(h)
    mm = int((h - hh) * 60.0)
    ss = ((h - hh) * 60.0 - mm) * 60.0
    return f"{hh:02d}:{mm:02d}:{ss:07.4f}"


def fmt_dec_deg(dec_deg):
    """Dec 角度(度) -> +dd:mm:ss.sss。"""
    sign = '-' if dec_deg < 0 else '+'
    dec = abs(dec_deg)
    dd = int(dec)
    mm = int((dec - dd) * 60.0)
    ss = ((dec - dd) * 60.0 - mm) * 60.0
    return f"{sign}{dd:02d}:{mm:02d}:{ss:06.3f}"


def spherical_offset(ra0_deg, dec0_deg, dist_arcmin, ang_deg):
    """
    严格球面三角偏移。
    ra0_deg, dec0_deg: 中心赤经、赤纬，单位度
    dist_arcmin: 波束与中心角距离，单位角分
    ang_deg: 方位角，0=沿RA增加方向，90=沿Dec增加方向
    返回: ra_deg, dec_deg
    """
    a0 = ra0_deg * D2R
    d0 = dec0_deg * D2R
    d = (dist_arcmin / 60.0) * D2R
    th = ang_deg * D2R

    sin_dec = np.sin(d0) * np.cos(d) + np.cos(d0) * np.sin(d) * np.sin(th)
    sin_dec = np.clip(sin_dec, -1.0, 1.0)
    dec = np.arcsin(sin_dec)

    dra = np.arctan2(
        np.sin(d) * np.cos(th),
        np.cos(d0) * np.cos(d) - np.sin(d0) * np.sin(d) * np.sin(th)
    )

    ra = a0 + dra
    ra = np.mod(ra, 2.0 * np.pi)

    return ra * R2D, dec * R2D


def flat_offset(ra0_deg, dec0_deg, dist_arcmin, ang_deg):
    """原代码使用的平面小角度近似，仅用于误差对比。"""
    d = dist_arcmin / 60.0
    th = ang_deg * D2R
    ra = ra0_deg + d * np.cos(th) / np.cos(dec0_deg * D2R)
    dec = dec0_deg + d * np.sin(th)
    return ra % 360.0, dec


def main():
    # 参数：ra dec [ang]
    # 例如：python rotate_19beam_position.py 20:00:00 20:00:00 23.4
    if len(sys.argv) < 3:
        ra0_deg = float(ephem.hours('20:00:00')) * R2D
        dec0_deg = float(ephem.degrees('20:00:00')) * R2D
        ang = 23.4
    else:
        ra0_deg = float(ephem.hours(sys.argv[1])) * R2D
        dec0_deg = float(ephem.degrees(sys.argv[2])) * R2D
        ang = float(sys.argv[3]) if len(sys.argv) >= 4 else 23.4

    d0_arcmin = 5.74

    print("center:", fmt_ra_deg(ra0_deg), fmt_dec_deg(dec0_deg))
    print("center deg:", ra0_deg, dec0_deg)
    print("ang =", ang)

    beams = []

    # M02-M07：内圈 6 个，半径 5.74'
    for i in range(6):
        beams.append((f"M{2+i:02d}", d0_arcmin, ang - 60.0 * i))

    # M08-M19：外圈 12 个
    # 偶数 i：半径 2*5.74'
    # 奇数 i：半径 sqrt(3)*5.74'
    for i in range(12):
        if i % 2 == 0:
            dist = 2.0 * d0_arcmin
        else:
            dist = np.sqrt(3.0) * d0_arcmin
        beams.append((f"M{8+i:02d}", dist, ang - 30.0 * i))

    for name, dist_arcmin, theta in beams:
        ra_s, dec_s = spherical_offset(ra0_deg, dec0_deg, dist_arcmin, theta)
        ra_f, dec_f = flat_offset(ra0_deg, dec0_deg, dist_arcmin, theta)

        # 天球上的 RA 方向偏差应按 dRA*cos(dec) 计算
        dra_arcsec = ((ra_s - ra_f + 180.0) % 360.0 - 180.0) * 3600.0 * np.cos(dec_s * D2R)
        ddec_arcsec = (dec_s - dec_f) * 3600.0

        print(
            f"{name}  "
            f"sphere {fmt_ra_deg(ra_s)} {fmt_dec_deg(dec_s)}  "
            f"flat {fmt_ra_deg(ra_f)} {fmt_dec_deg(dec_f)}  "
            f"diff(arcsec): dRA*cosdec={dra_arcsec:+.3f}, dDec={ddec_arcsec:+.3f}"
        )


if __name__ == "__main__":
    main()
