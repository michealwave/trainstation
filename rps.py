#Michael Williams Period 1 9/30/19
#Rock paper scissors Game
# break into pieces
# Welcome page, with name entry
# Prints score screen with computer, player and ties
# options for game r, p ,s and q
# game will loop until q is entered
# each loop it will get a random choice from the computer
# a choice from the player, compare the two and update the score
# When the game is over(q is entered) final score is displayed

#welcome page
#prompt for the players name
#a welcome message

#-----------------------------------------

#imports
import random 
#variables
playerScore = 0
compScore = 0
ties = 0
#make a list
cChoices = ["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name ")
# main loop
while True:
	#print score
	print("Score:")
	print("Computer:  " + str(compScore))
	print(name + ": " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' for quit: ")
	computerChoice = random.choice(cChoices)
	if choice == "q":
		break

	if choice == "r":
		print(name + " Picked Rock")
		if computerChoice == "r": #tie
			print("Computer picked Rock")
			print("This is a tie!")
			ties = ties + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rock!")
			compScore += 1
		else: #s is only choice left
			print("Computer picked scissors")
			print("Rock beats Scissors!")
			playerScore += 1
	elif choice == "p":
		print(name + " Picked Paper")
		if computerChoice == "p":
			print("Computer picked Paper")
			print("It's a tie!")
			ties += 1 
		elif computerChoice == "r":
			print("Computer picked Rock")
			print("Paper beats Rock!")
			playerScore += 1
		else:
			print("Computer picked Scissors")
			print("Scissors beat paper!")
			compScore += 1
	elif choice == "s":
		print(name + "Picked Scissors")
		if computerChoice == "s":
			print("Computer picked Scissors")
			print("It's a tie!")
			ties = ties + 1
		elif computerChoice == "r":
			print("Computer picked Rock")
			print("Rock beats Scissors!")
			compScore =+ 1
		else:
			print("Computer picked Paper")
			print("Scissors beat Paper!")
			playerScore += 1
	else: #print type something else
		print("Invalid Input, try again monkey")