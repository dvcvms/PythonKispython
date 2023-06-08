import math


def main(y, z, x):
    n = len(x)
    x = [0] + x
    y = [0] + y
    z = [0] + z
    res = 0
    for i in range(1, n + 1):
        res += math.ceil((72 * y[n + 1 - math.ceil(i / 2)] ** 2) - (z[math.ceil(i / 4)] ** 3) / 2 \
                         - x[n + 1 - math.ceil(i / 3)])
    return res * 25


res = main([-0.08, 0.82, -0.43, 0.21, -0.62],
           [0.02, 0.63, 0.85, 0.54, -0.74],
           [0.78, -0.31, -0.2, -0.39, 0.75])

print(res)
print('%.2e' % res)
