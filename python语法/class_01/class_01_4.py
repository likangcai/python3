#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-07-12 23:23
# @Software: PyCharm
# @File    : class_01_4.py

str_1 = 'hello'
str_2 = 'HELLO'

#2、字符串的查找 find()函数
# res = str_1.find('o')
# # res = str_1.find('he')
# # res = str_1.find('666')
# print('查找的结果：{}'.format(res))
#单个字符 如果能够找到 就返回单个字符在字符串里面的索引值
#子字符串 如果能够找到就返回子字符串的第一个元素在原来字符串里面的索引值
#没找到 返回-1


#字符串的大小写切换 upper()  lower()
# res = str_2.lower()
# print(res)

#3、字符串的替换 replace() 函数 内建 可以指定替换次数
# res = str_1.replace('o',"影子",1) #你要替换的目标字符 你要换上去的新值
# print('替换后的结果：{}'.format(res))

#4、字符串的切割split()
# res = str_1.split('o') #返回列表类型的数据 但是元素类型还是字符串
# print('切割后的结果：{}'.format(res))

#5、字符串头尾的处理 strip()
res = str_1.strip('o') #只能处理头尾 不能处理中间的
print('处理后的结果：{}'.format(res))
