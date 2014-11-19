#!/usr/bin/python3

################################
# File Name:	SaleItem.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		An individual item for sale
################################

class SaleItem:
	
	# this is a list because we need a mutable object to be shared
	# among all instances of SaleItem
	runningItemID = [1]
	
	def __init__ (self, listDetails) :
		""" An item for sale
		
		Each item contains:
		cost
		weight
		title
		freeshipping (true or false)
		item id 
		"""
	
		self._cost = listDetails[0]
		self._weight = listDetails[1]
		self._title = listDetails[2]
		self._freeShipping = False
		
		if len(listDetails) == 4 :
			self._freeShipping = True
			
		self._itemID = self.runningItemID[0]
		self.runningItemID[0] += 1
			

	def getCost(self):
		return self._cost
		
	def getWeight(self):
		return self._weight
		
	def getTitle(self):
		return self._title

	def getFreeShipping(self):
		return self._freeShipping
		
	def getDetailsAsString(self):
		return self._title + ' $' +str(self._cost)
		
	def getID(self):
		return self._itemID
		
		
		
