from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random
#import matplotlib.pyplot as plt

runs = 1
results = []

for run_time in range(runs):

    grid = []
    for r in range(48):
        thisrow = []
        for c in range(85):
            thisrow.append(0)
        grid.append(thisrow)
    
    for E in range(0,100):
        a = randint(5,43)
        b = randint(5,80)
        while grid[a][b] == 9:
            a = randint(5,43)
            b = randint(5,80)
        grid[a][b] = 9 #Assign elephant to cell
    
    for Po in range(0,10):
        c = randint(5,43)
        d = randint(5,80)
        while grid[c][d] == 9 or grid[c][d] == 1: #If cell is currently already 9 or 1 then rerun
            c = randint(5,43)
            d = randint(5,80)
        grid[c][d] = 1 #Assign poacher to cell
    
    for Pr in range(0,5):
        e = randint(5,43)
        f = randint(5,80)
        while grid[e][f] == 9 or grid[e][f] == 1 or grid[e][f] == 6:
            e = randint(5,43)
            f = randint(5,80)
        grid[e][f] = 6
        
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
    
    ITER = 0 #Variable to track iterations
    Elephant = []
    
    Count = []
    
    while run:
    
        ITER += 1 #New iteration so add to total
    
        ELEPH = 0 # Set elephant count to zero at start of every iteration
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 9: #If a cell has an elephant
                    ELEPH += 1 #Add to count
    
        POACH = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    POACH += 1
    
        if ELEPH == 0:
            results.append(ELEPH)
            print(f"All elephants have been poached after {ITER} iterations.")
            run = False
            break
    
        if POACH == 0:
            results.append(ELEPH)
            print(f"All poachers have been eliminated after {ITER} iterations with {ELEPH} elephants alive")
            run = False
            break
    
        if ITER %20 == 0: #If Iteration count is divisable by 10
            print(f"Iteration: {ITER}. {ELEPH} elephants currently living.")
        
        canvas.delete("all") #Reset grid for next iteration
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 9:
                    colour = "gray" #Elephant
                elif grid[r][c] == 1:
                    colour = "red" #Poacher
                elif grid[r][c] == 6:
                    colour = "blue" #Protector
                else: 
                    colour = "green" #Grass
                canvas.create_rectangle((15*c,15*r), (15*(c+1), 15*(r+1)), fill=colour)
    
        # Start with a copy of the current grid
        nextgrid = []
    
        for r in range(len(grid)):
            nextgrid.append(grid[r][:])
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
    
    #PROTECTOR MOVEMENT
    
                if ITER %2 == 1: #Humans move almost twice as slow so move every other iteration
                    if grid[r][c] == 6 and nextgrid[r][c] == 6:
                        closest_dist = 999999 #Set an extremly large distance so poacher will always go towards closest elephant
                        target_r = r
                        target_c = c #New variables store location of nearest elephant
    
                        for er in range(len(grid)):
                            for ec in range(len(grid[0])):
                                if grid[er][ec] == 1: #Check if current cell is poacher
                                    dist = abs(er-r) + abs(ec-c) #Calculate distance from poacher to protector
                                    if dist < closest_dist: #Check if truly closest
                                        closest_dist = dist #Confirm closest
                                        target_r = er
                                        target_c = ec
    
                        nr, nc = r, c #Protector next movement
                        if target_r > r:
                            nr += 1
                        elif target_r < r:
                            nr -= 1
                        elif target_c > c:
                            nc += 1
                        elif target_c < c:
                            nc -= 1
                        if grid[nr][nc] == 0 and nextgrid[nr][nc] == 0:
                            nextgrid[r][c] = 0
                            nextgrid[nr][nc] = 6 #Move protector normally
                        elif nextgrid[nr][nc] == 1:
                            nextgrid[r][c] = 0
                            nextgrid[nr][nc] = 6
                        elif nextgrid[nr][nc] == 6:
                            pass 
                        for r in range(len(grid)):
                            for c in range(len(grid[0])):
                                if nextgrid[r][c] == 1:
                        
                                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        
                                        nr = r + dr
                                        nc = c + dc
                        
                                        if (
                                            0 <= nr < len(grid)
                                            and 0 <= nc < len(grid[0])
                                            and nextgrid[nr][nc] == 6
                                        ):
                                            nextgrid[r][c] = 0
                                            break           
    
    #POACHER MOVEMENT
    
                if ITER %2 == 0: #Humans move almost twice as slow so move every other iteration
                    if grid[r][c] == 1 and nextgrid[r][c] == 1 and nextgrid[r][c] != 6:
                        closest_dist = 999999 #Set an extremly large distance so poacher will always go towards closest elephant
                        target_r = r
                        target_c = c #New variables store location of nearest elephant
    
                        for er in range(len(grid)):
                            for ec in range(len(grid[0])):
                                if grid[er][ec] == 9: #Check if current cell is elephant
                                    dist = abs(er-r) + abs(ec-c) #Calculate distance from elephant to poacher
                                    if dist < closest_dist: #Check if truly closest
                                        closest_dist = dist #Confirm closest
                                        target_r = er
                                        target_c = ec
    
                        nr, nc = r, c #Poachers next movement
                        if target_r > r:
                            nr += 1
                        elif target_r < r:
                            nr -= 1
                        elif target_c > c:
                            nc += 1
                        elif target_c < c:
                            nc -= 1
                        if grid[nr][nc] == 0 and nextgrid[nr][nc] == 0:
                            nextgrid[r][c] = 0
                            nextgrid[nr][nc] = 1 #Move poacher normally
                        elif nextgrid[nr][nc] == 9:
                            nextgrid[r][c] = 0
                            nextgrid[nr][nc] = 1 #Elephant killed
                        elif nextgrid[nr][nc] == 6:
                            nextgrid[r][c] = 0 #Poacher moves onto protector so is removed
    
    #ELEPHANT MOVEMENT
                            
                if ITER %1 == 0:
                    if grid[r][c] == 9 and nextgrid[r][c] == 9: #Check if poacher has already killed it
    
                        if random() < 0.7: #Chance of moving in random direction
    
                            direction = randint(0, 3) #Randomise the direction
    
                            nr, nc = r, c #Create new variable for moving in a random direction
    
                            if direction == 0 and r > 0:
                                nr = r - 1          # up
                            elif direction == 1 and r < len(grid)-1:
                                nr = r + 1          # down
                            elif direction == 2 and c > 0:
                                nc = c - 1          # left
                            elif direction == 3 and c < len(grid[0])-1:
                                nc = c + 1          # right
    
                            if grid[nr][nc] == 0 and nextgrid[nr][nc] == 0: #If the next square selected is empty currently and in the next iteration
                                nextgrid[r][c] = 0 #In next iteration current square is empty
                                nextgrid[nr][nc] = 9 #In next iteration chosen square is an elephant
                            elif nextgrid[nr][nc] == 1: #If the next grid is a poacher then
                                nextgrid[r][c] = 0 #In next iteration current cell is empty
                                nextgrid[nr][nc] = 1 #In next iteration next cell is poacher
    
        grid = nextgrid
    
        Elephant.append(ELEPH)
          
        window.update()
        sleep(0.1)
     
