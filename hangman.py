import time
myword = "shrimp"
mylist = list(myword)
guesslist = []
miss = []
failed = 0
framelist = ['''
 +---+
     |
     |
     |
    ===''',
'''
 +---+
 0   |
     |
     |
    ===''',
'''
 +---+
 0   |
 |   |
     |
    ===''',
'''
 +---+
 0   |
 |\  |
     |
    ===''',
'''
 +---+
 0   |
/|\  |
     |
    ===''',
'''
 +---+
 0   |
/|\  |
/    |
    ===''',
'''
 +---+
 0   |
/|\  |
/ \  |
    ===''']
for letter in mylist:
	guesslist.append("_") 
print(guesslist)

for letter2 in miss:
	guesslist.append("_")
print(miss)
print(framelist[0])
while True:
	letter = input("Enter a letter: ")
	print("You have 30 seconds to choose a letter")

	
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
		miss.append(letter)
		failed = failed + 1

	if failed < 1:
		print(framelist[0])
	else:
		print(framelist[len(miss)])
	print(guesslist)	
	print(miss)
	if failed == 6:
		print("GAME OVER")
		break
	if guesslist == mylist:
		print("You Win!")
		break


		

	

