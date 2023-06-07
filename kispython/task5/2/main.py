import math  # 4 Вариант


def main(y, z, x):
    n = len(x)
    x = [0] + x
    y = [0] + y
    z = [0] + z
    res = 0
    for i in range(1, n + 1):
        res += 24 * math.tan(y[i] - x[n + 1 - i] ** 3 - z[n + 1 - i] ** 2) ** 2
    return (4 * res)


# print(main([-0.52, -0.75, 0.27, -0.73, -0.46],
#            [-0.68, -0.3, -0.12, 0.42, -0.02],
#            [0.83, 0.62, -0.45, 0.46, -0.92]))
