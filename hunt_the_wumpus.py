# Julius Sytstra, Lars Bäcker, Guido Cnossen


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created: Mon May  4 15:15:56 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from hunter import *
from wumpus import * 
from caves import *
import sys
from time import *

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

# set up the user interface with background , labels, buttons
class Ui_Widget(QtGui.QWidget):
	
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
			    
	def setupUi(self, Widget):
		Widget.setObjectName(_fromUtf8("Hunt The Wumpus"))
		Widget.resize(908, 585)
		self.label = QtGui.QLabel(Widget)
		self.label.setGeometry(QtCore.QRect(20, 0, 871, 41))
		self.label.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));"))
		self.label.setText(_fromUtf8(""))
		self.label.setObjectName(_fromUtf8("label"))
		self.label_2 = QtGui.QLabel(Widget)
		self.label_2.setGeometry(QtCore.QRect(310, 0, 301, 41))
		self.label_2.setStyleSheet(_fromUtf8("font: 75 24pt \"Waree\";\n"
"color: rgb(0, 0, 0);"))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.graphicsView = QtGui.QGraphicsView(Widget)
		self.graphicsView.setGeometry(QtCore.QRect(160, 50, 600, 400))
		self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
		self.scene = QtGui.QGraphicsScene(Widget)
		self.graphicsView.setStyleSheet("border: 0px")
		self.rooms = QtGui.QGraphicsPixmapItem()
		self.rooms.setPixmap(QtGui.QPixmap("rooms.jpg"))
		self.scene.addItem(self.rooms)
		self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
		self.graphicsView.setScene(self.scene)
		self.frame = QtGui.QFrame(Widget)
		self.frame.setGeometry(QtCore.QRect(-1, 50, 161, 401))
		self.frame.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0) ;"))
		self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setObjectName(_fromUtf8("frame"))
		self.frame_2 = QtGui.QFrame(Widget)
		self.frame_2.setGeometry(QtCore.QRect(750, 50, 161, 401))
		self.frame_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0) ;"))
		self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
		self.frame_2.setObjectName(_fromUtf8("frame_2"))
		self.horizontalLayoutWidget = QtGui.QWidget(Widget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 520, 311, 51))
		self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_4.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 10pt \"Waree\";\n"
"color: rgb(0, 0, 0);"))
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.horizontalLayout.addWidget(self.pushButton_4)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_3.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 10pt \"Waree\";\n"
"color: rgb(0, 0, 0);"))
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.horizontalLayout.addWidget(self.pushButton_3)
		spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem1)
		self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_2.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 10pt \"Waree\";\n"
"color: rgb(0, 0, 0);"))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.horizontalLayout.addWidget(self.pushButton_2)
		self.verticalLayoutWidget = QtGui.QWidget(Widget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 470, 81, 55))
		self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
		self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setMargin(0)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 10pt \"Waree\";\n"
"color: rgb(0, 0, 0);"))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.verticalLayout.addWidget(self.pushButton)
		self.verticalLayoutWidget_2 = QtGui.QWidget(Widget)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(320, 470, 301, 101))
		self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_2)
		self.label_5.setStyleSheet(_fromUtf8("font: 75 10pt \"Waree\";"))
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.verticalLayout_2.addWidget(self.label_5)
		self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_2)
		self.label_6.setStyleSheet(_fromUtf8("font: 10pt \"Waree\";"))
		self.label_6.setObjectName(_fromUtf8("label_6"))
		self.verticalLayout_2.addWidget(self.label_6)
		self.verticalLayoutWidget_3 = QtGui.QWidget(Widget)
		self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(640, 460, 261, 121))
		self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
		self.verticalLayout_3.setMargin(0)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
		self.label_3.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 10pt \"Waree\";\n"
"color: rgb(0, 0, 0);"))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.verticalLayout_3.addWidget(self.label_3)
		self.lcdNumber = QtGui.QLCDNumber(self.verticalLayoutWidget_3)
		self.lcdNumber.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"))
		self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
		self.verticalLayout_3.addWidget(self.lcdNumber)
		self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_3)
		self.label_4.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 10pt \"Waree\";\n"
