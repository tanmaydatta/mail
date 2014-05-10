import smtplib
from smtplib import SMTP
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

print 'Enter Gmail Id'
gmail_user=str(raw_input())
gmail_pwd = getpass.getpass("Enter your password:")
print "TO"
to = str(raw_input())
# smtpserver = smtplib.SMTP('smtp.gmail.com',587)
# smtpserver = smtplib.SMTP('smtp.gmail.com:587')
print "Enter Subject"
subject=str(raw_input())
print "Enter Message"
Msg=str(raw_input())
smtpserver = SMTP()
smtpserver.connect('smtp.gmail.com',587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + subject+'\n'
msg = header + '\n '+Msg+'\n\n'
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()

