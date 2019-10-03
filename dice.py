# Michael Williams
# Period 1
# 10/3/19
import random
space = " "
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
rollNum = 1
rolls = int(input("How many rolls would you like? "))

while rollNum <= rolls:
  randnum = random.randint(1, 6)
  print("Roll #" + str(rollNum) + ":" + str(randnum))
  rollNum = rollNum + 1

  if randnum == 1:
    one = one + 1
  
  elif randnum == 2:
    two = two + 1

  elif randnum == 3:
    three = three + 1

  elif randnum == 4:
    four = four + 1

  elif randnum == 5:
    five = five + 1

  elif randnum == 6:
    six = six + 1

print("Total Rolls: " + str(rolls))
print("1s: " + str(one))
print("2s: " + str(two))
print("3s: " + str(three))
print("4s: " + str(four))
print("5s: " + str(five))
print("6s: " + str(six))

total = one + two + three + four + five + six

one = one / total * 100.0
two = two / total * 100.0
three = three / total * 100.0
four = four / total * 100.0
five = five / total * 100.0
six = six / total * 100.0

print(space)
print("1s: " + str(one) + "%")
print("2s: " + str(two) + "%")
print("3s: " + str(three) + "%")
print("4s: " + str(four) + "%")
print("5s: " + str(five) + "%")
print("6s: " + str(six) + "%")
