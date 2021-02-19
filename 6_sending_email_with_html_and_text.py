from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

text_content = """
 Hello there,
 this is a sample webpage.
 -Baye
"""

html_content = """
<!DOCTYPE html>
<html>
<title>HTML Tutorial</title>
<body style="background-color:powderblue;">

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>

"""

msg = MIMEMultipart("alternative")

sender_password = "L@m$abarane521997"

msg['To'] = "serignelam05@gmail.com"
msg['From'] = "bayesabarane@gmail.com"
msg['Subject'] = "Sample web page"

part1 = MIMEText(text_content, "plain")
part2 = MIMEText(html_content, "html")

msg.attach(part1)
msg.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	server.login(msg['From'], sender_password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())

print("Successfully sent email with image to %s" %(msg['To']))

