#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-07 10:04
# @Software: PyCharm
# @File    : oushu.py
# 打印1~100内的偶数

# 方法一
for i in range(2,101,2): # 2 4 6 8 10 10
    print(i)

# 方法二
a = 0
while a < 100:
    a = a + 2
    print(a)