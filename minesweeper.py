from tkinter import *
from easygui import *
from tkinter import messagebox
from random import *
import time

x = int(integerbox("Sissestage mänguväljaku pikkus 5-30:",lowerbound = 5, upperbound = 30))
y = int(integerbox("Sissestage mänguväljaku laius 5-30:",lowerbound = 5, upperbound = 30))
bomb_count = int(integerbox("Sissestage pommide arv 1-"+ str(x*y) + " :",lowerbound = 1, upperbound = x*y))



#=======================================================================================

def field_create(x,y,bomb):
    field = []
    for rida in range(x):
        field.append([])
        for el in range(y):
            field[rida].append(0)
    while bomb != 0:
        i = randint(0,x-1)
        j = randint(0,y-1)
        if field[i][j] != "pomm":
            field[i][j] = "pomm"
            bomb -= 1
    for rida in range(x):
        for el in range(y):
            if field[rida][el] != "pomm":
                if el > 0:
                    if field[rida][el-1] == "pomm":
                        field[rida][el] += 1
                if el < (y-1):
                    if field[rida][el+1] == "pomm":
                        field[rida][el] += 1
                if rida < (x-1) and el < (y-1):
                    if field[rida+1][el+1] == "pomm":
                        field[rida][el] += 1
                if rida < (x-1):
                    if field[rida+1][el] == "pomm":
                        field[rida][el] += 1
                if el > 0 and rida < (x-1):
                    if field[rida+1][el-1] == "pomm":
                        field[rida][el] += 1
                if rida > 0 and el < (y-1):
                    if field[rida-1][el+1] == "pomm":
                        field[rida][el] += 1
                if rida > 0:
                    if field[rida-1][el] == "pomm":
                        field[rida][el] += 1
                if rida > 0 and el > 0:
                    if field[rida-1][el-1] == "pomm":
                        field[rida][el] += 1
    return(field)

#=======================================================================================
def LeftClick_w(click):
    return lambda Button: leftClick(click)
def RightClick_w(click):
    return lambda Button: rightClick(click)


#=======================================================================================
def leftClick(click):
    if buttons[click][1] != "pomm":
        if buttons[click][5] != 1:
            buttons[click][0].config(state="disabled",relief=SUNKEN)
            buttons[click][5] = 2
            if buttons[click][1] != 0:
                buttons[click][0].config(text=str(buttons[click][1]))
            if buttons[click][1] == 0:
                check(click)
    elif buttons[click][5] != 1:
        messagebox.showinfo(title="Game Over", message="BOOooom! Pomm plahvatas.")
        raam.destroy()


        
def rightClick(click):
    bomb_count = buttons[1][8]
    flag_count = 0
    for x in range(buttons[1][6]*buttons[1][7]):
        if buttons[x][5] == 1:
            flag_count += 1
    if buttons[click][5] == 0:
        if flag_count < bomb_count:
            buttons[click][0].config(bg='blue')
            buttons[click][5] = 1
            check_win(click)
    elif buttons[click][5] == 1:
        buttons[click][0].config(bg='#f0f0ed')
        buttons[click][5] = 0



#=======================================================================================

def check(click):
    buttons[click][5] = 2
    if click > 0:
        if buttons[click-1][1] != "pomm":
            if buttons[click-1][4] != 1:
                if buttons[click][3] > 0:
                    buttons[click-1][0].config(state="disabled",relief=SUNKEN,bg='#f0f0ed')
                    if buttons[click-1][1] != 0:
                        buttons[click-1][4] = 1
                        buttons[click-1][5] = 2
                        buttons[click-1][0].config(text=str(buttons[click-1][1]))
                    if buttons[click-1][1] == 0:
                        buttons[click-1][4] = 1
                        check(click-1)
    if click < (buttons[1][6]*buttons[1][7]-1):
        if buttons[click+1][1] != "pomm":
            if buttons[click+1][4] != 1:
                if buttons[click][1] < (buttons[1][6]*buttons[1][7]-1) and buttons[click][3]< (buttons[1][7]-1):
                    buttons[click+1][0].config(state="disabled",relief=SUNKEN,bg='#f0f0ed')
                    if buttons[click+1][1] != 0:
                        buttons[click+1][4] = 1
                        buttons[click+1][5] = 2
                        buttons[click+1][0].config(text=str(buttons[click+1][1]))
                    if buttons[click+1][1] == 0:
                        buttons[click+1][4] = 1
                        check(click+1)
    if click/buttons[1][7] > 1:
        if buttons[click-buttons[1][7]][1] != "pomm":
            if buttons[click-buttons[1][7]][4] != 1:
                if buttons[click][3] > 0:
                    buttons[click-buttons[1][7]][0].config(state="disabled",relief=SUNKEN,bg='#f0f0ed')
                    if buttons[click-buttons[1][7]][1] != 0:
                        buttons[click-buttons[1][7]][4] = 1
                        buttons[click-buttons[1][7]][5] = 2
                        buttons[click-buttons[1][7]][0].config(text=str(buttons[click-buttons[1][7]][1]))
                    if buttons[click-buttons[1][7]][1] == 0:
                        buttons[click-buttons[1][7]][4] = 1
                        check(click-buttons[1][7])

    if click/(buttons[1][6]*buttons[1][7]-buttons[1][7]) < 1:
        if buttons[click+buttons[1][7]][1] != "pomm":
            if buttons[click+buttons[1][7]][4] != 1:
                if buttons[click+buttons[1][7]][3] < (buttons[1][6]*buttons[1][7]-1):
                    buttons[click+buttons[1][7]][0].config(state="disabled",relief=SUNKEN,bg='#f0f0ed')
                    if buttons[click+buttons[1][7]][1] != 0:
                        buttons[click+buttons[1][7]][4] = 1
                        buttons[click+buttons[1][7]][5] = 2
                        buttons[click+buttons[1][7]][0].config(text=str(buttons[click+buttons[1][7]][1]))
                    if buttons[click+buttons[1][7]][1] == 0:
                        buttons[click+buttons[1][7]][4] = 1
                        check(click+buttons[1][7])



def check_win(click):
    max = buttons[1][8]
    count = 0
    for x in range(buttons[1][6]*buttons[1][7]):
        if buttons[x][1] == "pomm" and buttons[x][5] == 1:
            count += 1
    if max == count:
        messagebox.showinfo(title="You won", message="Tupli pois! Leidsid kõik pommi.")
        raam.destroy()

#=======================================================================================

field = field_create(x,y,bomb_count)

raam = Tk()
raam.title("Minesweeper")

win_count = 0
n = 0
buttons = {}
for i in range(x):
    for j in range(y):
        buttons[n] = [Button(width = 2),field[i][j],i,j,0,0,x,y,bomb_count]
        buttons[n][0].bind("<Button-1>",LeftClick_w(n))
        buttons[n][0].bind("<Button-3>",RightClick_w(n))
        n +=1
for each in buttons:
    buttons[each][0].grid(row=buttons[each][2],column=buttons[each][3])

raam.mainloop()
    
        