#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-07-12 22:17
# @Software: PyCharm
# @File    : calss_01_2.py
#字符串的切片
# a = 'hello'
#根据字符串的索引去取值 缺点 只能取单个值
#切片：可以根据你的要求去取值 子字符串
#字符串的切片：  字符串名[m:n:k]
#m 索引开始的地方 n 索引结束的地方 k步长
# res = a[0:4:1] #0 1 2 3取左不取右 n-1就结束了索引的取值
# res = a[0:5:2]  #k=2  0 2 4
# res = a[0:5] #如果不输入k 那么k就去取默认值k=1  0 1 2 3 4
# res = a[:] #从头取到尾
# res = a[0:] #默认取完所有值

# str_1 = 'hello python3 nihao'
# #在字符串里面 空格也是一个字符
# #偶数位的元素取出来 不包含0
# #对应的索引值： 2 4 6 8 10 12 14 16 18
# #因为是偶数，k=2
# print(str_1[2:19:2])

#什么时候用切片：如果你想获取字符串里面的子字符串就可以用

