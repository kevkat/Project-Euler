#!/usr/bin/python
import math

def get_divs(n):
    return all( n % x == 0 for x in range(1,21) )

x = 0
while True:
	x += 20
	if get_divs(2520+x) == True:
		print 2520+x
		break