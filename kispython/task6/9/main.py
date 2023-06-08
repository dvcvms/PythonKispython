def x4_1959(x):
    x4 = x[4]
    if x4 == 1993:
        return 8
    if x4 == 2002:
        return 9


def x0_ioke_slim(x, left, middle, right):
    x0 = x[0]
    if x0 == 2005:
        return left
    if x0 == 1959:
        return middle
    if x0 == 1993:
        return right


def x0_1973(x):
    x0 = x[0]
    if x0 == 2005:
        return 7
    if x0 == 1959:
        return x4_1959(x)
    if x0 == 1993:
        return 10


def x2_1963(x):
    x2 = x[2]
    if x2 == 'IOKE':
        x0_ioke_slim(x, 0, 1, 2)
    if x2 == 'CLEAN':
        return 3
    if x2 == 'SLIM':
        x0_ioke_slim(x, 4, 5, 6)


def x1_1998(x):
    x1 = x[1]
    if x1 == 1963:
        return x2_1963(x)
    if x1 == 1973:
        return x0_1973(x)
    return 11


def main(x):
    x3 = x[3]
    if x3 == 1979:
        return 12
    if x3 == 2018:
        return 13
    return x1_1998(x)


print(main([1959, 1963, 'CLEAN', 2018, 1993]))
print(main([1993, 2002, 'IOKE', 1998, 1993]))
print(main([1993, 1973, 'CLEAN', 1998, 2002]))
print(main([1959, 2002, 'CLEAN', 1979, 2002]))
print(main([2005, 1973, 'IOKE', 1998, 2002]))
