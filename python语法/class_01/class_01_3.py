#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-07-12 22:34
# @Software: PyCharm
# @File    : class_01_3.py
#1、格式化输出
age = 18 #存放的是年龄 int
name = '影子' #存放的是名字 str
score = 99.99 #浮点数 float
# print(name+",今年 "+str(age),"岁")
# print(name+",今年",age,"岁")

#格式化输出 %d整数 %f浮点数 %s字符串
# print('%s今年 %d 岁'%(name,age)) #按顺序取值
# print('%s今年 %s 岁'%(name,age))
# print('%s今年 %s 岁,数学考了%.2f'%(name,age,score))  #%.2f表示精确到小数点后2位
#%d 必须放一个整数 %f可以放一个整数，也可以放一个浮点数 %s 可以放任意值

#2、第二种格式化输出 format {}
print("{}今年数学考了{}".format(name,score))
print("{0}今年数学考了{1}".format(name,score)) #按顺序取值
#{}里面不指定数值 就会按顺序取值
#{}里面指定数值 就会根据你设置的去取值
#format里面的数据也是有索引的 从0开始标记数据



