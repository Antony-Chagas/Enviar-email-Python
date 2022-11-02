import smtplib

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = "587"
login = "antony@gmail.com"
senha = "123"

sever = smtplib.SMTP(host,port)

sever.ehlo()
sever.starttls()
sever.login(login,senha)

corpo = " <p>Boa noite </p> " "<p>Segue o email automatico</p>"

email_msg = MIMEMultipart()
email_msg['from'] = login
email_msg['To'] = "antony.tiago556@gmail.com"
email_msg['Subject'] = "Meu e-mail envido"
email_msg.attach(MIMEText(corpo,'html'))

sever.sendmail(email_msg['from'],email_msg['To'],email_msg.as_string( ))

sever.quit()
 