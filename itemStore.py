#!/usr/bin/python3

################################
# File Name:	itemStore.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Demonstrate the inventory system on an online store
################################

import csv
from SaleItem import SaleItem

class ItemStore :
	
	def __init__ (self, filename) :
		""" construct item store and read data from a csv file
		"""
		
		# create an empty list for the inventory
		self._inventory = []
		
		with open(filename) as csvFile :
			# open the reader
			csvReader = csv.reader(csvFile)
			
			# read each row
			for dataRow in csvReader :
				if len(dataRow) > 0 :
					# put the data into the list as a SaleItem
					self._inventory.append(SaleItem(dataRow))
		
	def items(self):
		""" generator for accessing items in inventory
		"""
		for dataRow in self._inventory:
			yield dataRow

	def getItemById(self, itemID):
		""" get an item by itemID
		"""
		for dataRow in self._inventory:
			if dataRow.getID() == itemID:
				return dataRow
		
		return None
