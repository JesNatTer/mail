import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'jessenterblanche@gmail.com'
receiver_email_id = ['jeandreross@gmail.com', 'abdullah.isaacs@gmail.com', 'jessenterblanche@gmail.com']
password = input("Password: ")

s.starttls()

s.login(sender_email_id, password)

message = "Subject: Greeting.\n""Testing python email\n"
message = message + "testing python email 2"

s.sendmail(sender_email_id, receiver_email_id, message)

s.quit()
