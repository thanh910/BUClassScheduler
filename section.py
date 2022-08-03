class section:
    
    def __init__(self, sectionName, title, instructor, credits, type, bld, room, day, start, stop, notes):
        "constructor for section class"
        self.sectionName = sectionName
        self.title = title
        self.instructor = instructor
        self.credits = credits
        self.type = type
        self.bld = bld
        self.room = room
        self.day = day
        self.start = start
        self.stop = stop
        self.notes = notes
    
    
    def __repr__(self):
        "string representation of the section"
        result = ""
        s = [self.sectionName, self.instructor, self.bld, self.room, self.day, self.start.strftime('%I:%M%p'), self.stop.strftime('%I:%M%p')]
        for string in s:
            result += str(string) + " "
        return result
    
    
    def filterSectionFrom(self, dfList):
        for df in dfList:
            #df.sections = df.sections.loc[((~df.sections['Day'].str.contains(sect.day)) & ~(sect.day in (df.sections['Day']))) | (df.sections['Start']<sect.start) | (df.sections['Start']>sect.stop)]
            df.sections = df.sections.loc[(df.sections['Days']=='Arranged') | ~((df.sections['Days'].str.contains(self.day)) | (df.sections['Days'].map(lambda x: x in self.day))) \
                | (df.sections['Stop']<self.start) | (df.sections['Start']>self.stop)]
            
    
    def isvalid(self, row):
        """ checks for overlapping times between two time objects and returns false if there is a time conflict
            and true if there is no time conflict
        """
        if self.day == "Arranged" or row.Day == "Arranged":
            return True
        
        elif self.day == row.Day:
            if self.start < row.Stop and self.stop > row.Start:
                return False
        return True
    