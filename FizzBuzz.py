start = int (input ("Enter The Start Interval Number : "))
stop = int (input ("Enter The Stop Interval Number : "))


def fizzBuzz (a, b):
	for number in range (a, b):
		if number % 3 == 0 and number % 5 == 0:
			print ("FizzBuzz")
		elif number % 3 == 0:
			print ("Fizz")
		elif number % 5 == 0:
			print ("Buzz")
		else:
			print (number)


fizzBuzz (start, stop)
