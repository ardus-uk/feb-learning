#!/usr/bin/python
# Finds real solutions to quadratic equation ax^2 + bx + c = 0, if they exist.
import math
a = float(raw_input("Value of a: "))
if a<> 0:
	b = float(raw_input("Value of b: "))
	c = float(raw_input("Value of c: "))
	d = b*b-4*a*c
	if d >=0:
		if d ==0:
			print "There is a single (repeated) solution, namely, ",    (-1*b)/(2*a)
		else:
			print "The two solutions are",  (-1*b + math.sqrt(d))/(2*a), " and " , (-1*b - math.sqrt(d))/(2*a)
	else:
		print "no real solutions to this equation!"
else:
	print "This is not a quadratic equation!"

