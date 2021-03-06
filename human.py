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
		self.ageOfMaturity = 5000
		self.preferenceOfDirection = self.decideWhereToWalk()
		self.NORTH = self.posy -1
		self.EAST = self.posx + 1
		self.SOUTH = self.posy + 1
		self.WEST = self.posx -1
		self.partner = None
		self.children = []
		self.friends = []
		self.partner = None
		self.timeSinceBaby = 0
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

	def agressive(self, encounter):
		if encounter in self.friends:
			return False
		a = random.randrange(2)
		if a == 1:
			return True
		else:
			a = random.randrange(2)
			if a > 0.99:
				return True
			else:
				return False

	def makeLoveNotWar(self, lover):
		baby = None
		if self.partner == None or self.partner == lover:
			if self.age >= self.ageOfMaturity and lover.age >= lover.ageOfMaturity and self.timeSinceBaby > 300 and lover.timeSinceBaby > 300:
				name = self.name + lover.name
				baby = Human(name,self.posx+2, self.posy)
				#print(baby)
				self.partner = lover
				self.timeSinceBaby = 0
				lover.timeSinceBaby = 0
		return baby

	def __meetAndGreatInteraction(self, posOne, posTwo, world):
		baby = None
		if not world[posOne][posTwo].isHere == None:
			if not self == world[posOne][posTwo].isHere:
				encounter = world[posOne][posTwo].isHere
				if self.agressive(encounter):
					self.fightYeBastards(encounter)
				else:
					if not encounter in self.friends:
						self.friends.append(encounter)
					baby = self.makeLoveNotWar(encounter)
					self.friends.append(encounter)
		return baby

	def meetAndGreat(self, world):#FIGHT YE BASTARDS
		humans = self.look(world, Human)
		baby = None
		if humans[0]:
			self.__meetAndGreatInteraction(self.posx, self.NORTH, world)
		elif humans[1]:
			self.__meetAndGreatInteraction(self.EAST, self.posy, world)
		elif humans[2]:
			self.__meetAndGreatInteraction(self.posx, self.SOUTH, world)
		elif humans[3]:
			self.__meetAndGreatInteraction(self.WEST, self.posy, world)
		return baby

	def doStuff(self, world):
		#Age check is needed to be done, so it's not an infinite loop of pairs
		#Should also do so they don't kill their children
		baby = self.meetAndGreat(world)
		self.posx = self.wrapAround(self.posx, len(world))
		self.posy = self.wrapAround(self.posy, len(world))
		self.walk(world)
		self.timeSinceBaby += 1
		self.age += 1
		return baby


if __name__ == '__main__':
	bob = Human("bob", 1, 1)
