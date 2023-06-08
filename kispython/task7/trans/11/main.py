# def main(x):
#     x = int(x, 16)
#     d1 = 0b111111 & (x >> 0)
#     d2 = 0b1111 & (x >> 6)
#     d3 = 0b11111 & (x >> 10)
#     d4 = 0b111111 & (x >> 15)
#
#     d1 = d1 << 21
#     d2 = d2 << 0
#     d3 = d3 << 10
#     d4 = d4 << 4
#
#     y = d1 + d2 + d3 + d4
#     print(y)
#
# main('0x194b')
# main('0x13d7')
# main('0x369')
# main('0x8de')

def main(x):
    x = int(x, 16)  # 10 сс
    o1 = 0b11111111 & (x >> 0)
    o2 = 0b11111111 & (x >> 8)
    o3 = 0b111 & (x >> 16)
    o4 = 0b1111111 & (x >> 19)

    o1 = o1 << 18
    o2 = o2 << 10
    o3 = o3 << 7  # не говори так
    o4 = o4 << 0

    y = o1 + o2 + o3 + o4
    print(y)


main('0x25dd513')
main('0x23d2968')
main('0x2a1bbd5')
main('0x23add3f')