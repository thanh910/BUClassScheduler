# Importing the matplotlib.pyplot and other libraries
import matplotlib.pyplot as plt
import matplotlib.dates as dt
from course import *
import random

# Declaring a figure "gnt"
fig, gnt = plt.subplots(figsize=(8, 8), dpi=100)

# Setting figure title
fig.suptitle('Weekly Schedule', fontsize=20)

# Setting x-axis and y-axis limits
gnt.set_xlim(0, 100)
gnt.set_ylim(420, 1440)

#inverting y-axis and setting x-axis to the top
gnt.invert_yaxis()
gnt.xaxis.tick_top()

# Setting ticks on x-axis and y-axis
gnt.set_xticks([20, 40, 60, 80], minor=True)
gnt.set_xticks([10, 30, 50, 70, 90], major=True)
gnt.set_yticks([60*x for x in range(7, 25)])

# Labelling ticks of x-axis and y-axis
gnt.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
gnt.tick_params(axis=u'both', which=u'both',length=0)
gnt.set_yticklabels(['7:00 AM', '8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM', '11:00 PM', '12:00 AM',])
 
# Setting graph attribute
gnt.grid(which='minor')
gnt.grid(axis='y')

plt.savefig("templates/emptygraph.png")


def graph(sectionList):
    
    for section in sectionList:
        days = section.days.split(',')
        start = (section.start.hour)*60 + section.start.minute
        stop = (section.stop.hour)*60  + section.stop.minute
        dayStart = 0
        duration = 20
        
        r = random.random()
        g = random.random()
        b = random.random()
        color = (r, g, b)
        
        for weekday in days:
            if 'Mon' in weekday:
                dayStart = 0
            elif 'Tue' in weekday:
                dayStart = 20
            elif 'Wed' in weekday:
                dayStart = 40
            elif 'Thu' in weekday:
                dayStart = 60
            elif 'Fri' in weekday:
                dayStart = 80
            else:
                dayStart=0
                duration=0
            
            gnt.broken_barh([(dayStart, duration)], (start, stop-start), facecolors=color)
        
    plt.savefig('templates/graph.png')
    return fig


# gnt.broken_barh([(start_time, duration)], (lower_yaxis, height), facecolors=('tab:colours'))
