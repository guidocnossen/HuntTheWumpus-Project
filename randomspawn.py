#randomspawn.py
# Julius Sytstra, Lars Bäcker, Guido Cnossen

from random import * 

# generate a random spawn for the hunter 

def randomspawn():
	x_pos_hunter = randrange(1,6)
	y_pos_hunter = randrange(1,5)
	
	randomspawnposition = (x_pos_hunter, y_pos_hunter)
	
	return randomspawnposition, randomspawnposition_wumpus
	
	
