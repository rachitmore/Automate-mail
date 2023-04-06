import logging
import time
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


logging.basicConfig(filename="maillog",
                    format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)


class automail:
    def autosender(self,email,subject,body,email_id,password,attachment):
        a = attachment
        port = 587  
        smtp_server = "smtp.gmail.com"
        sender_email = "rachitmore3@gmail.com" 
        password = "umfmqgpvsjzqxlzi"
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject
        body = body

        msg.attach(MIMEText(body, 'plain'))

        a.save(a.filename)
        attachment = open("Rachit_More_Resume.pdf", "rb")
        filename = a.name

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        encoders.encode_base64(p)
        msg.attach(p)

        
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo() 
            server.starttls(context=context)
            server.ehlo() 
            server.login(sender_email, password)
            server.sendmail(sender_email,email, msg.as_string())
            server.quit()
            time.sleep(5)

        logging.info("Mail Sent")

