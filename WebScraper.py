#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 03:29:19 2022

@author: thanh, grace, derek, rylie, jenny
"""


import requests
from bs4 import BeautifulSoup

semester = input("Enter a semester (ex. Fall 2022): ")
courseName = input("Enter a course (ex. CAS XX 123): ")

semester = semester.replace(" ", "+")
courseName = courseName.upper().split(" ")


URL = "https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1658458219?ModuleName=univschr.pl&SearchOption" + \
    "Desc=Class+Number&SearchOptionCd=S&KeySem=20233&ViewSem=" + semester + \
    "&College=" + courseName[0] + "&Dept=" + courseName[1] + "&Course=" + courseName[2] + "&Section="
    
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

for linebreak in soup.find_all('br'):
    linebreak.replace_with("\n")

results = soup.find_all("font")

sections =[]

for line in results:
    data = []
    
    for element in line:
        if element.text.strip() != "":
            data += [element.text.strip().replace("\xa0", " ")]
    
    while("" in data):
        data.remove("")
    
    sections += [data]

sections = [x for x in sections if x]
allSections = []

for row in range(len(sections)):
    temp = []
    if len(sections[row]) == 2 and sections[row-1][0][0:9].replace(" ", "") == "".join(courseName):
        temp += sections[row-1]
        for i in range(10):
            if(sections[row + i] != []):
                temp += sections[row + i]
    allSections += [temp]

allSections = [x for x in allSections if x]

for x in allSections:
    print(allSections)
