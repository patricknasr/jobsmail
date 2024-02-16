from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib 
from dotenv import load_dotenv
from datetime import datetime
import os

def send_email(to_email):
    
    try: 
        #Create your SMTP session 
        smtp = smtplib.SMTP('smtp.gmail.com', 587) 

    #Use TLS to add security 
        smtp.starttls() 

        load_dotenv()
        password = os.getenv("PASSWORD")
        #User Authentication 
        smtp.login("jobsmailaus@gmail.com", password)

        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        
        name = 'Patrick'
        
        msg = MIMEMultipart()
        msg['From'] = "jobsmailaus@gmail.com"
        msg['To'] = "pnasrwork@gmail.com"
        msg['Subject'] = "Test Email"

        # Email body
        body = f"Hello {name}, greeting from {date_time}."
        msg.attach(MIMEText(body, 'plain'))

        #Sending the Email
        smtp.sendmail("jobsmailaus@gmail.com", "pnasrwork@gmail.com",msg.as_string()) 

        #Terminating the session 
        smtp.quit() 
        print ("Email sent successfully!") 

    except Exception as ex: 
        print("Something went wrong....",ex)