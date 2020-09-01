#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-09-01 12:29
# @Software: PyCharm
# @File    : class_math.py
'''
在数学之中，除了加减乘除四则运算之外——这是小学数学——还有其它更多的运算，比如乘方、开方、对数运算等等，要实现这些运算，需要用到 Python 中的一个模块：Math
模块(module)是 Python 中非常重要的东西，你可以把它理解为 Python 的扩展工具。换言之，Python 默认情况下提供了一些可用的东西，
但是这些默认情况下提供的还远远不能满足编程实践的需要，于是就有人专门制作了另外一些工具。这些工具被称之为“模块”
任何一个 Pythoner 都可以编写模块，并且把这些模块放到网上供他人来使用。
当安装好 Python 之后，就有一些模块默认安装了，这个称之为“标准库”，“标准库”中的模块不需要安装，就可以直接使用。
如果没有纳入标准库的模块，需要安装之后才能使用。模块的安装方法，我特别推荐使用 pip 来安装。这里仅仅提一下，后面会专门进行讲述，性急的看官可以自己 google。
使用 math 模块 math 模块是标准库中的，所以不用安装，可以直接使用。
'''
import math
# print(math.pi)  # 要得到圆周率
# # 这个模块都能做哪些事情呢？可以用下面的方法看到：
# print(dir(math))

# dir(module)是一个非常有用的指令，可以通过它查看任何模块中所包含的工具。从上面的列表中就可以看出，在 math 模块中，可以计算正 sin(a),cos(a),sqrt(a)......
# 这些我们称之为函数，也就是在模块 math 中提供了各类计算的函数，比如计算乘方，可以使用 pow 函数。但是，怎么用呢？
# Python 是一个非常周到的姑娘，她早就提供了一个命令，让我们来查看每个函数的使用方法。
# print(help(math.pow))  # 这里展示了 math 模块中的 pow 函数的使用方法和相关说明。

# 下面是几个常用的 math 模块中函数举例，看官可以结合自己调试的进行比照。
# print(math.sqrt(9))
# print(math.floor(3.14))
# print(math.floor(3.92))
# print(math.fabs(-2))  # 等价于 abs(-2)
# print(abs(-2))
# print(math.fmod(5,3))  # 等价于 5%3
# print(5%3)

# 求绝对值
# print(abs(10))
# print(abs(-10))
# print(abs(-1.2))

# 四舍五入
print(round(1.234))
print(round(1.234, 2))
# 如果不清楚这个函数的用法，可以使用下面方法看帮助信息
print(help(round))
