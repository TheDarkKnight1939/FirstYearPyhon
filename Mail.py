import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("rahulav12@gmail.com", "")
 
msg = "YOUR MESSAGE!"
server.sendmail("rahulav12@gmail.com", "rahulav12@gmail.com", msg)
server.quit()	