import string

f = open('post_agc_cw_lp.txt', 'w')

k =[0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    1,    1,    1,    1,    1,    1,    2,  
    2,    2,    3,    3,    3,    3,    4,    4,    4,    4,    5,    5,    5,    5,    5,    5,    5,  
    4,    4,    4,    3,    2,    2,    1,    0,  -1,  -2,  -4,  -5,  -7,  -8,  -10,  -12,  -14,  
  -16,  -18,  -20,  -22,  -24,  -26,  -28,  -31,  -33,  -34,  -36,  -38,  -40,  -41,  -42,  
  -43,  -44,  -45,  -45,  -45,  -44,  -44,  -42,  -41,  -39,  -37,  -34,  -31,  -27,  -23,  
  -18,  -13,  -7,  -1,    6,    13,    20,    28,    37,    46,    55,    65,    75,    85,    96,  
    107,    119,    130,    142,    154,    166,    178,    190,    202,    214,    226,    238,    249,  
    260,    271,    282,    292,    302,    312,    321,    329,    337,    344,    351,    357,    362,  
    366,    370,    373,    376,    377,    378]


for i in range (0,128):
    if k[i] >= 0:
        f.write('    "{0:010b}",\n'.format(k[i]))
    else:
        f.write('    "{0:010b}",\n'.format(1024+k[i]))
#f.write( "%d\n" % k[i]
