import smtplib
from email.mime.text import MIMEText

def send_email(recipient_email, crypto, current_price):
    sender_email = "sagarreddy.ragoor@gmail.com"
    sender_password = "sagar"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, sender_password)

    subject = f"Price Alert: {crypto}"
    body = f"The price of {crypto} has reached ${current_price}!"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    server.send_message(msg)
    server.quit()
