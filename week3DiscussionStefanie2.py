# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:24:29 2022

@author: jared
"""

class County:

    def __init__(self, city, county, population, state):

        self.city= city
        
        self.county= county
        
        self.population= population
  
        self.state= state


myCounty = County(input('Name of city: '),
                        input('Name of county: '),
                        input('City populaiton: '),
                        input('State: '))

print("I live in ", myCounty.city, "and the county I live in is ", myCounty.county)

print("The population of the city I live in is ", myCounty.population)

print("I like living in ", myCounty.city, ", ", myCounty.state)