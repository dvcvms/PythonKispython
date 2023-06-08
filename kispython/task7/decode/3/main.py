def main(x):
    x = int(x)
    a1 = 0b11 & (x >> 0)
    a2 = 0b111 & (x >> 2)
    a3 = 0b111111 & (x >> 5)
    a4 = 0b1 & (x >> 11)
    a5 = 0b111111 & (x >> 12)


    print((str(a1), str(a2), str(a3), str(a4), str(a5)))

main('166247')
main('232270')
main('224395')
main('222177')