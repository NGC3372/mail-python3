from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart


class MyEmail:

    def __init__(self, account: str, password: str, smtp_server: str):
        self.account = account
        password = password
        smtp_server = smtp_server
        self.server = SMTP_SSL(smtp_server)  # SMTP协议默认端口是25
        self.server.set_debuglevel(1)
        self.server.login(account, password)

    def create_email(self, title: str, content: str):
        msg = MIMEMultipart()
        msg['From'] = self.account
        msg['Subject'] = Header(title, 'utf-8')
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        return msg

    def add_email_attachment(self, email: MIMEMultipart, path: str, file_name: str):
        att = MIMEText(open(path).read(), 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment; filename= "{}"'.format(file_name)
        email.attach(att)

    def send_email(self, email: MIMEMultipart, receiver: []):
        email["To"] = str(receiver)
        self.server.sendmail(self.account, receiver, email.as_string())

    def quit(self):
        self.server.quit()

