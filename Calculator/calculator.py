from replit import clear
from art import logo


def add(n1, n2):
	return n1 + n2


def subtract(n1, n2):
	return n1 - n2


def multiply(n1, n2):
	return n1 * n2


def divide(n1, n2):
	return n1 / n2


operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}


def calculator():
	""" here we are taking n1 and n2 values and evaluating and print the answer"""
	print(calculator.__doc__)
	print(logo)

	n1 = float(input("What's the first number?: "))
	for symbol in operations:
		print(symbol)
	should_continue = True

	while should_continue:
		operation_symbol = input("Pick an operation: ")
		n2 = float(input("What's the next number?: "))
		calculation_function = operations[operation_symbol]
		answer = calculation_function(n1, n2)
		print(f"{n1} {operation_symbol} {n2} = {answer}")

		if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
			n1 = answer
		else:
			should_continue = False
			clear()
			calculator()


calculator()
