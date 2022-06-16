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
        
apple = Fruit('Apple', 'Red', 'Skin')
banana = Fruit('Banana', 'Yellow', 'Peel')
orange = Fruit('Orange', 'Orange', 'Rind')



fruitDict = {'Apple': { 'objectInfo' : vars(apple), 'qty' : 3},
              'Banana': {'objectInfo' : vars(banana), 'qty' : 12},
              'Orange': {'objectInfo': vars(orange), 'qty' : 18}
              }

fruitIter = iter(fruitDict)

for i in fruitDict:
    thisIter = next(fruitIter)
    print('Object: {}'.format(thisIter)) #this can also be done using variable 'i'
    print(fruitDict[thisIter])
   
    