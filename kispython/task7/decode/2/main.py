# Вариант 2
def main(a):
    # x = int(bin(a)[2:])
    x = a
    o2 = 0b1111 & (x >> 1)
    o3 = 0b11111111 & (x >> 5)
    o4 = 0b1111111 & (x >> 13)
    o5 = 0b11111 & (x >> 20)
    o6 = 0b111111111 & (x >> 25)
    print([("O2", o2), ("O3", o3), ("O4", o4), ("O5", o5), ("O6", o6)])

n = 1161494153
main(n)