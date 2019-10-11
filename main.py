import os
import re
import time
import psutil
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr



def mail():
	
	my_sender=''  # 发件人邮箱账号
	my_pass = ''   # 发件人邮箱密码
	my_user =''      # 收件人邮箱账号，我这边发送给自己
	ret=True
	try:
		msg=MIMEText('快来看看吧','plain','utf-8')
		msg['From']=formataddr(["xiaoxiaoqiao",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
		msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject']="监控网络好像挂掉了"                # 邮件的主题，也可以说是标题
		server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
		server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
		server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()  # 关闭连接
	except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
		print(e)
		ret=False
	return ret
 

def flow():

	return psutil.disk_io_counters()[3]

print("start call me")
print(time.asctime( time.localtime(time.time() ) ) )
count = []
while True:
	fir = flow()
	time.sleep(10)
	last = flow()
	num = round((last-fir)/10/1024**2, 2)
	if num <0.18:
		count.append(num)
		if len(count) >8:
			print(count)
			while not mail():
				time.sleep(10)
			count = []
			time.sleep(3600)
	else:
		count = []
