import smtplib
import ssl



def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "patilmihir9588@gmail.com"
    password = "xplnkbupijisicox"

    receiver = "patilmihir958@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server :
        server.login(username, password)
        server.sendmail(username, receiver, message)
