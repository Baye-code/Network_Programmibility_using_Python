from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import email.message

email_content = """
<!DOCTYPE html>
<html>
<title>HTML Tutorial</title>
<body style="background-color:powderblue;">

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>

"""

msg = email.message.Message

message = "This is the beautiful scene"

sender_password = "L@m$abarane521997"
msg['To'] = "serignelam05@gmail.com"
msg['From'] = "bayesabarane@gmail.com"
msg['Subject'] = "My web page"

msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], sender_password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("Successfully sent email with image to %s" %(msg['To']))