#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-07-28 13:49
# @Software: PyCharm
# @File    : password3.py

'''
输入密码错误超过3次就禁止再次输入
'''
password_list = ['*##*','123456']

def account_login():
    tries = 3
    while tries > 0:  #条件成立可输入密码
        password = input('请输入密码:')
        password_correct = password == password_list[1]
        password_reset = password == password_list[0]

        if password_correct: #条件为真
            print('登录成功！')

        elif password_reset:
            new_password = input('输入新密码并回车:')
            password_list.append(new_password)
            print('密码已成功更改!')
            account_login()

        else:
            print('密码错误或输入无效!')
            tries = tries -1  #密码输入错误减1
            print(tries,'times left')

    else: #次数用完进行账号锁定
        print('你的账号已被暂停！')

account_login()

