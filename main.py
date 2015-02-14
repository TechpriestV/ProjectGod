#!/usr/bin/env python
# -*- coding: utf-8 -*-

from human import Human
from ground import GroundTile
import time, os, random
#from Tkinter import tkinter

def createWorld(size, empty):
	"""
	row = * size
	world = []
	for i in range(size):
		world.append(row[:])
	return world
	"""
	world =[]
	for y in range(size):
		row = []
		for x in range(size):
			gt = GroundTile(x, y)
			row.append(gt)
		world.append(row)
	return world

def drawWorld(world):
	row = ""
	for i in world:
		for j in i:
			if j.isHere == None:
				row = row + "_"
			else:
				row = row + j.isHere.name[0]
		print(row)
		row = ""
	print("\n")


def createHumans(worldSize):
	humans = []
	names = ["Bob", "Hugo", "Steve", "Lars", "Ola", "Per", "Rob"]
	for i in names:
		human = Human(i, random.randrange(worldSize), random.randrange(worldSize))
	#bob = Human("bob", 1, 1)
		humans.append(human)
	return humans

def updateWorld(world, humans):
	for i in humans:
		baby = i.doStuff(world)
		if not baby == None:
			humans.append(baby)
		world[i.posx][i.posy].place(i)
		if i.alive == False:
			world[i.posx][i.posy].isHere = None
			humans.remove(i)
	for i in humans:
		i.age += 1
	return world, humans

def main(humans, world):
	cycles = 0
	pongs = 0
	while len(humans)>1:
		world, humans = updateWorld(world, humans)
		"""
		print("There should be something printed here")
		for i in world:
			for j in i:
				if not j.isHere == None:
					print(j)
		"""
		cycles += 1
	print("It took ", cycles, " cycles for everyone but one die")
	for i in humans:
		print(i)

if __name__ == '__main__':
	empty = "_"
	worldSize = 128
	world = createWorld(worldSize, empty)
	humans = createHumans(worldSize)
	main(humans, world)

