for num in range(1, 101):
	if num % 5 == 0 and num % 3 == 0:
		print(str(num), end="")
		print(" Fizz Buzz")
	elif num % 3 == 0:
		print(str(num), end="")
		print(" Fizz")
	elif num % 5 == 0:
		print(str(num), end="")
		print(" Buzz")	
	else:
		print(num)
