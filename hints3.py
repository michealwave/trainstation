mysteryword = "Halloween"
mysteryword = list(mysteryword)

guesslist = "_________"
guesslist = list(guesslist)

guess = input("Guess a letter")
if guess in mysteryword: 
	count = 0
	for letter in mysteryword:
		if letter == guess:
			guesslist[count] = guess

print(guesslist)

frame1 = '''
 +---+
     |
     |
     |
    ==='''
print(frame1)
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
# -------------------------------
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