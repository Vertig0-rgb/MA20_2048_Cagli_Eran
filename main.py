#Eran cagli
#05.02.2026
# projet 2048 MA-20

import tkinter as tk
from importlib.metadata import entry_points
from tkinter import mainloop
# --- DEF + VARIABLE ---
def display():

    for line in range(len(game)):
        for col in range(len(game[line])):
            value = game[line][col]
            font_color = "black" if 0< value < 10 else "white"
            labels[line][col].configure(text=value,bg=tuiles_colors[value],fg=font_color)

            if game[line][col] == 0:
                text=""
            else :
                text = str(2 ** game[line][col])


            labels[line][col].config(text=text, bg=tuiles_colors[game[line][col]])


"""
game = [[0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]]
"""
game = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,0,0,0]]

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



# --- CODE GENERAL  + TITRE ---
window = tk.Tk()
window.geometry("800x650")
window.title("MA20_2048_Cagli Eran")
window.configure(bg=tuiles_colors[1])

frame = tk.Frame(window, bg=tuiles_colors[1])
frame.pack()

frame_game = tk.Frame(window)
frame_game.pack()

lbl_2048 = tk.Label(frame, text="2048", font=("Arial", 35),bg=tuiles_colors[1])
lbl_2048.grid(row=0, column=2)

btn_newgame = tk.Button(frame, text="nouvelle partie", font=("Arial", 18),background="#FFE6CC")
btn_newgame.grid(row=1, column=2)

lbl_score = tk.Label(frame, text="score:", font=("Arial", 25),bg=tuiles_colors[1])
lbl_score.grid(row=2, column=1)

lbl_record = tk.Label(frame, text="record:", font=("Arial", 25),bg=tuiles_colors[1])
lbl_record.grid(row=2, column=3)

ent_score = tk.Label(frame, text="", font=("Arial", 10, "bold"), height=4,width=20, relief="sunken")
ent_score.grid(row=3, column=1)

ent_record = tk.Label(frame, text="", font=("Arial", 10, "bold"), height=4,width=20, relief="sunken")
ent_record.grid(row=3, column=3, pady=10)

for line in range(len(game)):
    for col in range(len(game[line])):
        # creation without placement
        labels[line][col] = tk.Label (frame_game, width=8, height=4, borderwidth=1, relief="solid", font=("Arial", 15))
        labels[line][col].grid(row=line + 1, column=col)

display()
mainloop()