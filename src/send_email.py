from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib 
from dotenv import load_dotenv
from datetime import datetime
import os

def send_email(to_email):
    
    try: 
        results_file = "./results/" + datetime.now().strftime("%d-%m-%Y") + ".csv"

        smtp = smtplib.SMTP('smtp.gmail.com', 587) 
 
        smtp.starttls() 

        load_dotenv()
        password = os.getenv("PASSWORD")
        #User Authentication 
        smtp.login("jobsmailaus@gmail.com", password)

        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        
        msg = MIMEMultipart()
        msg['From'] = "jobsmailaus@gmail.com"
        msg['To'] = "pnasrwork@gmail.com"
        msg['Subject'] = "Test Email"

        with open(results_file, 'r') as file:
            file_content = file.read()
        
        name = "Patrick"
        # Now, use name, date_time, and file_content to compose your email body
        body = f"Hello {name}, nothing to see here as at {date_time}. Here's the file content:\n{file_content}"

        msg.attach(MIMEText(body, 'plain'))

        smtp.sendmail("jobsmailaus@gmail.com", "pnasrwork@gmail.com",msg.as_string()) 

        smtp.quit() 
        print ("Email sent successfully!") 

    except Exception as ex: 
        print("Something went wrong....",ex)