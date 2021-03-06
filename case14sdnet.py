import numpy as np
def network():
    sdnet ={"version":'20151110'}
    sdnet["baseMVA"] = 100.00
    sdnet["Balance-p.u."] = True
    sdnet["node"] = np.array([
[1,1,0],
[2,2,0],
[3,3,0],
[4,4,0],
[5,5,0],
[6,6,0],
[7,7,0],
[8,8,0],
[9,9,0],
[10,10,0],
[11,11,0],
[12,12,0],
[13,13,0],
[14,14,0],
])
    sdnet["one-phase-line"] = np.array([
[9,-1,0.00000,0.19000,0.00000],
[1,2,4.99913,-15.26309,0.05280],
[1,5,1.02590,-4.23498,0.04920],
[2,3,1.13502,-4.78186,0.04380],
[2,4,1.68603,-5.11584,0.03400],
[2,5,1.70114,-5.19393,0.03460],
[3,4,1.98598,-5.06882,0.01280],
[4,5,6.84098,-21.57855,0.00000],
[6,11,1.95503,-4.09407,0.00000],
[6,12,1.52597,-3.17596,0.00000],
[6,13,3.09893,-6.10276,0.00000],
[7,8,0.00000,-5.67698,0.00000],
[7,9,0.00000,-9.09008,0.00000],
[9,10,3.90205,-10.36539,0.00000],
[9,14,1.42401,-3.02905,0.00000],
[10,11,1.88088,-4.40294,0.00000],
[12,13,2.48902,-2.25197,0.00000],
[13,14,1.13699,-2.31496,0.00000],
])
    sdnet["two-phase-line"] = np.array([
])
    sdnet["three-phase-line"] = np.array([
])
    sdnet["winding"] = np.array([
[4,-1,7,-1,0.00000,-4.78194,0.97800,0.00000],
[4,-1,9,-1,0.00000,-1.79798,0.96900,0.00000],
[5,-1,6,-1,0.00000,-3.96794,0.93200,0.00000],
])
    sdnet["I-load"] = np.array([
])
    sdnet["Z-load"] = np.array([
])
    sdnet["PQ-load"] = np.array([
[2,-1,0.21700,0.12700],
[3,-1,0.94200,0.19000],
[4,-1,0.47800,-0.03900],
[5,-1,0.07600,0.01600],
[6,-1,0.11200,0.07500],
[7,-1,0.00000,0.00000],
[8,-1,0.00000,0.00000],
[9,-1,0.29500,0.16600],
[10,-1,0.09000,0.05800],
[11,-1,0.03500,0.01800],
[12,-1,0.06100,0.01600],
[13,-1,0.13500,0.05800],
[14,-1,0.14900,0.05000],
])
    sdnet["one-phase-pv"] = np.array([
[2,-1,0.40000,1.04500,0.50000,-0.40000],
[3,-1,0.00000,1.01000,0.40000,0.00000],
[6,-1,0.00000,1.07000,0.24000,-0.06000],
[8,-1,0.00000,1.09000,0.24000,-0.06000],
])
    sdnet["three-phase-pv"] = np.array([
])
    sdnet["three-phase-vsc"] = np.array([
])
    sdnet["one-phase-switch"] = np.array([
])
    sdnet["one-phase-voltage-source"] = np.array([
[1,-1,1.06000,0.00000],
])
    return sdnet
