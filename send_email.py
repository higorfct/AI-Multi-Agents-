import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = os.getenv("EMAIL_USER")
    msg['To'] = os.getenv("EMAIL_DESTINO")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(msg['From'], os.getenv("EMAIL_PASS"))
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
