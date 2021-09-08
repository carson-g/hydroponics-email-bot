import smtplib
import grove_ph_sensor
import time

#Variables
server = 'smtp.gmail.com'
gmail_user = 'hydrohomiebot@gmail.com'
gmail_pass = 'hydro_pass'
port = 587
sendTo = 'carson@garnergalaxy.com'
emailSubject = "Hey, this is a HydroHomie update."

class Emailer:
    def sendmail(self, recipient, subject, content):
        headers = ["From: " + gmail_user, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect
        connection = smtplib.SMTP(server, port)
        connection.ehlo()
        connection.starttls()
        connection.ehlo()

        #Login
        connection.login(gmail_user, gmail_pass)

        #Send
        connection.sendmail(gmail_user, recipient, headers + "\r\n\r\n" + content)
        connection.quit()

sender = Emailer()

while True:
    #Gather input pH information
    try:
        phInput = grove_ph_sensor.ph
        emailContent = "Your water's pH level was measured to be " + str(phInput) + " this morning. Have a good day!"
    except:
        emailContent = "Something seems to have gone wrong. Check out the Raspberry Pi & sensor today!"

    #Send mail
    sender.sendmail(sendTo, emailSubject, emailContent)

    #Loop every 24 hours
    time.sleep(86400)
