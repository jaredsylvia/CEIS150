# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 10:37:10 2022

@author: jared
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.devry.edu/about/contact-us.html'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
divs = soup.find_all("div", 
    {"class": "aem-Grid aem-Grid--default--12 aem-Grid--tablet--6 aem-Grid--phone--1"})

for i in divs:
    if i.find("div", {"class": "backgroundColorLightGrey"}):
        if i.find("p"):
            print(i.text)
        
        