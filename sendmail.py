import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user='pythonweekday22@gmail.com'
email_send='pythonweekday22@gmail.com'
subject="Mail from Python"

msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_send
msg['Subject']=subject

body="""Hi there,
 This is a mail received from python program!
 
 Thanks,
 Ericcson Team."""
msg.attach(MIMEText(body,'plain'))

filename='myfile.txt'
attachment=open(filename,'r')
part=MIMEBase('applicaiton','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment", filename="MyFirstFile.txt")

msg.attach(part)
text=msg.as_string()
servers=smtplib.SMTP('smtp.gmail.com',587)
servers.starttls()
servers.login(email_user,'Funnypass@123')

servers.sendmail(email_user,email_send,text)
servers.quit()

