#!/usr/bin/env python
# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = "weatherfortoday@163.com"
password = "Kvmial99"
# 多个地址用逗号分隔，还是一个字符串传入
to_addr = "1279917365@qq.com"
smtp_server = "smtp.163.com"

with open("todayWeather.txt","r") as f:
  text = f.read()
msg = MIMEText(text, 'plain', 'utf-8')
msg['From'] = _format_addr(u'WeatherForToday <%s>' % from_addr)
msg['To'] = _format_addr(u'unknown <%s>' % to_addr)
msg['Subject'] = Header(u'今日天气早知道', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
