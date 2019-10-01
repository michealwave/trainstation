# Conditionals

age = input("What is your age? ") # prompt for age

# Check if the age is more than 17, so the person
# Can see R rated movies
age = int(age)
if age >= 17: #Everything in the if statement only runs if the condition is true
	print("You can see an R rated movie")

else:
	print("You can not see an R rated movie, too bad")

print("Have a nice day")
#You can check all these conditions
# >, <, >=, <=, == (== means equal to)

birthday = input("Is today your birthday? (yes or no) ")
if birthday == "yes":
	print("Happy birthday")

print("Have a nice day")

myNum = 7 
guess = input("Guess a number between 1 and 10 ")
guess = int(guess)
if guess == myNum:
	print("You guess correctly")
elif guess > myNum:
	print("Too high")
else:
	print("Too low")

print("Thanks for playing")