#!/usr/bin/python
import math

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def triangle(n):
	return n*(n+1)/2

def find_lowest(n):
	i=1
	while n > len(factors(triangle(i))):
		i+=1
	return i, triangle(i)

print find_lowest(500)