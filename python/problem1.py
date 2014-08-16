#!/usr/bin/python
x = 1000
sum = 0
while  x:
		x -= 1
		if x % 3 == 0 or x % 5 == 0:
			sum += x
print sum,