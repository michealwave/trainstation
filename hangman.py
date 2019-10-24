import time
import os
myword = "shrimp"
#how to check if a letter is in a word
mylist = list(myword)
guesslist = []
turns = 10
miss = []
failed = 0
frame1 = '''
 +---+
     |
     |
     |
    ==='''
frame2 = '''
 +---+
 0   |
     |
     |
    ==='''
frame3 = '''
 +---+
 0   |
 |   |
     |
    ==='''
frame4 = '''
 +---+
 0   |
 |\  |
     |
    ==='''
frame5 = '''
 +---+
 0   |
/|\  |
     |
    ==='''
frame6 = '''
 +---+
 0   |
/|\  |
/    |
    ==='''
frame7 = '''
 +---+
 0   |
/|\  |
/ \  |
    ==='''
for letter in mylist:
	guesslist.append("_") 
print(guesslist)

for letter2 in miss:
	guesslist.append("_")
print(miss)
print(frame1)
while True:
	letter = input("Enter a letter: ")
	if letter == "s":
		guesslist[0] = "s"
		
	elif letter == "h":
		guesslist[1] = "h"
		
	elif letter == "r":
		guesslist[2] = "r"
		
	elif letter == "i":
		guesslist[3] = "i"
		
	elif letter == "m":
		guesslist[4] = "m"
		
	elif letter == "p":
		guesslist[5] = "p"
	else:
		frame1 = frame2
		miss.append(letter)
		failed = failed + 1
        
	print(guesslist)	
	print(miss)
	print(frame1)
	if failed == 6:
		print("GAME OVER")
		break
	if guesslist == mylist:
		print("You Win!")
		break
		

	

