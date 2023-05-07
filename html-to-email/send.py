# coding: UTF-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(mail_host, mail_from, mail_to, msg):
	smtp = smtplib.SMTP()
	smtp.connect(mail_host)
	smtp.login(mail_from, "xxxxxxxxxxx")  # Sender Account and Authorization Code
	try:
		smtp.sendmail(mail_from, mail_to, msg.as_string())
		print("successfully")
	except smtplib.SMTPException:
		print("failed to send")
	finally:
		smtp.quit()

def get_massage(mail_from, mail_to):
	msg = MIMEMultipart('alternative')
	msg["From"] = mail_from
	msg["To"] = ";".join(mail_to)
	msg['Subject'] = r"Test Email"
	content = MIMEText(get_html(), 'html', 'UTF-8')
	msg.attach(content)
	return msg


def get_html():
	file_path = './html-to-Email/html.html'
	with open(file_path, 'r', encoding='utf-8') as f:
		return f.read()


if __name__ == "__main__":
	mail_host = "smtp.qq.com"
	mail_from = '123456789@qq.com'
	mail_to = ['xxxxxxx@xxxxxxx.com']
	msg = get_massage(mail_from, mail_to)
	send_mail(mail_host, mail_from, mail_to, msg)



