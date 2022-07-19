#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Section:
    
    def __init__(self, section, instructor, ctype, location, time, status):
        self.section = section
        self.instructor = instructor
        self.ctype = ctype
        self.location = location
        self.time = time
        self.status = status
  
    
    
    def __repr__(self):
        return "" + self.section + " " + self.instructor + " " + \
            self.ctype + " " + self.location + " " + self.time + " " + self.status
            
    def __eq__(self, other):
        if self.section == other.section and self.intstructor == other.instructor and \
            self.ctype == other.ctype and self.location == other.location and self.time == other.time and \
                self.status == other.status:
                    return True
        return False
            
    