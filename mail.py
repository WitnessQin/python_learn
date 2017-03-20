import smtplib,io
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host='mail.haha.com'  #设置服务器
mail_user='qinyinglin@haha.com'    #用户名
mail_pass='hahahaha'  #口令 

sender='qinyinglin@haha.com'
mail_receiver=['hahahaha@qq.com','qinyinglin@haha.com']
mail_to = ','.join(mail_receiver)
#需要用逗号隔开

HtmlFile = "c:\\python35\\work\\result.html"
with open(HtmlFile, "rb") as fb:
	#print(fb.read())
	message=MIMEText(fb.read(),'html','UTF-8')
#如果需要发送的是html，可以用这种方式

#message=MIMEText('python 邮件发送测试','plain','UTF-8')
message['From']=Header(sender,'UTF-8')
message['To']=mail_to

subject='python SMTP 邮件测试主题'
message['Subject']=Header(subject,'UTF-8')



try:
	smtpObj=smtplib.SMTP()
	print('准备连接服务器')
	smtpObj.connect(mail_host)
	print('准备登录邮箱')
	smtpObj.login(mail_user, mail_pass)
	print('准备邮件发送')
	smtpObj.sendmail(sender, mail_receiver, message.as_string())
	print('邮件发送成功')
except smtplib.SMTPException:
	print('error:无法发送邮件')