import numpy as np
def network():
    sdnet ={"version":'20151110'}
    sdnet["baseMVA"] = 100.00
    sdnet["Balance-p.u."] = False
    sdnet["node"] = np.array([
[1,1,66.395000],
[2,1,66.395000],
[3,1,66.395000],
[4,1,2.401800],
[5,1,2.401800],
[6,1,2.401800],
[7,1,2.401800],
[8,1,2.401800],
[9,1,2.401800],
[10,1,2.401800],
[11,1,2.401800],
[12,1,2.401800],
[13,1,0.277130],
[14,1,0.277130],
[15,1,0.277130],
[16,1,2.401800],
[17,1,2.401800],
[18,1,2.401800],
[19,1,2.401800],
[38,1,2.401800],
[20,1,2.401800],
[21,1,2.401800],
[23,1,2.401800],
[39,1,2.401800],
[22,1,2.401800],
[24,1,2.401800],
[25,1,2.401800],
[26,1,2.401800],
[27,1,2.401800],
[28,1,2.401800],
[29,1,2.401800],
[30,1,2.401800],
[31,1,2.401800],
[32,1,2.401800],
[33,1,2.401800],
[34,1,2.401800],
[35,1,2.401800],
[36,1,2.401800],
[37,1,2.401800],
[40,1,2.401800],
[41,1,2.401800],
])
    sdnet["one-phase-line"] = np.array([
[41,27,0.37668221,-0.38186824,0.00000000],
[40,28,0.24753090,-0.09447660,0.00000039],
])
    sdnet["two-phase-line"] = np.array([
[34,33,38,19,0.24833567,-0.08333386,-0.08333386,0.25006170,-0.23104246,0.03458816,0.03458816,-0.22998756,0.00000000,-0.00000000,-0.00000000,0.00000000],
[38,19,21,20,0.41389278,-0.13888976,-0.13888976,0.41676951,-0.38507076,0.05764694,0.05764694,-0.38331260,0.00000000,-0.00000000,-0.00000000,0.00000000],
[16,18,40,41,0.41389278,-0.13888976,-0.13888976,0.41676951,-0.38507076,0.05764694,0.05764694,-0.38331260,0.00000000,-0.00000000,-0.00000000,0.00000000],
])
    sdnet["three-phase-line"] = np.array([
[7,8,9,32,33,34,0.06605620,-0.02802662,-0.01534757,-0.02802662,0.05784125,-0.00728588,-0.01534757,-0.00728588,0.05115022,    -0.19039467,0.07039233,0.05262110,0.07039233,-0.18041776,0.04018905,0.05262110,0.04018905,-0.17020457,    0.00000001,-0.00000000,-0.00000000,-0.00000000,0.00000001,-0.00000000,-0.00000000,-0.00000000,0.00000001    ],
[32,33,34,29,30,31,0.19806956,-0.08403785,-0.04601970,-0.08403785,0.17343703,-0.02184670,-0.04601970,-0.02184670,0.15337399,    -0.57089857,0.21107144,0.15778440,0.21107144,-0.54098278,0.12050691,0.15778440,0.12050691,-0.51035854,    0.00000000,-0.00000000,-0.00000000,-0.00000000,0.00000000,-0.00000000,-0.00000000,-0.00000000,0.00000000    ],
[29,30,31,16,17,18,0.09910908,-0.04205045,-0.02302711,-0.04205045,0.08678357,-0.01093155,-0.02302711,-0.01093155,0.07674452,    -0.28566343,0.10561489,0.07895138,0.10561489,-0.27069431,0.06029866,0.07895138,0.06029866,-0.25537070,    0.00000001,-0.00000000,-0.00000000,-0.00000000,0.00000001,-0.00000000,-0.00000000,-0.00000000,0.00000001    ],
[16,17,18,35,36,37,0.13211240,-0.05605324,-0.03069514,-0.05605324,0.11568250,-0.01457175,-0.03069514,-0.01457175,0.10230045,    -0.38078935,0.14078465,0.10524219,0.14078465,-0.36083552,0.08037811,0.10524219,0.08037811,-0.34040915,    0.00000001,-0.00000000,-0.00000000,-0.00000000,0.00000001,-0.00000000,-0.00000000,-0.00000000,0.00000001    ],
[32,33,34,10,11,12,0.32099444,-0.08624783,-0.12341559,-0.08624783,0.28314850,-0.06276251,-0.12341559,-0.06276251,0.29933846,    -0.41151330,0.08686815,0.09749416,0.08686815,-0.40745250,0.07974335,0.09749416,0.07974335,-0.40873258,    0.00000000,-0.00000000,-0.00000000,-0.00000000,0.00000000,-0.00000000,-0.00000000,-0.00000000,0.00000000    ],
[23,39,22,24,25,26,0.59522842,-0.13964112,-0.06216966,-0.13964112,0.66033189,-0.13964112,-0.06216966,-0.13964112,0.59522842,    -0.44808575,0.17324210,0.14181793,0.17324210,-0.46670563,0.17324210,0.14181793,0.17324210,-0.44808575,    0.00000026,0.00000000,0.00000000,0.00000000,0.00000026,0.00000000,0.00000000,0.00000000,0.00000026    ],
[16,17,18,23,39,22,576864.32400000,0.00000000,0.00000000,0.00000000,576864.32400000,0.00000000,0.00000000,0.00000000,576864.32400000,    0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,    0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000    ],
])
    sdnet["winding"] = np.array([
[1,-1,4,-1,1538.46154,-12307.69231,1.00000,0.00000],
[2,-1,5,-1,1538.46154,-12307.69231,1.00000,0.00000],
[3,-1,6,-1,1538.46154,-12307.69231,1.00000,0.00000],
[4,-1,7,-1,5000.00000,-5000.00000,1.00000,0.00000],
[5,-1,8,-1,5000.00000,-5000.00000,1.00000,0.00000],
[6,-1,9,-1,5000.00000,-5000.00000,1.00000,0.00000],
[10,-1,13,-1,21.11324,-38.38772,1.00000,0.00000],
[11,-1,14,-1,21.11324,-38.38772,1.00000,0.00000],
[12,-1,15,-1,21.11324,-38.38772,1.00000,0.00000],
])
    sdnet["I-load"] = np.array([
])
    sdnet["Z-load"] = np.array([
])
    sdnet["PQ-load"] = np.array([
[13,-1,0.00160,0.00110],
[14,-1,0.00120,0.00090],
[15,-1,0.00120,0.00090],
[19,-1,0.00170,0.00125],
[24,-1,0.00485,0.00190],
[25,-1,0.00068,0.00060],
[26,-1,0.00290,0.00212],
[29,-1,0.00017,0.00010],
[30,-1,0.00066,0.00038],
[31,-1,0.00117,0.00068],
])
    sdnet["one-phase-pv"] = np.array([
])
    sdnet["three-phase-pv"] = np.array([
])
    sdnet["three-phase-vsc"] = np.array([
])
    sdnet["one-phase-switch"] = np.array([
])
    sdnet["one-phase-voltage-source"] = np.array([
[1,-1,1.00000,0.00000],
[2,-1,0.50000,-0.88600],
[3,-1,0.50000,0.88600],
])
    return sdnet