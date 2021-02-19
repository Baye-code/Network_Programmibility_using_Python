import smtplib
# https://myaccount.google.com/lesssecureapps

message_content = "Hello from python. This is a test"
sender_email = "bayesabarane@gmail.com"
sender_password = "L@m$abarane521997"
receiver_email = "oudiopisidk@groupeisi.com"

#Connecting and testing the server
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()

#Start TLS
mail.starttls()

#Login
mail.login(sender_email, sender_password)

#Sending message
mail.sendmail(sender_email, receiver_email, message_content)

