#wumpus.py 
# Julius Sytstra, Lars Bäcker, Guido Cnossen

from caves import *
from randomspawn import *
from random import *

# Generate the wumpus by the Wumpus Class
class Wumpus():
	
	# take the position of the hunter into account
	def __init__(self, location_hunter):
		self.xposhunter = location_hunter[0]
		self.yposhunter = location_hunter[1]
		self.randomspawn_wumpus()
		
	# define the position of the Wumpus
	def getpositionwumpus(self):
		return self.xpos, self.ypos
	
	# spawn the Wumpus randomly	
	def randomspawn_wumpus(self):
		self.xpos = randrange(1,6)
		self.ypos = randrange(1,5)
		spawn_position_wumpus = (self.xpos, self.ypos)
		
		while abs(self.xpos - self.xposhunter) <2:
			self.xpos= randrange(1,6)
		while abs(self.ypos - self.yposhunter) <2:     
			self.ypos=randrange(1,5)
		
		self.updateposition()
	
	# updates the position of the Wumpus	
	def updateposition(self):
		self.wumpusposition = (self.xpos,self.ypos)
		return self.wumpusposition

	def returnwumpus(self):
		return [self.xpos,self.ypos]
