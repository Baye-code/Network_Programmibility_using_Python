from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()

message = "Welcome to my email Client"
sender_password = "L@m$abarane521997"

msg['To'] = "serignelam05@gmail.com"
msg['From'] = "bayesabarane@gmail.com"
msg['Subject'] = "Subscription"

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(msg['From'], sender_password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("Successfully sent email to %s" %(msg['To']))