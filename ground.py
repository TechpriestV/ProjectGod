#!/usr/bin/env python
# -*- coding: utf-8 -*-

class GroundTile(object):
	"""docstring for GroundTile"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		#self.occupied = False
		self.isHere = None
		self.type = "Grass"
	def __str__(self):
		return self.type + str(self.x) + str(self.y) + str(self.isHere)

	def place(self, what):
		self.x = what.posx
		self.y = what.posy
		self.isHere = what
