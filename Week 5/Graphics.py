from tkinter import * 
from tkinter.ttk import * #Graphics packages
from time import sleep #For animations the sleep function delays each iterations by a set amount of time

window = Tk() #This will hold all our drawings
window.geometry('900x7000')

canvas = Canvas(window, width=700, height=500, bg='white') #Defining area of which the drawing will appear
canvas.pack(anchor=CENTER, expand=True)

canvas.create_rectangle((650,450), (750,550), fill="blue") #Create a rectangle by defining co-ordinates of opposing corners and colour

x = 0 #Define start position variable
y = 0
run = True
while run:
    canvas.delete("all") #Remove previous square
    rect_id = canvas.create_rectangle((x,y), (x+100,y+100), fill="blue") #Constantly update square position

    x += 1.5 #Move 1.5 along
    y += 1
    if x>600: #When leaving canvas
        run = False #Stop updating postion
    elif y>400:
        run = False

    window.update()
    sleep(0.01) #Make each iteration wait inputed seconds
    #position = canvas.coords(rect_id) #Identify the corner co-ordinates of the square
    #print(f"Rectangle position: {position}") #Report corner co-ordinates

window.mainloop()
