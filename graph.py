# Importing the matplotlib.pyplot
import matplotlib.pyplot as plt

# Declaring a figure "gnt"
fig, gnt = plt.subplots()

# Setting Y-axis limits
gnt.set_ylim(0, 70)

# Setting X-axis limits
gnt.set_xlim(8, 20)

# Setting labels for x-axis and y-axis
gnt.set_xlabel('time')
gnt.set_ylabel('days of the week')

# Setting ticks on y-axis
gnt.set_yticks([15, 25, 35, 45, 55])
# Labelling tickes of y-axis
gnt.set_yticklabels(['Fri', 'Thurs', 'Wed', 'Tues', 'Mon'])

# Setting graph attribute
gnt.grid(True)


# Declaring a bar in schedule

# gnt.broken_barh([(start_time, duration)], (lower_yaxis, height), facecolors=('tab:colours'))

gnt.broken_barh([(9, 2)], (50, 10), facecolors =('tab:orange'))

gnt.broken_barh([(9, 2)], (30, 10), facecolors =('tab:orange'))

gnt.broken_barh([(9, 2)], (10, 10), facecolors =('tab:orange'))

gnt.broken_barh([(11.5, 2)], (40, 10), facecolors =('tab:red'))

gnt.broken_barh([(11.5, 2)], (20, 10), facecolors =('tab:red'))

plt.savefig("gantt1.png")
