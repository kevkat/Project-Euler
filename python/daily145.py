#!/usr/bin/python

class tree():
	def __init__(self, size, trunk, branch):
		self.size = size
		self.trunk = trunk
		self.branch = branch
	def drawtree(self):
		for i in range(int(self.size/2) + 1):
		    print('   ' + (int(self.size/2) - i)*' ' + str((2*i + 1)*self.branch))
		print('   ' + (int(self.size/2) - 1)*' ' + str(3*self.trunk))

smalltree = tree(3,'#','+')
smalltree.drawtree()

bigtree = tree(21,'%','&')
bigtree.drawtree()