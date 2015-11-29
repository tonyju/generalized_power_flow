import numpy as np
def network():
    sdnet ={"version":'20151110'}
    sdnet["baseMVA"] = 100.00
    sdnet["Balance-p.u."] = True
    sdnet["node"] = np.array([
[1,1,345],
[2,2,345],
[3,3,345],
[4,4,345],
[5,5,345],
[6,6,345],
[7,7,345],
[8,8,345],
[9,9,345],
])
    sdnet["one-phase-line"] = np.array([
[1,4,0.00000,-17.36111,0.00000],
[4,5,1.94219,-10.51068,0.15800],
[5,6,1.28201,-5.58824,0.35800],
[3,6,0.00000,-17.06485,0.00000],
[6,7,1.15509,-9.78427,0.20900],
[7,8,1.61712,-13.69798,0.14900],
[8,2,0.00000,-16.00000,0.00000],
[8,9,1.18760,-5.97513,0.30600],
[9,4,1.36519,-11.60410,0.17600],
])
    sdnet["two-phase-line"] = np.array([
])
    sdnet["three-phase-line"] = np.array([
])
    sdnet["winding"] = np.array([
])
    sdnet["I-load"] = np.array([
])
    sdnet["Z-load"] = np.array([
])
    sdnet["PQ-load"] = np.array([
[4,-1,0.00000,0.00000],
[5,-1,0.90000,0.30000],
[6,-1,0.00000,0.00000],
[7,-1,1.00000,0.35000],
[8,-1,0.00000,0.00000],
[9,-1,1.25000,0.50000],
])
    sdnet["one-phase-pv"] = np.array([
[2,-1,1.63000,1.00000,3.00000,-3.00000],
[3,-1,0.85000,1.00000,3.00000,-3.00000],
])
    sdnet["three-phase-pv"] = np.array([
])
    sdnet["three-phase-vsc"] = np.array([
])
    sdnet["one-phase-switch"] = np.array([
])
    sdnet["one-phase-voltage-source"] = np.array([
[1,-1,1.00000,0.00000],
])
    return sdnet
