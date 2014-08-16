#!/usr/bin/python
import math

def is_palindrome(number):
	if str(number)[0:len(str(number))/2] == str(number)[::-1][0:len(str(number))/2]:
		return True
	else:
		return False

def find_palindromes(rangemin,rangemax):
	palindromes = {}
	for x in range(rangemin,rangemax):
		for y in range(rangemin,rangemax):
			if is_palindrome(x*y):
				palindromes[x*y] = (x,y)
	return palindromes

palindromes = find_palindromes(100,1000)
for item in sorted(palindromes):
	print palindromes[item],item