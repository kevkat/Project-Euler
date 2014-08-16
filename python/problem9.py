#!/usr/bin/python

def find_triplet(n):
	for a in range(1,n):
		for b in range(1,n-a):
			c = n-a-b
			if a**2+b**2 == c**2:
				return "Triplet:", a, b, c, "Product:", a*b*c
	return 0

print find_triplet(1000)