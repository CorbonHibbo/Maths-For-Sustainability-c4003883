from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random

#0 is used for trees, 1 is for on fire, 9 is for burnt out

grid = []
for r in range(50):
    thisrow = []
    for c in range(70):
        thisrow.append(0)
    grid.append(thisrow)

grid[randint(15,35)][randint(15,55)] = 1 #Set a random cell in the middle to be on fire

for i in range(15,25):
    for j in range(i,30):
        for p in range(14,18):
            for q in range(p,22):
                for r in range(i,j):
                    for c in range(p,q):
                        grid[r][c] = 8 #Assign the basic lake

window = Tk() #Create window
window.geometry('1400x1000') #Window dimensions
window.title("Forest fire") #Window name
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
                colour = "green"
            canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)

    nextgrid = []
    
    for r in range(len(grid)):
        thisrow = []
        for c in range(len(grid[0])):
            thiscell = grid[r][c]
            if thiscell == 1:
                thiscell = 2
            elif thiscell == 2:
                thiscell = 3
            elif thiscell == 3:
                thiscell = 9
            #This statement creates the 3 different fire stages

            elif thiscell == 0 and r-1>=0 and c-1>=0 and r+1<50 and c+1<70:
                if grid[r-1][c] == 1 or grid[r-1][c] == 2:
                    if random()<0.3: #Controls probability of catching fire
                        thiscell = 1 # caught fire
                if grid[r][c-1] == 1 or grid[r][c-1] == 2:
                    if random()<0.3:
                        thiscell = 1
                if grid[r][c+1] == 1 or grid[r][c+1] == 2:
                    if random()<0.3:
                        thiscell = 1
                if grid[r+1][c] == 1 or grid[r+1][c] == 2:
                    if random()<0.3:
                        thiscell = 1
                #Part above is fire spreading
                        
                if grid[r-1][c] == 8:
                    if random()<0.01: #Controls probability of lake growing
                        thiscell = 8 #Lake expanded
                if grid[r][c-1] == 8:
                    if random()<0.01:
                        thiscell = 8
                if grid[r][c+1] == 8:
                    if random()<0.01:
                        thiscell = 8
                if grid[r+1][c] == 8:
                    if random()<0.01:
                        thiscell = 8
                #Part above is lake growing
                        
            thisrow.append(thiscell)
        nextgrid.append(thisrow)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = nextgrid[r][c]
      
    window.update()
    sleep(0.01)

window.mainloop()
