#!/usr/bin/python3

################################
# File Name:	ShippingLogic.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		The shipping calculator
################################

class ShippingLogic:
	""" Standard shipping costs
	
	A small table is build in the constructor
	to encode what each shipping weight costs.
	
	The FREE_SHIPPING_WEIGHT indicates at what weight
	an order receives free shipping
	"""
	
	def __init__(self):
		self._rate=[]
		
		# the table is: (low Weight, high Weight, cost)
		# low weight is inclusive
		# high weight is not inclusive		
		self._rate.append( ( .01, 1, 5) )
		self._rate.append( ( 1, 5, 7) )
		self._rate.append( ( 5, None, 10) )
		self._FREE_SHIPPING_WEIGHT = 50
	
	
	def calcWeightForCost(self, basket):
		""" determine the total chargable weight of the items in the basket
		"""
		
		weight = 1
		
		for item in basket.items():
			if item[1].getFreeShipping() :
				weight += (item[0] * int(item[1].getWeight()))
				
		return weight


	def calcCostForShippingByWeight(self, weight):
		""" determine the total cost of shipping the given weight
		"""
		
		cost = 0
		
		if weight <= self._FREE_SHIPPING_WEIGHT:
			for rate in self._rate :
				if weight >= rate[0] and (rate[1] is None or weight < rate[1]) :
					cost += rate[2]

		return cost

	def getName(self):
		""" the name of the shipping prices
		"""
		return 'Standard'

class SaleShippingLogic(ShippingLogic):
	""" Shipping prices for our Holiday Sale!
	"""
	
	def __init__(self):
		self._rate=[]
		self._rate.append( ( .01, 1, 3) )
		self._rate.append( ( 1, 3, 4) )
		self._rate.append( ( 4, 6, 6) )
		self._rate.append( ( 6, None, 7) )
		self._FREE_SHIPPING_WEIGHT = 100

	def getName(self):
		""" the name of the shipping prices
		"""
		return 'Sale'
