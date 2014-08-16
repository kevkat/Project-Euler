#!/usr/bin/python
lim=4000000
current=1
last=2
total_evens=0
	
while (current<lim):
	print current
	if current%2==0:
		total_evens=total_evens+current
	last=current+last
	current=last-current
	
print "Sum:",total_evens