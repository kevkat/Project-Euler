#!/usr/bin/python
import sys
import math

def is_prime(num):
	for j in range(2,int(math.sqrt(num)+1)):
		if (num % j) == 0:
			return False
	return True

def main(argv):

	if (len(sys.argv) != 3):
		sys.exit('Usage: prime_numbers3.py <lowest_bound> <upper_bound>')

	low = int(sys.argv[1])
	high = int(sys.argv[2])

	if (low % 2 == 0):
		low += 1

	primes = [2]
	for i in range(low,high,2):
		if is_prime(i):
			primes.append(i)
	print primes
	print "Sum of the primes less than", int(sys.argv[2]), "is", sum(primes)

if __name__ == "__main__":
	main(sys.argv[1:])