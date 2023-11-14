import smtplib
import ssl,os
from dotenv import load_dotenv

load_dotenv()

port = 465
host = "smtp.gmail.com"

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
to_email = email

context = ssl.create_default_context()


def send_mail(message):
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(email, password)
        print("sending mail..")
        server.sendmail(from_addr=email,to_addrs=to_email,msg=message)
        print("sent mail..")

