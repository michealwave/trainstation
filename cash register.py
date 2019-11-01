#Michael Williams	
#October 31 2019
#Period 1

change = 0
dollars = 0
halfdollar = 0
quarter = 0
dime = 0
nickels = 0
pennies = 0
price = 0
given = 0

price = float(input("What is the price of the item? "))
given = float(input("How much are you paying with? "))

change = given - price
change = change * 100

dollars = int(change / 100)
change = change % 100

halfdollar = int(change / 50)
change = change % 50

quarter = int(change / 25)
change = change % 25

dime = int(change / 10)
change = change % 10

nickels = int(change / 5)
change = change % 5

pennies = change
change = given - price

print("Change: " + str(change))
print("Dollars: " + str(dollars))
print("Half Dollars: " + str(halfdollar))
print("Quarters: " + str(quarter))
print("Dimes: " + str(dime))
print("Nickels: " + str(nickels))
print("Pennies: " + str(pennies))