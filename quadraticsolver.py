#!/usr/bin/python
# solves quadratic equation
import math
a = float(raw_input("Value of a: "))
if a<> 0:
	b = float(raw_input("Value of b: "))
	c = float(raw_input("Value of c: "))
	d = b*b-4*a*c
	if d >=0:
		if d ==0:
			print "There is only one solution, namely, ",    (-1*b)/(2*a)
		else:
			print "The two solutions are",  (-1*b + math.sqrt(d))/(2*a), " and " , (-1*b - math.sqrt(d))/(2*a)
	else:
		print "no real solutions to this equation!"
else:
	print "This is not a quadratic equation!"

