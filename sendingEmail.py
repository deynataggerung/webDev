import smtplib
from email.mime.text import MIMEText
import getpass

hostname = "smtp.gmail.com"
pswd = getpass.getpass("Password: ")
actual = "youraddress@gmail.com"
fake = "huehuehue@gmail.com"
to = "receiving@gmail.com"

payload = "Test Test Text"
msg = MIMEText(payload)

msg["Subject"] = "Phishing Test"
msg["From"] = me
msg["To"] = to

s = smtplib.SMTP_SSL(hostname, 465)
s.login(actual, password)
s.sendmail(fake, [to], msg.as_string())
s.quit()
