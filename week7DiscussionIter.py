# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 12:02:10 2022

@author: jared
"""

class Fruit:
    def __init__(self, name, color, exterior):
        self.name = name
        self.color = color
        self.exterior = exterior
        
class NumberIterator:
    def __init__(self, name, increment=1):
        self.name = name
        self.increment = increment
        
    def __iter__(self):
        self.value = 1
        return self
        
    def __next__(self):
        self.value += self.increment
        return self
        
apple = Fruit('Apple', 'Red', 'Skin')
banana = Fruit('Banana', 'Yellow', 'Peel')
orange = Fruit('Orange', 'Orange', 'Rind')



fruitDict = {'Apple': { 'objectInfo' : vars(apple), 'qty' : 3},
              'Banana': {'objectInfo' : vars(banana), 'qty' : 12},
              'Orange': {'objectInfo': vars(orange), 'qty' : 18}
              }

fruitIter = iter(fruitDict)

iterByOne = NumberIterator('byOne')
iterByTwo = NumberIterator('byTwo', 2)

print('***Iterate through dictionary***')
for i in fruitDict:
    thisIter = next(fruitIter)
    print('Object: {}'.format(thisIter)) #this can also be done using variable 'i'
    print(fruitDict[thisIter])

print('***Iterate using Class methods, by increments of one and two***')

print('***By one***')
firstIterLoop = iter(iterByOne)
for i in range(0, 8):
    print(vars(next(firstIterLoop)))

print('***By two***')
secondIterLoop = iter(iterByTwo)
for i in range(0, 8):
    print(vars(next(secondIterLoop)))