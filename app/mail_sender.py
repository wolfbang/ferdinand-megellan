#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mail_sender.py
# @Author: lucas
# @Date  : 12/28/18
# @Desc  :


import smtplib
from datetime import datetime
import uuid

from email.mime.text import MIMEText

mailto_list = ['some email address']
mailto_list_bcc = ['some mail address']
mail_host = "mail host"  # set mail server
mail_user = "your username"  # set from_user nanme
mail_pass = "your password"  # password
mail_postfix = "163.com"  # postfix of your mail service provider


def send_mail(to_list, sub, content):
    me = "captain" + "<" + mail_user + "@" + mail_postfix + ">"

    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    msg['Bcc'] = ";".join(mailto_list_bcc)

    mail_to_list = mailto_list + mailto_list_bcc

    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, mail_to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    now_datetime = datetime.now()
    now_datetime_str = now_datetime.strftime(u'%Y-%m-%d %H:%M:%S')
    uuid_str = str(uuid.uuid1())

    subject = u'Are you hungry? Time:' + now_datetime_str
    content = u'''Are you hungry?\nI'm Robot and my name is Jarvis!\n''' \
              + u'\n\n\nWhat do you eat today？Make Love,Not War...' \
              + u'\nToday is:' + now_datetime_str + u'\n\n@random:' + uuid_str

    if send_mail(mailto_list, subject, content):
        print u'send successfully!'
    else:
        print u'send failed!'
