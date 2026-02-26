def pack4(a, b, c, d):
    if c == 0:
        c, d = d, 0
    if b == 0:
        b, c, d = c, d, 0
    if a == 0:
        a, b, c, d = b, c, d, 0

    if a == b:
        a, b, c, d = 2 * a, c, d, 0
    if b == c:
        b, c, d = 2 * b, d, 0
    if c == d:
        c, d = 2 * c, 0

    return a, b, c, d
print(pack4(0,2,0,2))
print(pack4(0,0,8,8))
print(pack4(2,32,0,32))
