from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random

grid = []
for r in range(50):
    thisrow = []
    for c in range(70):
        thisrow.append(0)
    grid.append(thisrow)

for E in range(0,1):
    a = randint(15,30)
    b = randint(15,55)
    while grid[a][b] == 9:
        a = randint(15,30)
        b = randint(15,55)

    grid[a][b] = 9

window = Tk() #Create window
window.geometry('1200x800') #Window dimensions
window.title("Poaching") #Window name
canvas = Canvas(window, width=1400, height=1000, bg='white') #Canvas in window dimensions
canvas.pack(anchor=CENTER, expand=True)

def handler():
    global run
    run = False
    window.destroy()
window.protocol("WM_DELETE_WINDOW", handler)

run = True

while run:
    canvas.delete("all") #Reset grid for next iteration

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 9:
                colour = "gray" #Elephant
            elif grid[r][c] == 1:
                colour = "red" #Poacher
            else: 
                colour = "green" #Grass
            canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)

    nextgrid = []

    for r in range(len(grid)):
        thisrow = []
        for c in range(len(grid[0])):
            thiscell = grid[r][c]
            if thiscell == 0 and r-1>=0 and c-1>=0 and r+1<50 and c+1<70:
                if grid[r-1][c] == 9:
                    if random()<0.1:
                        grid[r-1][c] = 0
                        thiscell = 9
                elif grid[r+1][c] == 9:
                    if random()<0.1:
                        grid[r+1][c] = 0
                        thiscell = 9
                elif grid[r][c-1] == 9:
                    if random()<0.1:
                        grid[r][c-1] = 0
                        thiscell = 9
                elif grid[r][c+1] == 9:
                    if random()<0.1:
                        grid[r][c+1] = 0
                        thiscell = 9
                            
            thisrow.append(thiscell)
        nextgrid.append(thisrow)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = nextgrid[r][c]
      
    window.update()
    sleep(0.5)

window.mainloop()
