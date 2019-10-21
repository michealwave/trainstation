myword = "shrimp"
#how to check if a letter is in a word
mylist = [" ", " ", " ", " ", " ", " "]
print(mylist)

letter = input("Enter a letter: ")
if letter in myword:
	if letter == "s":
		mylist.insert(0, "s")
	elif letter == "h":
		mylist.insert(1, "h")
	elif letter == "r":
		mylist.insert(2, "r")
	elif letter == "i":
		mylist.insert(3, "i")
	elif letter == "m":
		mylist.insert(4, "m")
	elif letter == "p"
	mylist.insert(5, "p")
else:
	print("nah")

count = 0
for letter2 in mylist:
	if letter2 == letter:
		print(count)
	count += 1
print(mylist)