# caves.py
# Julius Sytstra, Lars Bäcker, Guido Cnossen

from random import *
from randomspawn import *

# generate a Class that makes a layout representing the caves

class Caves():
	def __init__(self, randomspawnposition, randomspawnposition_wumpus):
		self.caveslist = []
		self.caves()
		self.elements()
		self.randomspawnposition = randomspawnposition
		self.randomspawnposition_wumpus = randomspawnposition_wumpus
		
	# returns a cave layout with 20 random chambers 
	def caves(self): 
		self.caves = []
		for x in range(1,6):
			for y in range(1,5): 
				self.caveslist.append([(x,y), None])
		
		return self.caves
	
	# assigns elements gold, bats and pits to random locations inside the cave
	def elements(self):
		for cave in self.caves:
			if cave[0] != self.randomspawnposition:
				element = randrange(0,3)
				if randrange(0,8) == 0:
					if element == 0:
						cave[1] = "Gold"
					if element == 1:
						cave[1] = "Bat"
					if element == 2: 
						cave[1] = "Pit"
		
		return self.caves
		
	def returncaves(self):
		return self.caves 
		
		
