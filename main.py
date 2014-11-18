#!/usr/bin/python3

################################
# File Name:	main.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Simulate an online store
################################

from itemStore import ItemStore
from basket import Basket
from ShippingLogic import *
import sys
import getopt

# python3 main.py --file dataFiles/normalSales.csv [--shipping (normal|sale)]

def displayItems(theStore):
	""" display all the items in the store
	"""
	
	print('\n')
	print(str(0).rjust(3) + '.' + ' Display Basket'.ljust(25))
	for item in theStore.items():
		print(str(item.getID()).rjust(3) + '.' + item.getTitle().ljust(25)+ '\t'+
		'\t' + "${:.2f}".format(int(item.getCost())).rjust(7) + 
		 '\t'+item.getWeight().rjust(5), end='')
		if item.getFreeShipping() :
			print(' Free Shipping!')
		else:
			print('')
	print('\n')
	
def addItem(theStore, basket, itemID, qty):
	""" add an item
	
	If that item is already in the basket, the requested
	quantity (qty) is added to the existing quantity
	"""
	basket.addItem( [qty, theStore.getItemById(itemID)])

	
def printBasket(basket):
	""" display contents of the basket
	
	Also display the total weight, total charged weight (disregarding
	items with free shipping)
	"""
	
	totalWeight = 0	
	totalChargedWeight = 0
	print('\n=====Basket=====')
	for item in basket.items():
		print('Quantity: ' + str(item[0]) + ' ' +item[1].getTitle() 
			+ ' Total Cost: ' + "${:.2f}".format(int(item[1].getCost()) * item[0]) 
			+ ' Weight: ' + str(item[0]* int(item[1].getWeight())))
		totalWeight += item[0]* int(item[1].getWeight())
		if item[1].getFreeShipping() is False :
			totalChargedWeight += (item[0]* int(item[1].getWeight()))

	print('\nTotal Weight: ' + str(totalWeight))
	print('Total Charged Weight: ' + str(totalChargedWeight))
	print('================\n')
	
def main(filename, shippingLogic):
	# read items into the itemStore
	# display menu
	# add item to basket in given quantity
	# repeat to display
	# calculate shipping

	
	theStore = ItemStore(filename)
	basket = Basket()
	
	choice = 0
	
	while choice != -1 :
	
		displayItems(theStore)
		choice = int(input('Select item (-1 to quit) '))
	
		if choice == 0:
			printBasket(basket)
			total = basket.getTotalShipping(shippingLogic)
			print('Estimated Shipping cost: '+ str(total))
			
		elif choice != -1:
			qty = int(input('Quantity: '))
	
			addItem(theStore, basket, choice, qty)
	
	printBasket(basket)
	
	total = basket.getTotalShipping(shippingLogic)
	print(shippingLogic.getName() +' Shipping cost: '+ str(total))



def usage():
	print('python3 main.py --file dataFiles/normalSales.csv [--shipping (normal|sale)]')
	print('')



	
# invoke main()
if __name__ == "__main__":

	shippingLogic = ShippingLogic()
	filename = 'dataFiles/normalSales.csv'
	
	try:
		optlist, args = getopt.getopt(sys.argv[1:],'' , ['help', 'file=', 'shipping='])
		
		for option, arg in optlist:
			if option == '--file':
				filename = arg
			elif option == '--shipping':
				if arg == 'sale':
					shippingLogic = SaleShippingLogic()
			elif option == '--help':
				usage()
				sys.exit(0)
				
	except getopt.GetoptError as err:
		print('Option error!')
		usage()
		sys.exit(1)
		
	
	main(filename, shippingLogic)
