def pack4(a, b, c, d):
# --- partie ou on enlève les 0 vvv ---#
    if c == 0:
        c, d = d, 0
    if b == 0:
        b, c, d = c, d, 0
    if a == 0:
        a, b, c, d = b, c, d, 0
#--- partie ou on fusionne vvv ---#

    if a == b and a > 0:
        a, b, c, d = a+1, c, d, 0
    if b == c and b > 0:
        b, c, d = b+1, d, 0
    if c == d and c > 0:
        c, d = c+1, 0

    return a, b, c, d
print(pack4(0,1,0,3))
print(pack4(0,0,2,3))
print(pack4(1,1,2,0))
