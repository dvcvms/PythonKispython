
def main(x):

    z6 = int(x[0][1], 16) << 0
    z5 = int(x[1][1], 16) << 6
    z4 = int(x[2][1], 16) << 14
    z3 = int(x[3][1], 16) << 16
    z2 = int(x[4][1], 16) << 26
    z1 = int(x[5][1], 16) << 27

    return z1 + z2 + z3 + z4 + z5 + z6




print(main([('Z1', '0x3d'), ('Z2', '0x14'), ('Z3', '0x1'), ('Z4', '0x3e3'), ('Z5', '0x1'), ('Z6', '0x0')]))
print(main([('Z1', '0x9'), ('Z2', '0x39'), ('Z3', '0x3'), ('Z4', '0x372'), ('Z5', '0x1'), ('Z6', '0x1')]))
print(main([('Z1', '0x3d'), ('Z2', '0x14'), ('Z3', '0x1'), ('Z4', '0x3e3'), ('Z5', '0x1'), ('Z6', '0x0')]))
print(main([('Z1', '0x3d'), ('Z2', '0x14'), ('Z3', '0x1'), ('Z4', '0x3e3'), ('Z5', '0x1'), ('Z6', '0x0')]))
print(main([('Z1', '0x3d'), ('Z2', '0x14'), ('Z3', '0x1'), ('Z4', '0x3e3'), ('Z5', '0x1'), ('Z6', '0x0')]))
