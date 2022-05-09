# -*- coding: utf-8 -*-
"""
Created on Sun May  8 17:45:37 2022

@author: jared
"""
import secrets
import time

class APIauth: # A fake class that stores information for authenticating against a fake API
    def __init__(self):
        self.key = 'CN^mn(Cn?j/3g|K'
        self.secret = 'AZu?8@Z5roI<Grx'
        
    def genNonce(self):
        tokenHex = secrets.token_hex(15)
        return(str(tokenHex) + str(round(time.time())))

print('******')
print('Key encapsulated in class:', APIauth().key)
print('Secret encapsulated in class:', APIauth().secret)
print('Function generating nonce encapsulated in class:', APIauth().genNonce())

# print(APIauth().genNonce().tokenHex) 
# uncommenting the above line returns in an error because tokenHex is only known to the functin genNonce