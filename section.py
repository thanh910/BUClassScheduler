class section:
    
    def __init__(self, sectionName, title, instructor, credits, type, bld, room, days, start, stop, notes):
        "constructor for section class"
        self.sectionName = sectionName
        self.title = title
        self.instructor = instructor
        self.credits = credits
        self.type = type
        self.bld = bld
        self.room = room
        self.days = days
        self.start = start
        self.stop = stop
        self.notes = notes    
    
    
    def __repr__(self):
        "string representation of the section"
        result = ""
        s = [self.sectionName, self.instructor, self.bld, self.room, self.days, self.start.strftime('%I:%M%p'), self.stop.strftime('%I:%M%p')]
        for string in s:
            result += str(string) + " "
        return result
    
    
    def filterSectionFrom(self, dfList):
        for df in dfList:
            #df.sections = df.sections.loc[(df.sections['Days']=='Arranged') | ~((df.sections['Days'].str.contains(self.day)) | (df.sections['Days'].map(lambda x: x in self.day))) \
                #| (df.sections['Stop']<self.start) | (df.sections['Start']>self.stop)]
                
            df.sections = df.sections.loc[self.filterDay(df) | self.filterTime(df)]
            
            
    def filterDay(self, df):
        return ~df.sections['Days'].map(lambda x: x in self.days or self.days in x or x == 'Arranged')
    
    
    def filterTime(self, df):
        return ((df.sections['Stop']<self.start) | (df.sections['Start']>self.stop))
    