from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import smtplib

f = open('mail.json')
creds = json.load(f)

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = creds['email'] #change this to match your gmail account
recipient = "ebwinters@comcast.net"
GMAIL_PASSWORD = creds["pass"] #change this to match your gmail password
img_file = '/home/pi/pi-camera-stream-flask/static/newimage.jpg'
def send_mail():
    with open(img_file, 'rb') as f:
        img_data = f.read()
    msg = MIMEMultipart()
    msg['Subject'] = 'home security alert'
    msg['From'] = GMAIL_USERNAME
    msg['To'] = recipient
    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=img_file)
    msg.attach(image)

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    s.sendmail(GMAIL_USERNAME, recipient, msg.as_string())
    s.quit()

send_mail()
    