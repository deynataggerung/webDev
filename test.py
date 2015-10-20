hostname = "smtp.gmail.com"
password = "MicahP45"
me = "delightsofrussia@gmail.com"
to = "harmoncomputerservices@gmail.com"

import smtplib
from email.mime.text import MIMEText

payload = "Test Test Text"
msg = MIMEText(payload)

msg["Subject"] = "Phishing Test"
msg["From"] = me
msg["To"] = to

s = smtplib.SMTP_SSL(hostname, 465)
s.login(me, password)
s.sendmail(me, [to], msg.as_string())
s.quit()
