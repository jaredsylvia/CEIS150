# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:05:10 2022

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




fruitListTypes = [apple, banana, orange]
fruitListQty = [3, 12, 18]

fruitDict = {'Apple': { 'objectInfo' : vars(apple), 'qty' : 3},
              'Banana': {'objectInfo' : vars(banana), 'qty' : 12},
              'Orange': {'objectInfo': vars(orange), 'qty' : 18}
              }

print('*** Processing lists ***')
u=0
for i in fruitListTypes:
    print(vars(i))
    print(fruitListQty[u])
    u+=1

print('*** Processing dictionary')

print(fruitDict)