"color: rgb(0, 0, 0);"))
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.verticalLayout_3.addWidget(self.label_4)
		self.lcdNumber_2 = QtGui.QLCDNumber(self.verticalLayoutWidget_3)
		self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"))
		self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
		self.verticalLayout_3.addWidget(self.lcdNumber_2)
		self.pushButton_5 = QtGui.QPushButton(Widget)
		self.pushButton_5.setGeometry(QtCore.QRect(20, 460, 51, 27))
		self.pushButton_5.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 10pt \"Waree\";\n"
"color: rgb(0, 0, 0);"))
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.pushButton_6 = QtGui.QPushButton(Widget)
		self.pushButton_6.setGeometry(QtCore.QRect(250, 460, 51, 27))
		self.pushButton_6.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 10pt \"Waree\";\n"
"color: rgb(0, 0, 0);"))
		self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

		self.retranslateUi(Widget)
		QtCore.QMetaObject.connectSlotsByName(Widget)
	#set up labels and buttons
	def retranslateUi(self, Widget):
		Widget.setWindowTitle(_translate("Widget", "Hunt The Wumpus", None))
		self.label_2.setText(_translate("Widget", "Hunt The Wumpus", None))
		self.pushButton_4.setText(_translate("Widget", "Left", None))
		self.pushButton_3.setText(_translate("Widget", "Down", None))
		self.pushButton_2.setText(_translate("Widget", "Right", None))
		self.pushButton.setText(_translate("Widget", "Up", None))
		self.label_5.setText(_translate("Widget", "Welcome to Hunt the Wumpus!!!!", None))
		self.label_6.setText(_translate("Widget", "Made possible by Julius, Lars and Guido!", None))
		self.label_3.setText(_translate("Widget", "ARROWS", None))
		self.label_4.setText(_translate("Widget", "GOLD", None))
		self.pushButton_5.setText(_translate("Widget", "Move", None))
		self.pushButton_6.setText(_translate("Widget", "Shoot", None))


		# create the hunter
		self.hunter = Hunter("Brutal Killer")

		# create the wumpus 
		self.wumpus = Wumpus(self.hunter.updateposition())

		# create cave layout
		self.layout = Caves(self.hunter.updateposition(), self.wumpus.updateposition())

		# define positions
		hunter_position = self.hunter.updateposition()
		hunter_x, hunter_y = self.generate_coords(hunter_position)
		self.sethunter(hunter_x, hunter_y)

		# create smooth running game - based on code of other group
		self.game = Process()
		self.game.start()

		# connect UI to functions
		self.connect(self.game, QtCore.SIGNAL("gold"), self.changegold, QtCore.Qt.DirectConnection)
		self.connect(self.game, QtCore.SIGNAL("arrow"), self.changeArrows, QtCore.Qt.DirectConnection)
		self.connect(self.game, QtCore.SIGNAL("play"), self.newturn, QtCore.Qt.DirectConnection)
		
		self.pushButton_2.clicked.connect(self.move_to_right)
		self.pushButton_3.clicked.connect(self.move_down)
		self.pushButton_4.clicked.connect(self.move_to_left)
		self.pushButton.clicked.connect(self.move_up)
		self.pushButton_5.clicked.connect(self.move_action)
		self.pushButton_6.clicked.connect(self.shoot)
		
		# change the amount of arrows in the screen
	def changeArrows(self):
		arrows = self.hunter.arrow_number()
		self.lcdNumber.display(arrows)
	
		# change the amount of gold in the screen
	def changegold(self):
		self.hunter.gold_number()
		gold = self.hunter.found_gold()
		self.lcdNumber_2.display(gold)          

	# character function which scales the image of the hunter inside a room of the cave
	def sethunter(self, hunterx, huntery):
		self.hunterphoto = QtGui.QGraphicsPixmapItem()
		self.hunterphoto.setPixmap(QtGui.QPixmap("character.gif"))
		self.hunterphoto.setPos(hunterx,huntery)
		self.hunterphoto.scale(0.5,0.5)
		self.scene.addItem(self.hunterphoto)
		
	# generate coords as pixels, centering the hunter in each room 
	def generate_coords(self, coords):
		return (coords[0] - 1) * 120 + 35, (coords[1] - 1) * 100 + 35
	
	#setting up the walking code for the hunter
	def move_hunter(self, direction):
		if self.step == True:
			self.pos = self.hunter.updateposition()
			if direction == "left" and self.pos[0] == 1:
				self.game.direction = "left"
				self.hunterphoto.setPixmap(QtGui.QPixmap('character.gif'))
				self.hunterphoto.moveBy(480 , 0)
				self.hunter.left()
			if direction == "left" and self.pos[0] != 1:
				self.game.direction = "left"
				self.hunterphoto.setPixmap(QtGui.QPixmap('character.gif'))
				self.hunterphoto.moveBy(-120, 0)
				self.hunter.left()
			if direction == "right" and self.pos[0] == 5:
				self.game.direction = "right"
				self.hunterphoto.setPixmap(QtGui.QPixmap('character.gif'))
				self.hunterphoto.moveBy(-480 , 0)
				self.hunter.right()
			if direction == "right" and self.pos[0] != 5:
				self.game.direction = "right"
				self.hunterphoto.setPixmap(QtGui.QPixmap('character.gif'))
				self.hunterphoto.moveBy(120, 0)
				self.hunter.right()
			if direction == "up" and self.pos[1] == 1:
				self.game.direction = "up"
				self.hunterphoto.setPixmap(QtGui.QPixmap('character.gif'))
				self.hunterphoto.moveBy(0, 300)
				self.hunter.up()
			if direction == "up" and self.pos[1] != 1:
				self.game.direction = "up"
				self.hunterphoto.setPixmap(QtGui.QPixmap('character.gif'))
				self.hunterphoto.moveBy(00, -100)
				self.hunter.up()
			if direction == "down" and self.pos[1] == 4:
				self.game.direction = "down"
				self.hunterphoto.setPixmap(QtGui.QPixmap('character.gif'))
				self.hunterphoto.moveBy(0, -300)
				self.hunter.down()
			if direction == "down" and self.pos[1] != 4:
				self.game.direction = "down"
				self.hunterphoto.setPixmap(QtGui.QPixmap('character.gif'))
				self.hunterphoto.moveBy(0, 100)
				self.hunter.down()
	# returns the layout of the cave
	def returnlayout(self):
		return self.layout
	
	# defines a step that the hunter takes	
	def steps(self):
		self.step = True

	# a function that defines the shoot function of the hunter
	def shoot(self):
		self.shoot = True

	# a function that lets the hunter do another step
	def turn(self):
		self.step = False
	
	# a function that continues the game
	def newturn(self): 
		self.game.play = None
		
	# A function that combines the pushbuttons with movement of the hunter
	def move_function(self, movement):
		if movement == "Moving":
			self.game.play = "Moving"
		if movement == "Shoot":
			self.game.play = "Shoot"
		if movement == "left":
			self.move_hunter("left")
		if movement == "right":
			self.move_hunter("right")
		if movement == "up":
			self.move_hunter("up")
		if movement == "down":
			self.move_hunter("down")
	
	# 2 functions that decide whether a player moves or shoots. 
	def move_action(self):
		self.move_function("Moving")

	def shoot(self):
		self.move_function("Shoot")
	
	# 4 move functions that let the hunter go up, down, left and right
	def move_to_left(self):
		self.move_function("left")

	def move_to_right(self):
		self.move_function("right")

	def move_up(self):
		self.move_function("up")

	def move_down(self):
		self.move_function("down")
		
	
	#setting up the message to show the users what is happening
	def setMessage(self, message):
		self.label_5.setText(_translate("Widget", message, None))
			
	def win(self):
		self.setMessage("You defeated the Wumpus")
		sleep(1)
		self.setMessage("You found {} gold and had {} arrows left".format(self.hunter.gold_number(),(self.hunter.arrow_number())))
		self.game.quit()

	def lose(self, won):
		self.setMessage("You Died! You found {} goud and had {} arrows left".format(self.hunter.gold_number(),(self.hunter.arrow_number())))
		self.game.quit()

