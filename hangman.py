myword = "shrimp"
#how to check if a letter is in a word
mylist = list(myword)
guesslist = []
turns = 10
miss = []

for letter in mylist:
	guesslist.append("_") 
print(guesslist)

for letter2 in miss:
	guesslist.append("_")
print(miss)
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
		miss.append(letter)
	print(guesslist)	
	print(miss)

