from random import random
#Random package importing the random function

print(random())
#random() gives a decimal number in the range 0<=x<1

for i in range(10):
    print(random())
#For i in range(t) runs the code indented below t times

for i in range(10):
    if random() < 0.5: #Setting a 50% probability of a binary outcome
        print("Heads")
    else:
        print("Tails")

#Now we're going to count how many times we get heads
heads = 0 #Set heads to zero to start
for i in range(10):
    if random() < 0.5:
        heads += 1 #Add 1 to the count
print(heads) #Give total heads count
if heads >= 7: #Checking if we have 7 OR more heads
    print("Yes")

#Now we want to check how many times we can get 7 or more heads with 10 flips so lets run the test 10 times
counter = 0 #This will track how many times we get 7 or more heads
Test = int(input("How many times do you wish to run the test?:")) #Adjusting how many times the test is ran
for j in range(Test):
    heads = 0 #Since heads is already used earlier in the code we need to re-establish that heads is zero in this case
    for i in range(10):
        if random() < 0.5:
            heads += 1
    if heads >= 7: #If successful
        counter += 1 #Add 1 to the counter total
print(counter) #Keeping this line to check the counter/Test in the line below calculation works   
print(f"The probability of getting 7 or more heads is {counter/Test}") #Probability of getting 7 or more heads
