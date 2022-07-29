
import requests
import lxml.html as lh
import pandas as pd

import time
start_time = time.time()



semester = input("Enter a semester (ex. Fall 2022): ")
semester = semester.replace(" ", "+")

#numCourses = int(input("How many courses are you taking? "))

#allCourses = []
#for c in range(numCourses):
courseName = input("Enter a course (ex. CAS XX 123): ")


#for c in allCourses:
courseName = courseName.upper().split(" ")
if len(courseName) < 4:
    courseName += [""]

#

allCoursesDatabase = []

#for courseName in allCourses: 
#num of pages rerun
pageCount = 0
#Create empty list
col=[]  

while True:
    
    URL = "https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1658458219?ModuleName=univschr.pl&SearchOption" + \
            "Desc=Class+Number&SearchOptionCd=S&KeySem=20233&ViewSem=" + semester + \
            "&College=" + courseName[0] + "&Dept=" + courseName[1] + "&Course=" + courseName[2] + "&Section=" + courseName[3]
                    
    courseNameString = "".join(courseName)
    page = requests.get(URL)
    pageContent = lh.fromstring(page.content)
    tableElements = pageContent.xpath('//tr')

    inputValues = pageContent.xpath('//input')
    nextPageSearchInputs = [v.value for v in inputValues][1:5]


    #print([len(T) for T in tableElements]) #test for printing the width of all tables in URL

    
    i=0

    if pageCount == 0:
        
        
        #For each row, store each first element (header) and an empty list
        for t in tableElements[10]:
            i+=1
            name=t.text_content()
            #print(i,name) \\test for printing column names
            col.append([name,[]])
        

    for j in range(0,len(tableElements[11:])):
        
        #T is our j'th row
        T=tableElements[11+j]
        
        #If row is not of size 10, the //tr data is not from our table 
        if len(T)!=13:
            continue
        
        #i is the index of our column
        i=0
        
        #Iterate through each element of the row
        for t in T.iterchildren():
            data=t.text_content()
            
            #Check if row is empty
            if i>0:
            
            #Convert any numerical value to integers
                try:
                    data=int(data)
                except:
                    pass
                
            #Append the data to the empty list of the i'th column
            col[i][1].append(data)
            
            #Increment i for the next column
            i+=1
    
    #print([len(C) for (title,C) in col]) #test for printing how many number sections
        
    if nextPageSearchInputs[:3] != courseName[:3]:
        break
    else:
        courseName = nextPageSearchInputs
        pageCount += 1
    
    
#setting up a dictionary for the dataFrame
Dict = {title:column for [title,column] in col}

#print([len(C) for [title,C] in col]) #test for printing how many number sections

courseNameString = [courseName[2]]

#creating dataframe and dropping extra classes
df=pd.DataFrame(Dict)
df = df[df["Class"].str.contains("|".join(courseNameString))]
df.drop('', axis=1, inplace=True)
df.drop('OpenSeats', axis=1, inplace=True)

print(df)
print("--- %s seconds ---" % (time.time() - start_time))