Count.append(ITER)
    
window.destroy()
window.mainloop()

Elph_surv = []

Elph_surv.append(ELEPH)

print(results)

#NEW SECTION FOR PLOTTING THE ELEPHANTS OVER THE TIME SPAN

# plt.hist(results, bins=15, color='skyblue', edgecolor='black')
# plt.xlabel("Number of Elephants")
# plt.ylabel("Frequency")
# plt.title("Elephants survival")
# plt.show()

# import numpy as np
# from scipy import stats

# results = np.array(results) #Create an array based on the list

# print(f"Number of simulations: {len(results)}")
# print(f"Mean: {np.mean(results):.2f}")
# print(f"Median: {np.median(results):.2f}")
# print(f"Mode: {stats.mode(results)[0]:.2f}")
# print(f"Variance: {np.var(results):.2f}")
# print(f"Std deviation: {np.std(results):.2f}")
# print(f"Min: {min(results):.2f}")
# print(f"Max: {max(results):.2f}")
# print(f"IQ range: {stats.iqr(results):.2f}")

# hypothesized_mean = 46.07
# t_statistic, p_value = stats.ttest_1samp(results, hypothesized_mean)

# print("=" * 60)
# print("HYPOTHESIS TEST")
# print("=" * 60)
# print(f"H₀: μ = {hypothesized_mean}")
# print(f"Hₐ: μ ≠ {hypothesized_mean}")
# print("Significance level: α = 0.05")
# print()

# print(f"Test statistic (t): {t_statistic:.4f}")
# print(f"P-value: {p_value:.4f}")
# print(f"Degrees of freedom: {len(results) - 1}")

# #MONTE CARLO

# cumulative_mean = np.cumsum(results) / np.arange(1, len(results) + 1)

# plt.plot(cumulative_mean)
# plt.xlabel("Iteration")
# plt.ylabel("Cumulative mean")
# plt.title("Monte Carlo cumulative mean plot")
# plt.show()
