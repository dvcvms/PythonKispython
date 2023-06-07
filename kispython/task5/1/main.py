import math  # 1 Вариант


def main(x):
    n = len(x)
    x = [0] + x
    res = 0
    for i in range(1, n + 1):
        res += math.floor(x[math.ceil(i / 4)] ** 3 - 31 - 95 * x[i]) ** 4
    return (60 * res)

print('%.3e' % main([0.75, -0.17, -0.58, -0.84, 0.64, 0.85]))
print(main([0.75, -0.17, -0.58, -0.84, 0.64, 0.85]))