#inspired by Mathijs Bonema his group, to let the game run more smoothly
class Process(QtCore.QThread):
	
	def __init__(self):
		QtCore.QThread.__init__(self)
		
	def run(self):
		sleep(1)
		ui.turn()
		alive = True
		self.play = None
		self.direction = None
		self.emit(QtCore.SIGNAL("gold"))
		self.emit(QtCore.SIGNAL("arrow"))
		cavevariable = ui.layout.returncaves()

		while alive:
			items = []
			xcoord, ycoord = ui.hunter.updateposition()
			if ycoord == 1:
				surroundposition = [(xcoord, ycoord + 1), (xcoord, 4), (xcoord + 1, ycoord), (xcoord - 1, ycoord)]
				surroundpositionwumpus = [(xcoord, ycoord + 1), (xcoord, 4), (xcoord + 1, ycoord), (xcoord - 1, ycoord)]
			elif xcoord == 1:
				surroundposition = [(xcoord, ycoord + 1), (xcoord, 5), (xcoord + 1, ycoord), (xcoord - 1, ycoord)]
				surroundpositionwumpus = [(xcoord, ycoord + 1), (xcoord, 5), (xcoord + 1, ycoord), (xcoord - 1, ycoord)]
			elif ycoord == 4:
				surroundposition = [(xcoord, 1), (xcoord, ycoord - 1), (xcoord + 1, ycoord), (xcoord - 1, ycoord)]
				surroundpositionwumpus = [(xcoord, 1), (xcoord, ycoord - 1), (xcoord + 1, ycoord), (xcoord - 1, ycoord)]
			elif xcoord == 5:
				surroundposition = [(xcoord, ycoord + 1), (xcoord, ycoord - 1), (1, ycoord), (xcoord - 1, ycoord)]
				surroundpositionwumpus = [(xcoord, ycoord + 1), (xcoord, ycoord - 1), (1, ycoord), (xcoord - 1, ycoord)]
			else:
				surroundposition = [(xcoord, ycoord + 1), (xcoord, ycoord - 1), (xcoord + 1, ycoord), (xcoord - 1, ycoord)]
				surroundpositionwumpus = [(xcoord, ycoord + 1), (xcoord, ycoord - 1), (xcoord + 1, ycoord), (xcoord - 1, ycoord)]

			for coordinates in cavevariable:
				for caves in surroundposition:
					if str(coordinates[0]) == str(caves):
						items.append(coordinates[1])

			# messages for whats happening in the game
			
			if "Gold" in items:
				ui.setMessage("There is gold near you")
				sleep(2)
			if "Bat" in items:
				ui.setMessage("You can hear a bat!")
				sleep(2)
			if "Pit" in items:
				ui.setMessage("You can feel the draft of a pit...!")
				sleep(2)
					
			for coordinates in cavevariable:
				for caves in surroundposition:
					if str(coordinates[0]) == str(caves):
						if str(caves) == str(ui.wumpus.updateposition()):
							ui.setMessage("I smell the Wumpus")

			if alive:
				if ui.hunter.updateposition() == ui.wumpus.updateposition():
					ui.setMessage("The Wumpus ate You!")
					alive = False
					ui.lose(False)
					if ui.hunter.updateposition() == ui.wumpus.updateposition():
						ui.setMessage("The Wumpus ate you")
						alive = False
						ui.lose(False)
			
			ui.setMessage("What do you want to do next?")
			self.emit(QtCore.SIGNAL("play"))
			self.play = None
			while self.play == None:
				sleep(1)			
			
			# allows the player to move and shoot 
			if self.play == "Moving":
				ui.turn()
				ui.setMessage("Where do you want to go?")
				self.direction = None
				while self.direction == None:
					sleep(1)
				ui.turn()
				sleep(1)
				
				for room in cavevariabele:
					if ui.hunter.updateposition() == room[0]:
						if room[1] == "Gold":
							ui.setMessage("You have found gold!")
							room[1] = None
							sleep(1)
							self.emit(QtCore.SIGNAL("gold"))
						elif room[1] == "Bat":
							ui.setMessage("The bat took you to another room!")
							sleep(1)
							newxcoords, newycoords= ui.hunter.replace1(ui.wumpus.updateposition())
							replacehunterx, replacehuntery = ui.generate_coords((newxcoords, newycoords))
							ui.hunterphoto.setPos(replacehunterx,replacehuntery)
						elif room[1] == "Put":
							ui.setMessage("You fell into a pit and died!")
							sleep(1)
							alive = False
		
			#self.play = None						

def run():
	app = QtGui.QApplication(sys.argv)
	app.setStyle('cleanlooks')
	ui = Ui_Widget()
	ui.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	app.setStyle('cleanlooks')
	ui = Ui_Widget()
	ui.show()
	sys.exit(app.exec_())

