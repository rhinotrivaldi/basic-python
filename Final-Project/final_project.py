#sebelumnya dilakukan setting less secure app pada gmail pengirim

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email_sender = str(input("Masukan Email Pengirim: "))
password_sender = str(input("Masukan Password Pengirim: "))

#Membuka daftar penerima dan dijadikan list
my_list = open("receiver_list.txt", "r")
email = my_list.readlines()
email_list = []
for i in email:
    email_list.append(i.strip("\n"))

receiver = email_list #email list
print(receiver)


subject = 'Contoh Subject' #Bisa di custom dengan memanfaatan input()
message = 'Contoh Pesan' #Bisa di custom dengan memanfaatan input()

file_location = 'C:\\Users\\RHINO\\Documents\\Final-Project\\attach.txt' #lokasi file yang akan dikirim | ganti sesuai lokasi file

# Membuat lampiran file yang akan dikirim
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# koneksi ke server dengan port 587 gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_sender, password_sender)

# Kirim email sesuai dengan jumlah list email (looping)
for list_receiver in receiver:

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = list_receiver
    msg['Subject'] = subject

    #pesan sebagai obj
    msg.attach(MIMEText(message, 'plain'))
    #melampirkan fle
    msg.attach(part)

    #Mengirim email berdasarkan email
    server.sendmail(email_sender, list_receiver, msg.as_string()) 

# keluar server setelah selesai
server.quit()

