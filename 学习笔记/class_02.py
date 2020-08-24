#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-09 23:00
# @Software: PyCharm
# @File    : class_02.py
# 10 行以下 Python 代码高效使用

# 1、生产二维码
# 二维码作为一种信息传递的工具，在当今社会发挥了重要作用。而生成一个二维码也非常简单，在Python中我们可以通过MyQR模块了生成二维码，
# 而生成一个二维码我们只需要2行代码，我们先安装MyQR模块，这里选用国内的源下载：
# pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ myqr

# 方法一
# from MyQR import myqr
# myqr.run(words='http://www.baidu.com')

# 方法二
# from MyQR import myqr
# myqr.run(
#     words='http://www.baidu.com',  # 包含信息
#     picture='123.jpg',  # 背景图片
#     colorized=True,    # 是否有颜色，如果为False则为黑色
#     save_name='yingzi.png'  # 输出文件名
# )

# # 方法三
# from MyQR import myqr
# import os
#
# version, level, qr_name = myqr.run(
#     words="https://www.baidu.com",  # 可以是字符串，也可以是网址(前面要加http(s)://)
#     version=1,  # 设置容错率为最高
#     level='Q',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
#     picture="123.gif",  # 将二维码和图片合成
#     colorized=True,  # 彩色二维码
#     contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
#     brightness=1.0,  # 用来调节图片的亮度，其余用法和取值同上
#     save_name="shuchu.gif",  # 保存文件的名字，格式可以是jpg,png,bmp,gif
#     save_dir=os.getcwd()  # 控制位置
# )

# 2、词云是数据可视化的一种非常优美的方式，我们通过词云可以很直观的看出一些词语出现的频率高低。使用Python我们可以通过wordcloud模块生成词云，
# 我们先安装wordcloud模块： pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ wordcloud

# from wordcloud import WordCloud
# wc = WordCloud()  # 创建词云对象
# wc.generate('Do not go gentle into that good night')  # 生成词云
# wc.to_file('wc.png')  # 报存词云

# 3、抠图的实现需要借助百度飞桨的深度学习工具paddlepaddle，我们需要安装两个模块就可以很快的实现批量抠图了，
# 第一个是PaddlePaddle： 安装 pip3 install paddlepaddle -i https://mirror.baidu.com/pypi/simple
# 第二个是paddlehub模型库，安装 pip3 install -i https://mirror.baidu.com/pypi/simple paddlehub
# 更详细的安装事项可以参见飞桨官网：https://www.paddlepaddle.org.cn/

# import os, paddlehub as hub
#
# humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')  # 加载模型
# path = 'D:/python3/学习笔记/'  # 文件目录
# files = [path + i for i in os.listdir(path)]  # 获取文件列表
# results = humanseg.segmentation(data={'image': files})  # 抠图

#4、文字情绪识别
# 在paddlepaddle面前，自然语言处理也变得非常简单。实现文字情绪识别我们同样需要安装PaddlePaddle和Paddlehub，具体安装参见三中内容。

# import paddle
# import paddlehub as hub
# senta = hub.Module(name='senta_lstm')        # 加载模型
# sentence = [    # 准备要识别的语句
#     '你真美', '你真丑', '我好难过', '我不开心', '这个游戏好好玩', '什么垃圾游戏',
# ]
# results = senta.sentiment_classify(data={"text":sentence})    # 情绪识别
# # 输出识别结果
# for result in results:
#     print(result)

#5、识别是否戴了口罩 这里同样是使用PaddlePaddle的产品，我们按照上面步骤安装好PaddlePaddle和Paddlehub
# 执行程序后，项目下会生成detection_result文件夹，识别结果都会在里面

# import paddlehub as hub
# module = hub.Module(name='pyramidbox_lite_mobile_mask')  # 加载模型
# image_list = ['face.jpg']  # 图片列表
# input_dict = {'image':image_list}  # 获取图片字典
# module.face_detection(data=input_dict)  # 检测是否带了口罩

#6、简易信息轰炸
# Python控制输入设备的方式有很多种，我们可以通过win32或者pynput模块。我们可以通过简单的循环操作来达到信息轰炸的效果，
# 这里以pynput为例，我们需要先安装模块：# pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pynput
# 在写代码之前我们需要手动获取输入框的坐标：

# from pynput import mouse
# # 创建一个鼠标
# m_mouse = mouse.Controller()
# # 输出鼠标位置
# print(m_mouse.position)
# # 可能有更高效的方法，但是我不会。
# # 获取后我们就可以记录这个坐标，消息窗口不要移动。然后我们执行下列代码并将窗口切换至消息页面：
#
# import time
# from pynput import mouse, keyboard
# time.sleep(5)
# m_mouse = mouse.Controller()    # 创建一个鼠标
# m_keyboard = keyboard.Controller()  # 创建一个键盘
# m_mouse.position = (850, 670)       # 将鼠标移动到指定位置
# m_mouse.click(mouse.Button.left) # 点击鼠标左键
# while(True):
#     m_keyboard.type('你好')        # 打字
#     m_keyboard.press(keyboard.Key.enter)    # 按下enter
#     m_keyboard.release(keyboard.Key.enter)    # 松开enter
#     time.sleep(0.5)    # 等待 0.5秒

#7、识别图片中的文字
# 我们可以通过Tesseract来识别图片中的文字，在Python中实现起来非常简单，但是前期下载文件、配置环境变量等稍微有些繁琐
# 其中text就是识别出来的文本。如果对准确率不满意的话，还可以使用百度的通用文字接口

import pytesseract
from PIL import Image
img = Image.open('test.jpg')
text = pytesseract.image_to_string(img)
print(text)

#8、绘制函数图像
# 图标是数据可视化的重要工具，在Python中matplotlib在数据可视化中发挥重要作用，下面我们来看看使用matplotlib如何绘制一个函数图像

# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.arange(1,11)     # x轴数据
# y =  x * x +  5         # 函数关系
# plt.title("y=x*x+5")     # 图像标题
# plt.xlabel("x")     # x轴标签
# plt.ylabel("y")     # y轴标签
# plt.plot(x,y)     # 生成图像
# plt.show()    # 显示图像


# 9、人工智能
# 下面给大家介绍的是独家的AI人工智能，一般不外传的。这个人工智能可以回答许多问题，当然人工智能现在还在发展阶段，
# 想要理解人类的语言还差很多。废话不多说，下面来看看我们的人工智能Fdj

# while(True):
#     question = input("请输入：")
#     answer = question.replace('吗', '呢')
#     answer = answer.replace('？', '！')
#     print(answer)