import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from settings import (MAIL_HOST, MAIL_PASS, MAIL_USER, MAIL_PORT)


class SendMail:
    def __init__(self):
        self.sender = 'dukenan006@163.com'

    def msg_text(self):
        msg = """
        <p>今天天气很不错啊</p>
        """
        return msg

    def send_email(self, subject, receivers, html_str):
        msg_text = html_str
        message = MIMEText(msg_text, 'html', 'utf-8')
        message['From'] = formataddr(['中央气象局', self.sender])
        message['To'] = ','.join(receivers)
        message['Subject'] = subject
        try:
            smtpObj = smtplib.SMTP_SSL(MAIL_HOST, MAIL_PORT)
            smtpObj.login(MAIL_USER, MAIL_PASS)
            smtpObj.sendmail(self.sender, receivers, message.as_string())
            smtpObj.quit()
            print('发送成功')
        except smtplib.SMTPException as e:
            print('Error: 无法发送邮件', e)


if __name__ == '__main__':
    h = "<html><p>我么都一样</p></html>"
    e = SendMail()
    e.send_email('今天是个好天气', ['nangongjue5945@qq.com'], h)
