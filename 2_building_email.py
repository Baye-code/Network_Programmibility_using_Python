import email.message, email.policy, email.utils, sys

text = """" Hi there,
This is a basic email frome joe.
-Joe"""

def mailer():
	message = email.message.EmailMessage(email.policy.SMTP)
	message['To'] = "serignelam05@gmail.com"
	message['From'] = "bayesabarane@gmail.com"
	message['Subject'] = "Welcome Here"
	message['Date'] = email.utils.formatdate(localtime = True)
	message['message-ID'] = email.utils.make_msgid()
	message.set_content(text)

	print(message.as_bytes())


if __name__ == '__main__':
	mailer()