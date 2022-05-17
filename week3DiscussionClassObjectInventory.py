# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:17:28 2022

@author: jared
"""


class user:
    def __init__(self, name, employee_num):
        self.name = name
        self.employee_num = employee_num
        
    def __eq__(self, other):
        return self.employee_num == other.employee_num
    
    def __str__(self):
        return(f'user({self.name},{self.employee_num})')
    
class vendor:
    def __init__(self, name, address, contact, vendor_id, employee):
        self.name = name
        self.address = address
        self.contact = contact
        self.vendor_id = vendor_id
        self.employee = employee
    
    def __eq__(self, other):
        return self.vendor_id == other.vendor_id
    
    def __str__(self):
        return(f'vendor({self.name},{self.vendor_id},{self.employee}')
    
class item:
    def __init__(self, name, description, upc, cost, vendor, employee):
        self.name = name
        self.description = description
        self.upc = upc
        self.cost = cost
        self.vendor = vendor
        self.employee = employee
       
    def __eq__(self, other):
        return self.upc == other.upc
    
    def __str__(self):
        return(f'item({self.name},{self.description},{self.upc},{self.employee}\n'
               f'{self.vendor}\n')
    
# Create two separate employees both named Dave    
employee1 = user('Dave', 101)
employee2 = user('Dave', 105)

# employee1 is in charge of adding vendors to the system
vendor1 = vendor('Spacely Sprockets', '123 E. Main', 
                 '(800)555-1212', 1001, employee1)
vendor2 = vendor('Cogswell Cogs', '345 W. First',
                 '(888)555-1212', 1008, employee1)

# employee2 is in charge of adding items to the system
item1 = item('Cog', 'A Cog', 'ABC123', 5.99, vendor1, employee2)
item2 = item('Sprocket', 'A Sprocket', 'ABC456', 6.99, vendor1, employee2)
item3 = item('Cog', 'A Cog', 'DEF123', 5.49, vendor2, employee2)
item4 = item('Sprocket', 'A Sprocket', 'DEF456', 6.49, vendor2, employee2)
    
print(item1)        