def main(x):
    x = int(x, 16) # 10 сс
    o2 = 0b111 & (x >> 5)
    o3 = 0b1111 & (x >> 8)
    o4 = 0b1111 & (x >> 12)

    o2 = o2 << 4
    o3 = o3 << 0 # не говори так
    o4 = o4 << 7

    y = o2 + o3 + o4
    print(y)


n = '0x38e9'
main(n)
