myword = "hello"

choice = input("Type a word")

if choice == myword:
	print("Yes")
else:("nah")



#how to check if a letter is in a word

letter = input("Enter a letter: ")

if letter in myword:
	print("letter yes")
else:
	print("nah")

count = 0
mylist = list(myword)
for letter2 in mylist:
	if letter2 == letter:
		print(count)
	count += 1


myString = "Arizona"
mysteryword = list(myString)
print(mysteryword)
guesslist = []
#How to make a list with _ for characters

for letter in mysteryword:
	guesslist.append("_")

print(guesslist)

#how to replace a specific index in a list
guesslist[3] = "z"
print(guesslist)
#--------------------------------------------------------------
if letter == "s":
		guesslist[0] = "s"
		print(guesslist)
	elif letter == "h":
		guesslist[1] = "h"
		print(guesslist)
	elif letter == "r":
		guesslist[2] = "r"
		print(guesslist)
	elif letter == "i":
		guesslist[3] = "i"
		print(guesslist)
	elif letter == "m"
	guesslist[4] = "m"
	print(guesslist)
	elif letter == "p"
	guesslist[4] = "p"
	print(guesslist)
#