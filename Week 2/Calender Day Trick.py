print("Please think of a date")
day = int(input("Please enter the day of the month (1, 2, 3, etc.): "))
month = int(input("Please enter the month (1=Jan, 2=Feb, etc.): "))
fullyear = input("Please enter the year (2025, etc.): ")
#This forces the user to directly import the date for which the program runs for the day of the week
century = int(fullyear[0:2])
year = int(fullyear[2:])
#These new lines break down the full year inputted into the century chosen and the year within said century
print(f"day: {day}, month: {month}, century: {century}, year: {year}")
#F-printing all information inputted
D = day
rem = century % 4 #Dividing by 4
C = (3 - rem) * 2
#Determining century number
rem = year % 12
twelves = int(year/12)
fours = int(rem/4)
Y = twelves + rem + fours
#Determing year number
month_numbers = []
thismonth = 0
for n in range(1,13):
    month_numbers.append(thismonth)

    if n in (1,3,5,7,8,10,12): # Jan, Mar, May, Jul, Aug, Oct, Dec
        thismonth += 31
    elif n in (4,6,9,11): # Apr, Jun, Sep, Nov
        thismonth += 30
    else: # Feb
        thismonth += 28

    thismonth = thismonth % 7
M = month_numbers[month-1]
#Determing month number
print(C,Y,M,D)
W = (C + Y + M + D) % 7
#Calculating day of the week
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(weekdays[W])
