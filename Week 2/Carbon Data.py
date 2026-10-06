import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
#Adding essential packages for the work being done in the program
filename = "Carbon_Intensity_Data.csv"
#Create variable for the data set
data = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
#np.genfromtxt is used to 'translate' and read the data
fields = np.genfromtxt(filename, delimiter=',', dtype=str, max_rows=1)
print(fields)
#Finding and printing our headings within the data set
dates = []
actual_carbon = []
#Lists to store data
for row in data:
    dates.append(datetime.strptime(row[0], '%Y-%m-%dT%H:%MZ'))
    actual_carbon.append(int(row[1]))
#Taking all data from column 0 and putting it into dates
    #datetime converts the variables into a format matplotlib can understand
#Taking all data from column 1 and putting it into actual_carbon
plt.plot(dates, actual_carbon)
plt.show()
#Showing the graph
plt.xlabel('Date/time')
plt.ylabel('Actual Carbon')
#Label the x and y axis
plt.title('Carbon Intensity Data')
#Title for the graph
plt.xticks(rotation=45)
plt.tight_layout()
#rotating the dates along the bottom for better legability
plt.plot(dates, actual_carbon)
plt.show()
#Show new graph with the adjustments made
