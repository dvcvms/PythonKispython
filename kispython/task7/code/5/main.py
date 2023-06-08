def main(x):

    m1 = x[0]
    m2 = x[1]
    m3 = x[2]

    m1 = int(m1, 16)
    m2 = int(m2, 16)
    m3 = int(m3, 16)

    m1 = m1 << 0
    m2 = m2 << 7
    m3 = m3 << 13

    print(m1 + m2 + m3)

main(('0x5', '0x35', '0xe0'))
main(('0x2d', '0x36', '0x2ce'))
main(('0x5b', '0x1', '0x296'))
main(('0x9', '0x29', '0x17e'))
