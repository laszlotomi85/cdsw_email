import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart("related")
message["Subject"] = "Greetings from Python on ODL!"
message["From"] = "<any sender email address you'd like>"
message["To"] = "<receiver email address>"

message.attach(MIMEText("Hello, this is my email text."))

with smtplib.SMTP("10.119.25.8", 25) as server:
    server.sendmail(
        message["From"], message["To"], message.as_string()
    )
    server.quit()