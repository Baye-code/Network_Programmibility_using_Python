from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

msg = MIMEMultipart()

message = "This is the beautiful scene"

sender_password = "L@m$abarane521997"
msg['To'] = "serignelam05@gmail.com"
msg['From'] = "bayesabarane@gmail.com"
msg['Subject'] = "Subscription"

img = 'Blue.jpg'
fp = open(img, 'rb')
img_attach = MIMEImage(fp.read())
fp.close()
msg.attach(img_attach)

msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(msg['From'], sender_password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("Successfully sent email with image to %s" %(msg['To']))