#2. Ajasta Health check CRON jobia (tehtävä 6) käyttäen siten, että se lähettää palvelimelle pyynnön 15sec välein.
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#otettu External IP pois ja laitettu tilalle example.com
r = requests.get("http://example.com/health.html")

print("Status:", r.status_code)

if r.status_code == 200:
  print("Kaikki on ok!")
else:
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
  msg['Subject'] = "Houston, we have a problem!"

  body = "Healthcheck ei mennyt läpi, jotain on pielessä."
  msg.attach(MIMEText(body, 'plain'))

  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)