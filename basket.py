#!/usr/bin/python3

################################
# File Name:	basket.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Provide a shopping basket for an online store
################################

class Basket:
	""" The customer's shopping basket
	"""
	
	def __init__(self):
		""" the basket starts empty 
		
		The basket contains a list of (qty, SaleItem) tuples
		"""
		self._items = []
		
	def addItem(self, item):
		""" add an item (qty, SaleItem)
		
		If the item already exists, add the specified quantity
		of the item to the existing entry in the basket
		"""
		
		if self.contains(item[1].getID()):
			self.merge(item[1].getID(), item[0])
		else:
			self._items.append(item)
		
	def items(self):
		""" walk through the items"""
		for item in self._items:
			yield item

	def getTotalShipping(self, sLogic):
		""" use the given logic to determine weight and cost
		"""
		weight = sLogic.calcWeightForCost(self)
		cost = sLogic.calcCostForShippingByWeight(weight)
		return cost
		
		
	def contains(self, itemID):
		""" determine if the basket contains this itemID """
		found = False
		for item in self._items:
			if item[1].getID() == itemID:
				found = True
					
		return found
		
	def merge(self, itemID, qty):
		""" merge the given quantity of itemID with the existing
		entry in the basket
		"""
		
		found = False
		for item in self._items:
			if item[1].getID() == itemID:
				item[0] = qty
				found = True
					
		return found
