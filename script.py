import time
import smtplib
from email.message import EmailMessage
from urllib.request import urlopen
from course import *

url = "https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1667504839?ModuleName=univschr.pl&SearchOptionDesc=Class+Number&SearchOptionCd=S&KeySem=20234&ViewSem=Spring+2023&College=CAS&Dept=LC&Course=212&Section="
    
while True:
    #Course = course("SPRING 2023", "SAR HP 252")
    #Course2= course("SPRING 2023", "CAS LS 309")
    Course3= course("SPRING 2023", "CAS LC 212")
    #Course4= course("SPRING 2023", "SED DE 384")
    Course5= course("SPRING 2023", "SAR HS 201")

    try:
        #Section1 = Course.pullSection(Course.findIndex("A1"))
        #Section12 = Course.pullSection(Course.findIndex("B3"))
        #Section2 = Course2.pullSection(Course2.findIndex("A1"))
        Section3 = Course3.pullSection(Course3.findIndex("B1"))
        #Section4 = Course4.pullSection(Course4.findIndex("A1"))
        Section5 = Course5.pullSection(Course5.findIndex("A2"))
        
        
        """ if Section1.openseats > 0 or Section12.openseats > 0:
            msg = EmailMessage()
            msg.set_content(url)
            msg['From'] = 'autowongbot@gmail.com'
            msg['To'] = 'jiehoonn@bu.edu'
            msg['Subject'] = 'Open Seat Count Update SAR HP 252'
            fromaddr = 'autowongbot@gmail.com'
            toaddrs = ['jiehoonn@bu.edu']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('autowongbot@gmail.com', 'rttymsdwseggqyrf')
            server.send_message(msg)
            server.quit()
            response = urlopen(url).read()
            print("success SAR HP 252")
            continue"""
        
        """if Section2.openseats > 0:
            msg = EmailMessage()
            msg.set_content(url)
            msg['From'] = 'autowongbot@gmail.com'
            msg['To'] = 'dlaboy@bu.edu'
            msg['Subject'] = 'Open Seat Count Update LS 309'
            fromaddr = 'autowongbot@gmail.com'
            toaddrs = ['dlaboy@bu.edu']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('autowongbot@gmail.com', 'rttymsdwseggqyrf')
            server.send_message(msg)
            server.quit()
            response = urlopen(url).read()
            print("success CAS LS 309")"""
        
        if Section3.openseats > 0:
            msg = EmailMessage()
            msg.set_content(url)
            msg['From'] = 'autowongbot@gmail.com'
            msg['To'] = 'thanh910@bu.edu'
            msg['Subject'] = 'Open Seat Count Update LC 212'
            fromaddr = 'autowongbot@gmail.com'
            toaddrs = ['thanh910@bu.edu']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('autowongbot@gmail.com', 'rttymsdwseggqyrf')
            server.send_message(msg)
            server.quit()
            response = urlopen(url).read()
            print("success CAS LC 212")
        
        """if Section4.openseats > 0:
            msg = EmailMessage()
            msg.set_content(url)
            msg['From'] = 'autowongbot@gmail.com'
            msg['To'] = 'rlove@bu.edu'
            msg['Subject'] = 'Open Seat Count Update DE 384'
            fromaddr = 'autowongbot@gmail.com'
            toaddrs = ['rlove@bu.edu']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('autowongbot@gmail.com', 'rttymsdwseggqyrf')
            server.send_message(msg)
            server.quit()
            response = urlopen(url).read()
            print("success SED DE 384")"""
        
        if Section5.openseats > 0:
            msg = EmailMessage()
            msg.set_content(url)
            msg['From'] = 'autowongbot@gmail.com'
            msg['To'] = 'thanh910@bu.edu'
            msg['Subject'] = 'Open Seat Count Update SAR HS 201'
            fromaddr = 'autowongbot@gmail.com'
            toaddrs = ['thanh910@bu.edu']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('autowongbot@gmail.com', 'rttymsdwseggqyrf')
            server.send_message(msg)
            server.quit()
            response = urlopen(url).read()
            print("success SAR HS 201")
        
        time.sleep(30)
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
        
    time.sleep(30)

