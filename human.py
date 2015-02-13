#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
class Human(object):
	"""docstring for Human"""
	def __init__(self, name, posx, posy):
		self.name = name
		self.posx = posx
		self.posy = posy
		self.alive = True
		self.baseStrenght = 5
		self.age = 0
		self.preferenceOfDirection = self.decideWhereToWalk()
		self.NORTH = self.posy -1
		self.EAST = self.posx + 1
		self.SOUTH = self.posy + 1
		self.WEST = self.posx -1
		self.friends = []
	def __str__(self):
		tmp = "Hi, my name is " + self.name + " and my age is " + str(self.age) +" cycles, I am at X:" + str(self.posx) +" Y:"+ str(self.posy)
		return tmp

	def look(self,world, what):
		""" Returns true of false depending if the areas around are occuppied or not"""
		# DO A FUNCTION! FUNCTION DONE see tryLook()
		ways = []
		ways.append(self.tryLook(self.posx, self.posy-1, world, what)) #North
		ways.append(self.tryLook(self.posx+1, self.posy, world, what)) #East
		ways.append(self.tryLook(self.posx, self.posy+1, world, what)) #South
		ways.append(self.tryLook(self.posx-1, self.posy, world, what)) #West
		return ways

	def tryLook(self, x, y, world, what):
		try:
			world[x][y].isHere == what
			return True
		except IndexError:
			return False
		else:
			return False
	def doWalk(self, addX, addY):
		self.posx = self.posx + addX
		self.posy = self.posy + addY

	def walk(self, world):
		world[self.posx][self.posy].isHere = None
		ways = self.look(world, None)
		thinking = True
		while thinking:
			randDirection = self.decideWhereToWalk()
			if ways[randDirection]:
				if randDirection == 0: #North
					thinking = False
					self.doWalk(0, -1)
				elif randDirection == 1: #East
					thinking = False
					self.doWalk(1, 0)
				elif randDirection == 2: #South
					thinking = False
					self.doWalk(0, 1)
				elif randDirection == 3: #West
					thinking = False
					self.doWalk(-1, 0)

	def decideWhereToWalk(self):
		directions = [0,1,2,3]
		random.shuffle(directions)
		direction = directions[0]
		return direction

	def wrapAround(self, pos,worldLength):
		pos = pos
		if pos >= worldLength:
			pos = 0
		elif pos <= -worldLength:
			pos = 0
		return pos

	def fightYeBastards(self, opponent):
		if self.punch() >= opponent.punch():
			opponent.alive = False
			self.baseStrenght += 1
		else:
			self.alive = False
			opponent.baseStrenght += 1

	def punch(self):
		force = random.randrange(20) + self.baseStrenght
		return force
	def agressive(self):
		a = random.randrange(2)
		if a = 1:
			return True
		else:
			return False

	def meetAndGreat(self, world):#FIGHT YE BASTARDS
		humans = self.look(world, Human)
		if humans[0]:
			if not world[self.posx][self.NORTH].isHere == None:
				if not self == world[self.posx][self.NORTH].isHere:
					
					if self.agressive():
					self.fightYeBastards(world[self.posx][self.NORTH].isHere)

		elif humans[1]:
			if not world[self.East][self.posy].isHere == None:
				if not self == world[self.East][self.posy].isHere:
					self.fightYeBastards(world[self.East][self.posy].isHere)
		elif humans[2]:
			if not world[self.posx][self.SOUTH].isHere == None:
				if not self == world[self.posx][self.SOUTH].isHere:
					self.fightYeBastards(world[self.posx][self.SOUTH].isHere)
		elif humans[3]:
			if not world[self.WEST][self.posy].isHere == None:
				if not self == world[self.WEST][self.posy].isHere:
					self.fightYeBastards(world[self.WEST][self.posy].isHere)

	def doStuff(self, world):
		self.meetAndGreat(world)
		self.walk(world)
		self.posx = self.wrapAround(self.posx, len(world))
		self.posy = self.wrapAround(self.posy, len(world))


if __name__ == '__main__':
	bob = Human("bob", 1, 1)
	print(bob)
