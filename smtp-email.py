import smtplib
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo() # Calls the smtp servers and keeps them in listening mode for you to interact with them
smtpObj.starttls() # Start the tls security protocol for email services
smtpObj.login('bob@example.com', 'My_secret_password') # Credentials required to send mail.
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: message \nTo alice the recipient, Bob')
smtpObj.quit()


