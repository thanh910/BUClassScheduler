from WebScraper import *
from course import *
from IPython.display import display
from graph import *
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
""" for c in allCourses:
    display(c.sections) """


smartPriority(allCourses)

allChosen = []
for course in allCourses:
    display(course.lectures)
    print()
    
    while True:
        index = course.findIndex(str(input("Select a section: ")).upper())
        if index != None:
            chosenSection = course.pullSection(index)
            allChosen += [chosenSection]
            chosenSection.filterSectionFrom(allCourses)
            break
    
    if not course.discLabs.empty:
        display(course.discLabs)
        print()
        
        while True:
            index = course.findIndex(str(input("Select a section: ")).upper())
            if index != None:
                chosenSection = course.pullSection(index)
                allChosen += [chosenSection]
                chosenSection.filterSectionFrom(allCourses)
                break
            
            print("Section not found. Please enter a new section: ")
    

    graph(allChosen)


display(allChosen)


print("--- %s seconds ---" % (time.time() - start_time))