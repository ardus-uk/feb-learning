#!/usr/bin/python
# Find three consecutive integers such that the sum of their cubes is equal to a perfect square
import numbthy
import math
from types import *
# http://userpages.umbc.edu/~rcampbel/Computers/Python/numbthy.html

def isPerfectSquare(x):
	# determines whether x is a perfect square by examining its prime factors
	# The prime factors of a perfect square occur in pairs
	x_factors = numbthy.factors(x)
	non_paired_factors = [ ]
	for i in x_factors:
		if i in non_paired_factors:
			non_paired_factors.remove(i)
		else:
			non_paired_factors.append(i)
	if non_paired_factors:  # ie list is not empty, so not all factors of s are paired
		return False
	else:
		return True

n=0
no_of_solutions=2
a=1
while (n<no_of_solutions) :
	b=a+1
	c=b+1
	s = a*a*a+b*b*b+c*c*c
	if isPerfectSquare(s):  
		print a,"^3 + ",b,"^3 + ",c,"^3 = ",int(math.sqrt(s)),"^2"
		n+=1
	a+=1

		
	

	
