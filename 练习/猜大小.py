#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-07 11:53
# @Software: PyCharm
# @File    : 猜大小.py

import random


def roll_dice(numbers=3, points=None):
    print('<<<< 掷 骰 子! >>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers = numbers - 1
    return points


def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return "大"
    elif isSmall:
        return "小"


def start_game():
    print('<<<< 开 始 游 戏! >>>>')
    choices = ['大', '小']
    your_choice = input('请输入大或者小:')
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choice == roll_result(total)
        if youWin:
            print('重点是', points, '你赢了!')
        else:
            print('重点是', points, '你输了!')
    else:
        print('无效的选择，请选择大或小!')
        start_game()


start_game()
