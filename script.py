import time
import smtplib
from email.message import EmailMessage
from urllib.request import urlopen
from course import *

while True:
    url = "https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1667504839?ModuleName=univschr.pl&SearchOptionDesc=Class+Number&SearchOptionCd=S&KeySem=20234&ViewSem=Spring+2023&College=CAS&Dept=LC&Course=212&Section="
    prevCourse = course("SPRING 2023", "CAS CS 330")
    prevCourse2= course("SPRING 2023", "CAS CS 411")
    time.sleep(55)
    newCourse = course("SPRING 2023", "CAS CS 330")
    newCourse2= course("SPRING 2023", "CAS CS 411")

    try:
        prevSection = prevCourse.pullSection(prevCourse.findIndex("A1"))
        newSection = newCourse.pullSection(newCourse.findIndex("A1"))
        
        prevSection2 = prevCourse2.pullSection(prevCourse2.findIndex("A1"))
        newSection2 = newCourse2.pullSection(newCourse2.findIndex("A1"))
        

        if prevSection.openseats == newSection.openseats and prevSection2.openseats == newSection2.openseats:
            continue
        
        else:
                msg = EmailMessage()
                msg.set_content(url)
                msg['From'] = 'autowongbot@gmail.com'
                msg['To'] = 'thanh910@bu.edu'
                msg['Subject'] = 'Open Seat Count Update'
                fromaddr = 'autowongbot@gmail.com'
                toaddrs = ['thanh910@bu.edu']
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login('autowongbot@gmail.com', 'rttymsdwseggqyrf')
                server.send_message(msg)
                server.quit()
                response = urlopen(url).read()
                print("success")
                continue
            
    except Exception as e:

        print("fail")
        msg = EmailMessage()
        msg.set_content(url)
        msg['From'] = 'autowongbot@gmail.com'
        msg['To'] = 'thanh910@bu.edu'
        msg['Subject'] = 'PROGRAM FAILURE'
        fromaddr = 'autowongbot@gmail.com'
        toaddrs = ['thanh910@bu.edu']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('autowongbot@gmail.com', 'rttymsdwseggqyrf')
        server.send_message(msg)
        server.quit()

