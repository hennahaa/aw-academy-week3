import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

server.login("kayttajanimi", "salasana")

fromaddr = "lahettaja" #gmail.com osoite
toaddr = "vastaanottaja" #mikä tahansa muu sähköpostiosoite
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python Email!"

body = "Hello World"
msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)