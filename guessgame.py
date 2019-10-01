import random

mystnum = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Pick a number between 1 and 100 "))
	score = score + 1

	if guess == mystnum:
		print("Good Guess")
		break
	elif guess > mystnum:
		print("Too high, Try again")
	else:
		print("Too low, Try again")
	
print("It took you " + str(score) + " guesses")