# 2020.1.1.Noon, by Queenie Chen
# send mail using SMTP

import smtplib

from email.mime.text import MIMEText

msg = MIMEText('the mail body is here')

msg['From'] = 'pattyappier@gmail.com'
msg['To'] = 'queeniecplusplus@gmail.com'
msg['Subject'] = 'OH SMTP !'

# 第一個參數是 hostname，第二個參數是阜號，第三個參數是逾時時間
smtpMailSender = smtplib.SMTP('localhost', 25, 100)
smtpMailSender.send_message(msg)
smtpMailSender.quit()
