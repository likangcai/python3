#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-25 13:59
# @Software: PyCharm
# @File    : 生成器.py
import random

from PyInstaller.loader.pyiboot01_bootstrap import fn


class FakeUser():
    def fake_name(self, amount=1, one_word=False, two_words=False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
            yield full_name
            n += 1

    def fake_gender(self, amount=1):
        n = 0
        while n <= amount:
            gender = random.choice(['男', '女', '未知'])
            yield gender
            n += 1


class SnsUser(FakeUser):
    def get_followers(self, amount=1, few=True, a_lot=False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1, 50)
            elif a_lot:
                followers = random.randrange(200, 10000)
            yield followers
            n += 1


user_a = FakeUser()
user_b = SnsUser()
for name in user_a.fake_names(30):
    print(name)
for gender in user_a.fake_gender(30):
    print(gender)