import math


def main(x):
    # y = bin(int(x))
    # while(len(y) < 34):
    #     y = y[0:2] + '0' + y[2:len(y)]
    # j1 = y[len(y) - 10:len(y)]
    # j2 = y[len(y) - 11]
    # j3 = y[len(y) - 14:len(y) - 11]
    # j4 = y[len(y) - 16:len(y) - 14]
    # j5 = y[len(y) - 24:len(y) - 16]
    # j4_5 = j5 + j4
    # j6 = y[len(y) - 32:len(y) - 24]
    # j66 = hex(int(j6, 2))
    # j45 = hex(int(j4_5, 2))
    # k = (hex(int(j1, 2)), hex(int(j2, 2)), hex(int(j3, 2)), j45, j66)
    j5 = bin(int(x.get('W5')))
    j4 = bin(int(x.get('W4')))
    j3 = bin(int(x.get('W3')))
    j2 = bin(int(x.get('W2')))
    j1 = bin(int(x.get('W1')))
    while(len(j5) < 10):
        j5 = j5[0:2] + '0' + j5[2:len(j5)]
    while(len(j4) < 4):
        j4 = j4[0:2] + '0' + j4[2:len(j5)]
    while(len(j3) < 8):
        j3 = j3[0:2] + '0' + j3[2:len(j5)]
    while(len(j2) < 6):
        j2 = j2[0:2] + '0' + j2[2:len(j5)]
    while(len(j1) < 4):
        j1 = j1[0:2] + '0' + j1[2:len(j5)]
    j5 = j5[2:len(j5)]
    j4 = j4[2:len(j4)]
    j3 = j3[2:len(j3)]
    j2 = j2[2:len(j2)]
    j1 = j1[2:len(j1)]
    k = int(j5 + j4 + j3 + j2 + j1, 2)
    return k
