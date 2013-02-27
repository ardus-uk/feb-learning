#!/usr/bin/python
userName=raw_input("What is your name?  ")
print "Welcome to the program,", userName
goAgain = 1
while goAgain == 1:
	squareNumber = int(raw_input("Type the number to square: "))
	print squareNumber, "square is ", squareNumber * squareNumber
	goAgain = int(raw_input("Type 1 to enter more numbers, or any other number to quit: "))

