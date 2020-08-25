#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-25 9:39
# @Software: PyCharm
# @File    : class_smtplib.py
'''
SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。
这里我们就需要用到这个库。其中SMTP支持smtplib和Email两个模块，其中smtplib负责发送邮件，email负责构建邮件，SMTP支持发送纯文本，携带附件和携带图片等功能。
'''
# 1、首先导入smtplib模块和email模块中MIMEText（表示文本）
# 2、准备发送邮件所需要的参数（服务器，发送者账号，密码，和收件人账号）
# import smtplib
# from email.mime.text import MIMEText
#
# # 服务器地址
# smtpserver = 'smtp.163.com'  # 发送账号
# user = 'XXXXXXXX@163.com'  # 发送密码
# password = 'xxxxxxx'  # 收件人
# receivers = '123456@qq.com'
#
# # 3、根据源码内容完成对参数对应填写
# # 邮件标题
# subject = 'python 发送邮件'  # 发送内容 （文本内容，发送格式，编码格式）
# message = MIMEText('Python 通过smtplib发送邮件。。。', 'html', 'utf-8')
# # 发送地址
# message['From'] = user
# # 接受地址
# message['To'] = receivers
# # 邮件标题
# message['subject'] = subject
#
# # 4、通过对smtplib模块对邮件进行发送
# smtp = smtplib.SMTP()
# # 连接服务器
# smtp.connect(smtpserver)
# # 登录邮箱账号
# smtp.login(user, password)
# # 发送账号信息
# smtp.sendmail(user, receivers, message.as_string())
# # 关闭
# smtp.quit()


# 携带附件  我们正常发送邮件的时候可能会携带一些附件，当然这个功能python也可以帮助我们完成，SMTP中自带的有携带附件的模块。
# 1、导入email中的MIMEMultipart模块
# 2、准备发送邮件的配置和参数
# 3、邮件携带的附件

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# # 服务器地址
# smtpserver = 'smtp.163.com'  # 发送账号
# user = 'xxxxxx@163.com'  # 发送密码
# password = 'xxxxx'  # 收件人
# receivers = '123456.com'  # 邮件标题
# subject = 'python 发送携带附件邮件'  # 获取附件信息
# with open('name.txt', 'rb', )as f:
#     body = f.read().decode()
# message = MIMEMultipart()
# # 发送地址
# message['From'] = user
# # 接受地址
# message['To'] = receivers
# # 邮件标题
# message['subject'] = subject
# # 正文内容
# body = MIMEText(body, 'html', 'utf-8')
# message.attach(body)
# # 传当前目录中的name.txt文件
# att = MIMEText(open('name.txt', 'rb').read(), 'base64', 'utf-8')
# att["Content-Type"] = 'application/octet-stream'  # 死格式
# # filename 表示附件的名称
# att["Content-Disposition"] = 'attachment; filename="name.txt"'
# message.attach(att)
# smtp = smtplib.SMTP()
# # 连接服务器
# smtp.connect(smtpserver)
# # 登录邮箱账号
# smtp.login(user, password)
# # 发送账号信息
# smtp.sendmail(user, receivers, message.as_string())
# # 关闭
# smtp.quit()
#
# # 如果想要添加多个附件的话继续重新传取附件内容，只需要更改不同的附件名称即可
#
# # 传当前目录中的name.txt文件
# att = MIMEText(open('name.txt', 'rb').read(), 'base64', 'utf-8')
# att["Content-Type"] = 'application/octet-stream'  # 死格式
# # filename 表示附件的名称
# att["Content-Disposition"] = 'attachment; filename="name.txt"'


'''
邮件中添加图片
我们正常发送邮件的时候可以添加图片，当然python发送一样可以帮助我们完成这个需求
1、添加图片，需要用到email中的MIMEImage模块
2、准备发送邮件的配置和参数
3、邮件携带的附件
由于html中不能添加图片链接，因为会被认为是恶意链接，我们可以通过在html写入图片ID，通过ID进行匹配图片内容
'''
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# # 添加图片
# img_body = '''
#     <html>
#     <head>Python 发送携带图片信息</head>
#     <body>
#     <p>
#     <p><img src="cid:imageid"></p>
#     <p>
#     </body>
#     </html>
# '''
#
# # 正文内容
# body = MIMEText(img_body, 'html', 'utf-8')
# f = open('123.jpg', 'rb')
# mag = MIMEImage(f.read())
# f.close()
# # 定义图片ID在HTML中展示
# mag.add_header('Content-ID', 'imageid')
# # 添加图片图片
# message.attach(mag)
# # 添加body内容
# message.attach(body)


# 完整代码：
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 服务器地址
smtpserver = 'smtp.163.com'  # 发送账号
user = 'xxxxx@163.com'  # 发送密码
password = 'xxxxxxx'  # 收件人
receivers = '123456@qq.com'  # 邮件标题
subject = 'python 发送图片邮件'
message = MIMEMultipart()

img_body = '''

< html >
< head > Python
发送携带图片信息 < / head >
< body >
< p >
< p > < img
src = "cid:imageid" > < / p >
< p >
< / body >
< / html >
'''

# 正文内容
body = MIMEText(img_body, 'html', 'utf-8')
f = open('123.jpg', 'rb')
mag = MIMEImage(f.read())
f.close()
# 定义图片ID在HTML中展示
mag.add_header('Content-ID', 'imageid')
# 添加图片信息
message.attach(mag)
# 添加正文
message.attach(body)
# 发送地址
message['From'] = user
# 接受地址
message['To'] = receivers
# 邮件标题
message['subject'] = subject
# 非SSL邮箱
smtp = smtplib.SMTP()
# 连接服务器
smtp.connect(smtpserver)
# 登录邮箱账号
smtp.login(user, password)
# 发送账号信息
smtp.sendmail(user, receivers, message.as_string())
# 关闭
smtp.quit()

# 注意：上面的使用一些常规的邮箱，如果你的发件邮箱有SSL认证的需要打开认证信息，比如QQ邮箱需要配置一些信息
'''
QQ邮箱举例：
1、进入-设置--账户--POP3服务内容，打开POP3/SMTP服务
2、开启后会给一个密码，这个密码就是我们需要登录的密码，复制保存下来
3、上面的代码中需要更改服务器内容
'''

# SSL邮箱（QQ邮箱）
smtp = smtplib.SMTP_SSL(smtpserver, 465)
# 登录邮箱账号
smtp.login(user, password)
# 发送账号信息
smtp.sendmail(user, receivers, message.as_string())
# 关闭
smtp.quit()
