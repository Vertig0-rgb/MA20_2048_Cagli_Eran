
game = [[0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]]
"""

game = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,0,0,0]]
"""
labels=[[None,None,None,None],
        [None,None,None,None],
        [None,None,None,None],
        [None,None,None,None]]


tuiles_colors={0:"#EEEEEE",
               1:"#FFFFFF",
               2:"#DAE8FC",
               3:"#D5E8D4",
               4:"#FFE6CC",
               5:"#F8CECC",
               6:"#E1D5E7",
               7:"#FFCC99",
               8:"#FFFF88",
               9:"#CDEB8B",
               10:"#0050EF",
               11:"#6A00FF",
               12:"#D80073",
               13:"#A20025"}




def pack4(a, b, c, d):
# --- partie ou on enlève les 0 vvv ---#

    if c == 0:
        c, d = d, 0
    if b == 0:
        b, c, d = c, d, 0
    if a == 0:
        a, b, c, d = b, c, d, 0
#--- partie ou on fusionne vvv ---#

    if a == b and a >0 :
        a, b, c, d = a+1, c, d, 0
    if b == c and b >0 :
        b, c, d = b+1, d, 0
    if c == d and c >0:
        c, d = c+1, 0

    return a, b, c, d

def down():
    for col in range(4):
        (game[3][col],game[2][col],game[1][col],game[0][col])= pack4(game[3][col],game[2][col],game[1][col],game[0][col])

def up():
    for col in range(4):
        (game[0][col],game[1][col],game[2][col],game[3][col])= pack4(game[0][col],game[1][col],game[2][col],game[3][col])

def right():
    for line in range(4):
        (game[line][3],game[line][2],game[line][1],game[line][0])= pack4(game[line][3],game[line][2],game[line][1],game[line][0])

def left():
    for line in range(4):
        (game[line][0],game[line][1],game[line][2],game[line][3])= pack4(game[line][0],game[line][1],game[line][2],game[line][3])
