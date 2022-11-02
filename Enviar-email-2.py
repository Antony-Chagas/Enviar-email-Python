import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Prezados,</p>
    <p>Segue meu email</p>
    <p>Att: antony Chagas</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "email automatico"
    msg['From'] = 'antony445@gmail.com'
    msg['To'] = 'antony556@gmail.com'
    password = '123'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
