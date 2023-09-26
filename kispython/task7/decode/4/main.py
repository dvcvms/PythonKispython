

def main(x):
    x = int(x, 16)

    u1 = 0b1111 & (x >> 0)
    u2 = 0b111111111 & (x >> 4)
    u3 = 0b111 & (x >> 13)

    return dict(U1=u1, U2=u2, U3=u3)

print(main('0xea97'))
print(main('0x1f6e'))
print(main('0xf1b7'))
print(main('0xe3a5'))
