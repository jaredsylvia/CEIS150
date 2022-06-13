# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:02:31 2022

@author: jared
"""
import math




# Generate a string using three variables gathered by user input
questionsThree = lambda a, b, c : \
    'Name: {}\nQuest: {}\nAirspeed velocity of an unladen swallow: {}'.format(
        a,b,c)
print('*** Before continuing please answer these questions three:')
name = input('What is your name? ')
quest = input('What is your quest? ')
unladenSwallow = input('What is the airspeed velocity of an unladen swallow? ')

print(questionsThree(name,quest,unladenSwallow))



# Calculate the length of the hyoptenuse of a right triangle useing the Pythagorean theorem

triangleCalc = lambda a, b : math.sqrt((a * a) + (b * b))

print('*** Calculate the length of the hypotenuse of a right trangle ***')
try:
    lenAdj = float(input('Length of adjacent side: '))
    lenOpp = float(input('Length of opposite side: '))
except ValueError:
    print('Please enter a valid length. Do not include measurement unit.')
else:
    print('Adjacent: {}\nOpposite: {}\nHypotenuse: {}'.format(lenAdj, lenOpp, 
        round(triangleCalc(lenAdj,lenOpp),2)))


# Using lambda inline to sort by unique circumstances
nestedList = [[3,5,8,11], [2,6,7,8], [5,4,9,12], [6,14,18,3]] 
print('*** List sorting ***')
print('Given the following nested list: ')
print(nestedList)
print('\nApplying a traditional sort we get the following: ')
nestedList.sort()
print(nestedList)
print('\nApplying \'reverse = True\' to sort')
nestedList.sort(reverse=True)
print(nestedList)
print('\nApplying a lambda expression as the key to sort by the second number')
nestedList.sort(key=lambda x: x[1])
print(nestedList)
print('\nAgain but with the third number')
nestedList.sort(key=lambda x: x[2])
print(nestedList)