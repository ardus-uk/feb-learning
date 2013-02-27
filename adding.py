#!/usr/bin/python
userName=raw_input("What is your name?  ")
print "Welcome to the program, ", userName
goAgain = 1
while goAgain == 1:
	firstNumber = int(raw_input("Type the first number: "))
	secondNumber = int(raw_input("Type the second number: "))
	print firstNumber, "added to ", secondNumber, " is ", firstNumber + secondNumber
	goAgain = int(raw_input("Type 1 to enter more numbers, or any other number to quit: "))

