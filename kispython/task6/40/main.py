def grace_lua(x, left, middle, right):
    if x[1] == 'GRACE':
        return left
    if x[1] == 'LUA':
        return middle
    return right


def bro(x, left, right):
    if x[0] == 'BRO':
        return left
    return right


def four(x, left, middle, right):
    if x[4] == 1978:
        return left
    if x[4] == 2006:
        return middle
    return right


def main(x):
    if x[3] == 2015:
        if x[2] == 'UNO':
            return grace_lua(x, bro(x, 0, 1), four(x, 2, 3, 4), bro(x, 5, 6))
        if x[2] == 'BRO':
            return four(x, grace_lua(x, 7, 8, 9), 10, 11)
    if x[3] == 1983:
        return 12
    return 13