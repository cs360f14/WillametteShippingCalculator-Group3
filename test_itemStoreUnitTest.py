#!/usr/bin/python3

################################
# File Name:	test_SaleItemUnitTest.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Unittest for SaleItem
################################


import unittest
from itemStore import ItemStore
from SaleItem import SaleItem

class TestSaleItem(unittest.TestCase):
	
	
	def setUp(self):
		""" the text fixture, necessary setup for the tests to run
		"""
		self.theItemStore= ItemStore('dataFiles/testItemStore.csv')
		
		
	def tearDown(self):
		""" nothing to tear down here
		If your test created a database or built a network connection
		you might delete the database or close the network connection
		here. You might also close files you opened, close your
		TK windows if this is GUI program, or kill threads if this is
		a multithreaded application
		"""
		pass # nothing to do



	def test_getItemById(self):
		
		testSaleItem = SaleItem(['30', '10', ' Bat'])
		returnID = self.theItemStore.getItemById (2)
		self.assertEqual(testSaleItem.getCost(), returnID.getCost())
		self.assertEqual(testSaleItem.getWeight(), returnID.getWeight())
		self.assertEqual(testSaleItem.getTitle(), returnID.getTitle())
		
"""	
	def test_getItemByIdNotEqual(self):
		
		testSaleItem = SaleItem(['500', '200', ' Couch'])
		returnID = self.theItemStore.getItemById (2)
		self.assertNotEqual(testSaleItem.getCost(), returnID.getCost())
		self.assertNotEqual(testSaleItem.getWeight(), returnID.getWeight())
		self.assertNotEqual(testSaleItem.getTitle(), returnID.getTitle())
"""		
	
		
