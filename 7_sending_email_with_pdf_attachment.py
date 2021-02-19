from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart("alternative")

sender_password = "L@m$abarane521997"

msg['To'] = "serignelam05@gmail.com"
msg['From'] = "bayesabarane@gmail.com"
msg['Subject'] = "The document you requested"
msg['body'] = "Hello sir, I have attached the document you requested"

msg.attach(MIMEText(msg['body'], "plain"))
my_essay = "test.pdf"

with open(my_essay, "rb") as attachment:
	part = MIMEBase("application", "octet-stream")
	part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment ; filename = {my_essay}",)
msg.attach(part)


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	server.login(msg['From'], sender_password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())

print("Successfully sent email with image to %s" %(msg['To']))

