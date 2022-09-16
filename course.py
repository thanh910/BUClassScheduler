from WebScraper import *
from collections.abc import Iterable
from section import *

class course:
    
    def __init__(self, semester, courseName):
        self.title = courseName
        self.courseName = courseName.upper()
        self.sections = Webscraper(semester, self.courseName)
        self.title = self.sections['Title'].iloc[0]
        self.numSections = self.sections.shape[0]
        self.lectures = self.sections[self.sections["Type"].str.contains("Lecture")]
        self.numLectures = self.lectures.shape[0]
        self.discLabs = self.sections[~(self.sections["Type"].str.contains("Lecture"))]
        self.numDiscLabs = self.discLabs.shape[0]
        self.credits = self.sections['Credits'].max()
        self.instructors = self.lectures["Instructor"].unique()
    
        
    def __eq__(self, other):
        if not isinstance(other, course):
                # don't attempt to compare against unrelated object types
                return NotImplemented
        return deep_equals(self, other)
    
    
    def __repr__(self):
        #represents a course object in the form of a string containing course name, title, and credits
        strings = [self.courseName, self.title, self.credits, "Credits"]
        result = ""
        
        for i in strings:
            result += i + " "
        
        return result.strip()
    
    def findIndex(self, string):
        indexes = self.sections.index.tolist()
        for x in indexes:
            if string in x:
                return x
            
        return None

    def pullSection(self, index):
        return section(index, *self.sections.loc[index].values.tolist())



#non-instance helper methods
def generateCourses(list, semester):
    result = []
    for i in list:
        if i != "":
            result += [course(semester, i)]

    return result


def smartPriority(list):
    list.sort(key=lambda x: x.numSections)
    return list



#comparison function for comparing complex objects
BASE_TYPES = [str, int, float, bool, type(None)]


def base_typed(obj):
    """Recursive reflection method to convert any object property into a comparable form.
    """
    T = type(obj)
    from_numpy = T.__module__ == 'numpy'

    if T in BASE_TYPES or callable(obj) or (from_numpy and not isinstance(T, Iterable)):
        return obj

    if isinstance(obj, Iterable):
        base_items = [base_typed(item) for item in obj]
        return base_items if from_numpy else T(base_items)

    d = obj if T is dict else obj.__dict__

    return {k: base_typed(v) for k, v in d.items()}


def deep_equals(*args):
    return all(base_typed(args[0]) == base_typed(other) for other in args[1:])









    
    
