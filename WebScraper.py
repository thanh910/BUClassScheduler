#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 03:29:19 2022

@author: thanh, grace, derek, rylie, jenny
"""


import requests
from bs4 import BeautifulSoup
import Sections

course = input("Enter a course: ")
course = course.lower().replace(" ", "")

URL = "https://www.bu.edu/phpbin/course-search/section/?t=" + course + "&semester=2022-FALL&return=%2Fphpbin%2Fcourse-search%2Fsearch.php%3Fpage%3Dw0%26pagesize%3D10%26adv%3D1%26nolog%3D%26search_adv_all%3DCAS%2BCS%2B237%26yearsem_adv%3D2022-FALL%26credits%3D%2A%26pathway%3D%26hub_match%3Dall"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all(class_="first-row")


classes = []
for result in results:
    Section = result.find_all("td")
    section = []
    
    for element in Section:
        section += [element.text.strip()]
        
    if section != '':
        classes += [section]


classes = classes[1:]
courses = []


for data in classes:
    courses += [Sections.Section(data[0], data[2], data[3], data[4], data[5], data[7])]
    
print(courses)
    
