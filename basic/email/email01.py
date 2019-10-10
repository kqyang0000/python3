from email.mime.text import MIMEText
from email.header import Header
import smtplib

subject = '放假通知'
msg = MIMEText('Hello, send by python.', 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
# 输入email地址和口令
from_addr = input('From:')
msg['From'] = from_addr
password = input('password:')
# 输入收件人地址
to_addr = input('To:')
msg['To'] = to_addr
# 输入SMTP服务器地址
smtp_server = input('SMTP server:')

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
