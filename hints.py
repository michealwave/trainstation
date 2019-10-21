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
