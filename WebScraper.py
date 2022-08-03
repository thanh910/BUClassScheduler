
from ssl import DefaultVerifyPaths
import requests
import lxml.html as lh
import pandas as pd
import re
from datetime import datetime

pd.options.display.max_columns = None
pd.options.display.width = None
pd.options.display.max_rows=None


def Webscraper(semester, courseName):
    # takes semester and course name as inputs and returns a dataframe 
    # with info on all sections of the course from BU Student Link
    
    semester = semester.replace(" ", "+")
    courseName = courseName.split(" ")
    title = ""
    
    if len(courseName) < 4:
        courseName += [""]

    #num of pages rerun
    pageCount = 0
    
    #Create empty list to store column data
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
                data=t.text_content().strip()
                
                #Check if row is empty
                if i>0:
                
                #Convert any numerical value to integers
                    try:
                        data=int(data)
                    except:
                        pass
                
                #separates Title/Instructor string
                if i == 2:
                    if str(data) != "":
                        temp = re.sub( r"([A-Z])", r" \1", str(data)).split()
                        data = [" ".join(temp[:-1]), temp[-1]]
                    
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
    
    #separating title and instructor into two columms
    base = pd.DataFrame(df['Title/Instructor'].values.tolist()).iloc[:, [0, 1]]
    base = base.rename(index = lambda x: x + 1)
    df[['Title/Instructor', 'Instructor']] = base
    df = df.rename({'Title/Instructor': 'Title'}, axis=1)
    df = df.rename({'Day': 'Days'}, axis=1)
    
 
    
    #deleting unneccessary columns
    df.drop('', axis=1, inplace=True)
    df.drop('OpenSeats', axis=1, inplace=True)
    
    #reassigning display order
    df = df[['Class', 'Title', 'Instructor', 'CrHrs', 'Type', 'Bld', 'Room', 'Days', 'Start', 'Stop', 'Notes']]
    df['Start'] = df['Start'].map(lambda x: convertToTime(x))
    df['Stop'] = df['Stop'].map(lambda x: convertToTime(x))
    df.set_index('Class', inplace=True)
    
    return df



#helper methods

def convertToTime(entry):
    #helper function for converting time column of dataframe to datetime objects
    if entry != "":
        return datetime.strptime(entry,"%I:%M%p").time()
    else:
        return None
    






