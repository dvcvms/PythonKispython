import math


def main(x, y):
    n = len(x)
    sum = 0
    for i in range(1, n):
        a = 30 * (y[n - math.ceil(i / 3)] ** 2)
        b = x[math.ceil(i / 4) - 1]

        sum += math.log((1 - a - b), 10) ** 4
    return sum * 61


result = main([-0.16, 0.15, 0.29, -0.08, -0.88],
              [-0.1, 0.42, -0.75, -0.03, -0.01])

print(result)
