# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:49:15 2022

@author: jared
"""
class CA:
    def __init__(self):
        self.state = 'California'
        self.statePop = 39500000
        self.stateCapital = 'Sacramento'
        

class Stanislaus(CA):
    def __init__(self):
        super().__init__()
        self.county = 'Stanislaus'
        self.countyPop = 546235
        self.seat = 'Modesto'
        
class City(Stanislaus):
    def __init__(self, city, cityPop):
        super().__init__()
        self.city = city
        self.cityPop = cityPop

StanislausCities = []
StanislausCities.append(City('Turlock', 72715))
StanislausCities.append(City('Ceres', 48355))
StanislausCities.append(City('Riverbank', 24623))
StanislausCities.append(City('Oakdale', 22932))
StanislausCities.append(City('Modesto', 214485))


for i in StanislausCities:
    print('*** {} ***'.format(i.city))
    print('{},{} is located in {}.'.format(i.city, i.state, i.county))
    print('where the county seat is {}. {} has a population of {}.'.format(i.seat, i.city, i.cityPop))
    print('{} has a population of {}, and {} has a population of {}.'.format(i.county, i.countyPop, i.state, i.statePop))
    print('The capital of {} is {}.'.format(i.state, i.stateCapital))
    print('*** *** ***\n\n')

