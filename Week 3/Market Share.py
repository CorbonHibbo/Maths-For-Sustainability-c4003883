from random import random
#Put the buyers info onto the graph
import matplotlib.pyplot as plt

#Lists to track time and the car owners
times = []
V_owners = []
H_owners = []

counter = 0
Test = int(input("How many times shall we run the test?:"))
Ratio = int(input("How many people are we using to create the ratio?:"))
for j in range(Test):
    Vauxhall = 0
    Hyundai = 0
    for i in range(Ratio): #5 people choosing cars
        if random()<0.5: #Equal split choice
            Vauxhall += 1
        else:
            Hyundai += 1
        times.append(i)
        V_owners.append(Vauxhall)
        H_owners.append(Hyundai)
    #See results
    print(Vauxhall, Hyundai)

    #Code above sets the ratio of buyers and therefore influences the probability
    for i in range(1000-Ratio): #Total the buyers to 1000
        if random()<Vauxhall/(Vauxhall+Hyundai): #Probability of buying a Vauxhall
            Vauxhall += 1
        else:
            Hyundai += 1
        times.append(i)
        V_owners.append(Vauxhall)
        H_owners.append(Hyundai)
    if Vauxhall > Hyundai:
        counter += 1
    print(Vauxhall, Hyundai)
    
print(f"Vauxhall won {counter} times out of the {Test} times the test was ran")

#Creating the graph
plt.plot(times,V_owners)
plt.plot(times,H_owners)
plt.xlabel('Time')
plt.ylabel('No. owners')
plt.legend(['Vauxhall', 'Hyundai'])
plt.show()
