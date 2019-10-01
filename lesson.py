# Calculation, printing, variables

# Printing to the screen
# The built in function print(), prints to the screen
# it will print both Strings and numbers
print("Printing to the screen")
print("Bruh") # in quotes are called strings
print('bruhg')
print(6) #a number
print("6")
print(6 + 6) #prints 12
print("6" + "6") #string concationation; mashes 2 strings together
#print("6" + 6)# error

# Performing calculations
# addition +
# subtraction - 
# multiplication *
# division /
# exponents **
# modulo %

print(4 - 2) #subtraction
print(4 * 2) #multiplication
print(4 / 3) # division
print(4 ** 3) #exponent
print("Modulo test")
print(5 % 3)
print(10 % 2)
print(16 % 3)
# Module gives remainders.
# python operators follow the same order of operations as math
print(4 - 2 * 2) # will give zero
print((4 - 2) * 2) #will give 4

#Variables

#variables are used to hold data
# variables are declared and set to a value (initializing)

badluck = 13 #delcared a variables called badluck and initialized it to 13
# i can print the variable using its name
print("badluck = " + str(badluck)) #cast it to a string
# lets do another one

goodluck = "4" #string variables
print("goodluck = " + goodluck) #don't have to cast because it is already a string
badluck + 5 #pointless
print(badluck)
badluck = badluck + 5 #badluck is now 18
print(badluck)

#you can also save input into variables
# using input(), a prompt goes into the ()
name = input("What is your name?")
print("Hello " + name)
print(name * 10)
name = name + "\n" #escape character (newline)
print(name * 10)
# lets try some math

base = input("Enter the base number: ")
exponent = input("Enter the exponent: ")
print(int(base) ** int(exponent))