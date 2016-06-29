#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line

from socket import socket
from email.mime.text import MIMEText
import smtplib

msg = MIMEText("Hello, I am a human, no robot.", 'plain', 'utf-8')
from_addr = "466105758@qq.com"
password = "iqajsalyzthlbgij"

to_addr = "zhouhua2297@yeah.com"
smtp_server = "smtp.qq.com"

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()