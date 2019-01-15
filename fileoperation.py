import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(filepath):
# 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1143043178@qq.com"  # 用户名
    mail_pass = "clnrbnmhiwtgjgbj"  # 口令

    sender = '1143043178@qq.com'
    receivers = ['karatan@locision.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


    file = open(filepath, 'r')
    htmltext = file.read()

    message = MIMEText(htmltext, 'html', 'utf-8')
    message['From'] = Header("1143043178@qq.com", 'utf-8')
    message['To'] = Header("测试kara", 'utf-8')

    subject = '漳州收运系统接口测试报告'
    message['Subject'] = Header(subject, 'utf-8')

    try:
      smtpObj = smtplib.SMTP()
      smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
      smtpObj.login(mail_user, mail_pass)
      smtpObj.sendmail(sender, receivers, message.as_string())
      print("邮件发送成功")
    except:
      smtplib.SMTPException
      print("Error: 无法发送邮件")













