import smtplib

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.ehlo()
connection.starttls()

connection.login('username@gmail.com', 'your_password')

connection.sendmail('sender@gmail.com', 'recipient@gmail.com', \
        'Subject: Here is subject...\n\nDear recipient, blah\n\nSender')

connection.quit()