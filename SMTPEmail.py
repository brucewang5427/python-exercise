import smtplib
smtpObj=smtplib.SMTP_SSL('smtp.gmail.com',465)
smtpObj.ehlo()
smtpObj.login('cwang5315427@gmail.com','xg5315427')
smtpObj.sendmail('cwang5315427@gmail.com','brucewang5427@gmail.com',
                 'Subject: So long \nThis is just a test email, please ignor it')
smtpObj.quit()