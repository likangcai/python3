#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @File    : class_001.py
# @Time    : 2020-07-10 12:53
# @Software: PyCharm
#判断输入的密码与默认值是否一致，如果不一致提示错误，并接着重新输入

def account_login():  #定义函数
    password = input("请输入密码：")  #终端输入
    if password == 'lkc123456':
        print("密码正确，登录成功！")
    else:
        print('密码错误，请重新输入!')
        account_login()  #再次调用函数，让用户再次输入密码

account_login()  #调用函数

