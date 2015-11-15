import smtplib
import getpass
import argparse
from email import message

parser = agparse.ArgumentParser(description='Process the email address')
parser.add_argument('-f')
args = parser.parse_args()
print args

hostname = "smtp.mail.com"
pswd = getpass.getpass("Password: ")
actual = "original@mail.com"
fake = "me@spencer.sx"
to = "target@gmail.com"

m1 = message.Message()
m1.add_header("from", fake)
m1.add_header("to", to)
m1.add_header("subject", "Phishing Test")
m1.set_payload("Test Test Test")

s = smtplib.SMTP_SSL(hostname, 465)
s.login(actual, pswd)
s.sendmail(actual, [to], m1.as_string())
s.quit()
