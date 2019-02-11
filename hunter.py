# hunter.py 
# Julius Sytstra, Lars Bäcker, Guido Cnossen

from caves import *
from randomspawn import *
from wumpus import *

# generate a Hunter by defining the Class Hunter
class Hunter():
	def __init__(self, name):
		self.name = name
		self.win = False
		self.lose = False
		self.place()
		self.arrows = 5
		self.gold = 0
	
	# place the hunter randomly in one of the chambers in the cave
	def place(self):
		self.xcoord = randrange(1,6)
		self.ycoord = randrange(1,5)
		self.updateposition()
	
	# replace the hunter if he spawns on the wumpus' location
	def replace(self, wumpusposition):
		self.xcoord = randrange(1,6)
		self.ycoord = randrange(1,5)
		if (self.xcoord, self.ycoord) == wumpusposition:
			self.replace()
		else:
			self.updateposition()
	
	# replace the hunter if he comes across bats
	def bat_replace(self, wumpusposition):
		self.xcoord = randrange(1,6)
		self.ycoord = randrange(1,5)
		if (self.xcoord, self.ycoord) == wumpusposition:
			self.bat_replace()
		else:
			self.updateposition()
			
	def __str__(self):
		return "Hunter: {} Gold found: {} Arrows: {}".format(self.name,self.gold,self.arrows)
		
	# updates the position of the hunter		
	def updateposition(self):
		self.position = (self.xcoord,self.ycoord)
		return self.position
		
	def namereturn(self):
		return self.name
		
	def getpositionhunter(self):
		return self.position
	
	# defines when the hunter finds gold	
	def found_gold(self):
		self.gold = self.gold + 1
		return int(self.gold -1)
	
	# keeps track of the amount of gold that has been found by the hunter
	def gold_number(self):
		return int(self.gold -1)
	
	# keeps track of the number of arrows that the hunter uses	
	def arrow_number(self):
		return self.arrows
	
	# four functions that will keep the hunter inside the cave map 	
	def up(self):
		self.ycoord -= 1  
		if self.ycoord < 1:
			self.ycoord = 4
		self.updateposition()
	
	def down(self):
		self.ycoord += 1  
		if self.ycoord > 4:
			self.ycoord = 1
		self.updateposition()
		
	def right(self):
		self.xcoord += 1
		if self.xcoord > 5:
			self.xcoord = 1
		self.updateposition()

	def left(self):
		self.xcoord -= 1
		if self.xcoord < 1:
			self.xcoord = 5
		self.updateposition()
			

