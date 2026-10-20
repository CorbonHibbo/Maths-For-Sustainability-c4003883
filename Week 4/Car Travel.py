from random import randint #Random integer function

cars = [] #List to hold our cars

class Car: #This allows us to define every car and it's variables
    def __init__(self, colour):
        self.colour = colour
        self.location = 0
        self.destination = 0
        self.direction = ""
        self.direct()
        self.begin()
        self.end()
        self.join()

    def direct(self): #Define direction of an individual car
        if randint(0,3) < 2:
            self.direction = "north"
        else:
            self.direction = "south"

    def join(self): #Join adds the car information from the class into the list created earlier
        global cars #Because the list exists outside the class we use global to call it
        cars.append(self)

    def move(self):
        if self.direction == "north":
            self.location += 1
            if self.location >= self.destination:
                self.leave()

        elif self.direction == "south":
            self.location -= 1
            if self.location <= self.destination:
                self.leave()

    def begin(self):
        if self.direction == "north":
            self.location = randint(0, 10)
        else:
            self.location = randint(10, 20)

    def end(self):
        if self.direction == "north":
            self.destination = randint(10, 20)
        else:
            self.destination = randint(0, 10)

    def leave(self):
        global cars
        cars.remove(self) #Remove car from list

    def report(self):
        if self.location == self.destination:
            print(f"{self.colour} car has reached it's destination")
        else:
            print(f"{self.colour} car at {self.location}, heading for {self.destination} going {self.direction}.")

for colour in ["Blue", "Red", "Yellow", "Green","Silver", "Orange", "Purple"]:
    Car(colour) #Define colour, start distance, and destinantion distance of each car

while cars: #Keep looping till cars (List) is empty
    for car in cars[:]:
        car.move()
        car.report()
    road = len(cars)
    if road > 0:
        print(f"There are {road} cars on the road")
        print("PRESS ENTER FOR NEXT STEP")
    else:
        print("There are no longer cars on the road")
    input() #Press enter to rerun
