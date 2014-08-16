#!/usr/bin/python
import math

# sum of the squares of the first n natural numbers
def sum_of_squares(n):
	return sum([x*x for x in n])

# square of the sum of the first n natural numbers
def square_of_sums(n):
	return sum(n)**2

print square_of_sums(range(1,101)) - sum_of_squares(range(1,101))