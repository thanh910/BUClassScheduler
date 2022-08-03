from WebScraper import *
from course import *
from IPython.display import display

import time
start_time = time.time()

#semester = input("Enter a semester (ex. Fall 2022): ")
semester = 'FALL 2022'
numCourses = int(input("How many courses are you taking? "))

courseList = []
for i in range(numCourses):
    courseList += [str(input("Enter a course (ex. CAS XX 123): "))]

allCourses = generateCourses(courseList, semester)

#print test for all courses entered
for c in allCourses:
    display(c.sections)


smartPriority(allCourses)

allChosen = []
for course in allCourses:
    display(course.sections)
    print()
    
    while True:
        index = course.findIndex(str(input("Select a section: ")).upper())
        if index != None:
            chosenSection = course.pullSection(index)
            break
        
        print("Section not found. Please enter a new section: ")
    
    allChosen += [chosenSection]
    chosenSection.filterSectionFrom(allCourses)
    #print(*allCourses)
    display(chosenSection)

display(allChosen)


    
    


print("--- %s seconds ---" % (time.time() - start_time))