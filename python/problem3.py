#!/usr/bin/python
top = 600851475143
x = 2
while x<top:
		if top % x == 0:
			top = top/x
			print top
		else:
			x += 1
print top,