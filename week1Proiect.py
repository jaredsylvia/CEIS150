# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:25:28 2022

@author: jared
"""
import numpy

countVar = 0
sumVar = 0
higherPrices = []

fullName = input('Full Name: ')
minPrice = float(input('Minimum Price: '))
priceList = []
for i in range(0,10):
    priceList.append(numpy.random.uniform(1,100))

for i in priceList:
    sumVar += i
    if i > minPrice:
        countVar += 1
        higherPrices.append(i)
priceList.sort()

print('******\nHello,', fullName, 'The minimum price is', str(minPrice))
print('There are', str(countVar), 'prices greater than the minimum price.')
print('The total price is', str(round(sumVar,2)))
print('Higher prices are:')
for i in higherPrices:
    print(round(i,2), end= ', ')
print('\n******\nRandomly Generated Price List of numbers between 1 and 100:\n' +
      str(priceList))
