import smtplib 
from dotenv import load_dotenv
import os

def send_email(subject, body, to_email):
    
    try: 
        #Create your SMTP session 
        smtp = smtplib.SMTP('smtp.gmail.com', 587) 

    #Use TLS to add security 
        smtp.starttls() 

        load_dotenv()
        password = os.getenv("PASSWORD")
        #User Authentication 
        smtp.login("jobsmailaus@gmail.com", password)

        #Defining The Message 
        message = "Wyd" 

        #Sending the Email
        smtp.sendmail("jobsmailaus@gmail.com", "pnasrwork@gmail.com",message) 

        #Terminating the session 
        smtp.quit() 
        print ("Email sent successfully!") 

    except Exception as ex: 
        print("Something went wrong....",ex)