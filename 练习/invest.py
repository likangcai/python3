#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-02 16:07
# @Software: PyCharm
# @File    : invest.py

#  设计一个复利函数，它包含三个函数，amount资金，rate利率，time投资时间。输入每个参数后调用函数，应该返回每一年的资金总额，假设利率5%。
# 复利公式=本金X(1+利息)^时间


# 方法一
# def invest(amount, rate, time):
#     principal = amount * (1 + rate) ** time
#     return principal
# print('复利结果为:{0}'.format(invest(100, 0.05, 2)))


# 方法二
def invest():
    amount = float(input("请输入本金："))
    rate = float(input("请输入利率："))
    time = int(input("请输入期数："))
    fl = amount * (1 + rate) ** time
    return fl


print(invest())