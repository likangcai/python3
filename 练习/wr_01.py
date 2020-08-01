#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-01 17:16
# @Software: PyCharm
# @File    : wr_01.py

# 设计一个函数，在文件夹上创建10文本，以数字给它们命名


import os


def folder():
    os.mkdir('H:\github\python3\练习\\folder')  # 创建folder文件夹
    i = 0
    for i in range(1, 11, 1):
        if i < 11:
            file = open('H:\github\python3\练习\\folder\\' + str(i) + '.txt', 'a+', encoding='utf-8')  # 创建文件
            i = i + 1
        else:
            break  # 终止循环语句


folder()
