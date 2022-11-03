import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen
from course import *

while True:
    url = "https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1667504839?ModuleName=univschr.pl&SearchOptionDesc=Class+Number&SearchOptionCd=S&KeySem=20234&ViewSem=Spring+2023&College=CAS&Dept=LC&Course=212&Section="
    prevCourse = course("SPRING 2023", "CAS LC 212")
    time.sleep(60)
    newCourse = course("SPRING 2023", "CAS LC 212")

    try:
        prevSection = prevCourse.pullSection("B1")
        newSection = newCourse.pullSection("B1")
        

        if prevSection == newSection:
            continue
        
        else:
                msg = EmailMessage()
                msg.set_content()
                msg['From'] = 'sirwingwong@gmail.com'
                msg['To'] = 'thanh910@bu.edu'
                msg['Subject'] = 'Open Seat Count Update'
                fromaddr = 'sirwingwong@gmail.com'
                toaddrs = ['thanh910@bu.edu']
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login('sirwingwong@gmail.com', 'Thanh2003')
                server.send_message(msg)
                server.quit()
                response = urlopen(url).read()
                currentHash = hashlib.sha224(response).hexdigest()
                time.sleep(240)
                continue
            
    except Exception as e:

        msg = EmailMessage()
        msg.set_content(url)
        msg['From'] = 'sirwingwong@gmail.com'
        msg['To'] = 'thanh910@bu.edu'
        msg['Subject'] = 'PROGRAM FAILURE'
        fromaddr = 'sirwingwong@gmail.com'
        toaddrs = ['thanh910@bu.edu']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('sirwingwong@gmail.com', 'Thanh2003')
        server.send_message(msg)
        server.quit()

