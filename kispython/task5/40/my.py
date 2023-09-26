import math

def main(y, x, z):
    n = len(y)
    sum = 0
    for i in range(1, n + 1):
        a = z[n-i]
        b = 38 * x[i - 1] * x[i - 1]
        c = 44 * (y[math.ceil(i / 2) - 1] ** 3)

        sum += ((a - b - c) ** 5) * 44
    return sum

result = main([0.22, 0.68, -0.44, -0.7, 0.92, 0.33], [-0.29, -0.4, 0.39, -0.34, 0.7, 0.15], [-0.54, 0.4, 0.91, 0.22, -0.09, 0.18])
print(result)
print(f'{result:.2e}')