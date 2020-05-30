
import smtplib
sender_email="minshudwarika@gmail.com"
rec_email="minshunitrkl@gmail.com"
password="resonance"
message="hey ,Desired accuracy is not received in this particular epoch "
server=smtplib.SMTP("smtp.gmail.com",587) 
server.starttls()
server.login(sender_email,password)
print("Login success")
server.sendmail(sender_email,rec_email,message)
