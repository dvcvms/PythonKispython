def main(x):
    x1 = x['C1'] << 0
    x2 = x['C2'] << 8
    x3 = x['C3'] << 16
    x4 = x['C4'] << 23
    x5 = x['C5'] << 26
    x6 = x['C6'] << 28

    print(hex(x6 + x5 + x4 + x3 + x2 + x1))


main({'C1': 220, 'C2': 149, 'C3': 124, 'C4': 2, 'C5': 2, 'C6': 52})