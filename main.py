#!/usr/bin/env python
# -*- coding: utf-8 -*-

from human import Human
from ground import GroundTile
import time, os, random, sys
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
				row = row + " "
			else:
				row = row + j.isHere.name[0]
		row += "\n"
	return(row)


def createHumans(worldSize):
	humans = []
	names = ["Bob", "Hugo", "Steve", "Lars", "Ola", "Per", "Rob", "Eve", "Joe", "Ava"]
	for i in names:
		human = Human(i, random.randrange(worldSize), random.randrange(worldSize))
	#bob = Human("bob", 1, 1)
		humans.append(human)
	return humans

def updateWorld(world, humans):
	for i in humans:
		baby = i.doStuff(world)
		if not baby == None:
			#print(baby)
			humans.append(baby)
		world[i.posx][i.posy].place(i)
		if i.alive == False:
			world[i.posx][i.posy].isHere = None
			humans.remove(i)
			#for i in humans:
	 		#	print(i)
	return world, humans

def main(humans, world):
	cycles = 0
	pongs = 0
	try:
		while len(humans)>1:
			world, humans = updateWorld(world, humans)
			"""
			print("There should be something printed here")
			for i in world:
				for j in i:
					if not j.isHere == None:
						print(j)
			"""
			#print(drawWorld(world), end="\r")
			cycles += 1
			print("Cycle: ", cycles, "	","Humans: ", len(humans), end="\r")
		print("It took ", cycles, " cycles for everyone but one die")
		for i in humans:
			print(i)
	except KeyboardInterrupt as e:
		for i in humans:
 			print(i)
		sys.exit()
	#drawWorld(world)

if __name__ == '__main__':
	empty = "_"
	worldSize = 50
	world = createWorld(worldSize, empty)
	humans = createHumans(worldSize)
	print("Starting simulation")

	main(humans, world)
