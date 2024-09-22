import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'saikrishna@gmail.com'
email_passwd = 'yzmga fiki pksr cbmm'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='satishbathula9999@gmail.com', msg="Sent from my IDE. Hehe")
connection.close()
print('Mail sent successfully')
