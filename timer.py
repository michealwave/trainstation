import time
import os

# Variables
hours = 0
minutes = 0
seconds = 0

# Input
print("Enter the number of hours, minutes and seconds for the timer")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

# convert to seconds
minutes += hours * 60
seconds += minutes * 60

# set hours and minutes to 0
minutes = 0
hours = 0

# start countdown loop
while seconds >= 0:
	#convert back to hours, minutes and seconds to print time
	minutes = int(seconds / 60)
	seconds = seconds % 60

	hours = int(minutes / 60)
	minutes = minutes % 60

	#print time
	print(str(hours) + ":" + str(minutes) + ":" + str(seconds))

	#convert back to seconds
	# convert to seconds
	minutes += hours * 60
	seconds += minutes * 60

	# set hours and minutes to 0
	minutes = 0
	hours = 0

	# pause for 1 seconds
	time.sleep(1)
	#clear the screen
	os.system("cls")
	#subtract 1 seconds, loop back
	seconds -= 1