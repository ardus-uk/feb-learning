#!/usr/bin/python
# Find three consecutive integers such that the sum of their cubes is equal to a perfect square
import numbthy
import math
from types import *
# http://userpages.umbc.edu/~rcampbel/Computers/Python/numbthy.html
n=0
no_of_solutions=2
a=1
while (n<no_of_solutions) :
	b=a+1
	c=b+1
	s = a*a*a+b*b*b+c*c*c
	s_factors = numbthy.factors(s)
	non_paired_factors = [ ]
	for i in s_factors:
		if i in non_paired_factors:
			non_paired_factors.remove(i)
		else:
			non_paired_factors.append(i)
	if not non_paired_factors:  # ie list is empty, so all factors of s must be paired
		print a,"^3 + ",b,"^3 + ",c,"^3 = ",int(math.sqrt(s)),"^2"
		n+=1
	a+=1

		
	

	
