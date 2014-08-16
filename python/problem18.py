#!/usr/bin/python

text_triangle = """3
7 4
2 4 6
8 5 9 3"""

parsed_tri = text_triangle.split('\n')
tri_length = len(parsed_tri)

def tri(n):
	return n*(n+1)/2

def find_max_tri(triangle):
	parsed_tri = triangle.split()
	return parsed_tri

def triangle_line(n):
	return parsed_tri[n].split()

print [triangle_line(i) for i in range(len(parsed_tri))]
print [triangle_line(i) for i in range(len(parsed_tri))][len([triangle_line(i) for i in range(len(parsed_tri))])-2]
print [triangle_line(i) for i in range(len(parsed_tri))][len([triangle_line(i) for i in range(len(parsed_tri))])-1]