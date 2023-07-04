import math


def main(z, x, y):
    ans = 0
    for i in range(1, len(z) + 1):
        yi = 78 * y[len(z) - math.ceil(i / 3)]
        zi = -7 * math.pow(z[i - 1], 3)
        xi = -67 * math.pow(x[i - 1], 2)
        si = 49 * math.pow(yi + zi + xi, 2)
        ans = ans + si
    return (53 * ans)
