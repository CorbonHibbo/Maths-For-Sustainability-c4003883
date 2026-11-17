from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random

grid = []
for r in range(35):
    thisrow = []
    for c in range(63):
        thisrow.append(0)
    grid.append(thisrow)

window = Tk() #Create window
window.geometry('1200x800') #Window dimensions
window.title("Poaching") #Window name
canvas = Canvas(window, width=1200, height=750, bg='white') #Canvas in window dimensions
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
                colour = "gray"
            elif grid[r][c] == 1:
                colour = "red"
            elif grid[r][c] == 2:
                colour = "orange"
            elif grid[r][c] == 3:
                colour = "yellow"
            elif grid[r][c] == 8:
                colour = "blue"
            else: 
                colour = "olive"
            canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)

    nextgrid = []
                        
    thisrow.append(thiscell)
    nextgrid.append(thisrow)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = nextgrid[r][c]
      
    window.update()
    sleep(0.05)

window.mainloop()
