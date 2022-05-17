# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:15:20 2022

@author: jared
"""
from numpy import random

class myClass:
    def __init__(self, name, myVar1, myVar2, *argv):
        self.name = name
        self.myVar1 = myVar1
        self.myVar2 = myVar2
        self.myList = []
        for arg in argv:
            self.myList.append(arg)
        
    def __eq__(self, other):
        return(self.myVar1 == other.myVar1)
    
    def __ne__(self, other):
        return(self.myVar1 != other.myVar1)
    
    def __gt__(self, other):
        if self.myVar1 > other.myVar1:
            return self
        else:
            return other
        
    def __lt__(self, other):
        if len(self.myList) > len(other.myList):
            return other.myList
        else:
            return self.myList
        
    def __str__(self):
        return f'myClass({self.name},{self.myVar1},{self.myVar2},{self.myList})'
    
    def getInfo(self):
        return({
            'Name': self.name,
            'myVar1': self.myVar1,
            'myVar2': self.myVar2,
            'myList': self.myList})
        
    
        
# Generate object with self.name of 'First Object', and a series of random 
# integers between 1 and 20        
myObject = myClass('First Object',random.randint(1,20),random.randint(1,20), 
                   random.randint(1,20),random.randint(1,20),
                   random.randint(1,20),random.randint(1,20))

# Generate object with self.name of 'Second Object', and a shorter 
# series of random integers between 1 and 20        
myObject2 = myClass('Second Object',random.randint(1,20),
                      random.randint(1,20),random.randint(1,20),
                      random.randint(1,20))

# Set myFinalObject to be the object returned from the gt comparison
myFinalObject = myObject > myObject2

# Display values for myObject as dictionary called from getInfo function
print('*** First Object ***')
print(myObject.getInfo())

# Display values for myObject2
print('*** Second Object ***')
print(myObject2.getInfo())

# Display boolean operator returned from __eq__
print('*** Are object myVar1 values equal or not equal: ***')
print('Equal: {}'.format(myObject == myObject2))
print('Not Equal: {}'.format(myObject != myObject2))


#Display values for final object, determined by gt comparison
print('*** Final Object ***')
print(myFinalObject.getInfo())

#Display shorter list based on lt comparison in both directions
print('*** Shorter List ***')
print(myObject < myObject2)
print(myObject2 < myObject)

#Display string output of myClass for each object
print('*** String output of objects ***')
print(myObject)
print(myObject2)
print(myFinalObject)

