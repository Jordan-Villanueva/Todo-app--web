import smtplib

def send_email(msg):
    FROMADDR = "veredis.educacion@gmail.com"
    LOGIN = FROMADDR
    PASSWORD = "jsow tyct bvdq hdch"
    TOADDRS = ["veredis.educacion@gmail.com"]
    SUBJECT = "Test"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)
    server.sendmail(FROMADDR, TOADDRS, msg)
    server.quit()



'''
# -*- coding: utf-8 -*-
import smtplib
import ssl

host = "smpt.gmail.com"
port = 465

username = "veredis.educacion@gmail.com"
password = "jsow tyct bvdq hdch "

receiver = "veredis.educacion@gmail.com"
context = ssl.create_default_context()

message = "Hello, bye"
server = smtplib.SMTP('smtp.gmail.com', 587)
with smtplib.SMTP_SSL(host, port, context = context) as server:
    server.login(username,password)
    server.sendmail(username, receiver, message)


import smtplib

FROMADDR = "veredis.educacion@gmail.com"
LOGIN    = FROMADDR
# PASSWORD = "Usbw631#"
TOADDRS  = ["veredis.educacion@gmail.com"]
SUBJECT  = "Test"

msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
msg += "some text\r\n"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg)
server.quit()
'''