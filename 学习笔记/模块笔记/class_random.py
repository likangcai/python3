#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-23 18:25
# @Software: PyCharm
# @File    : class_random.py
# 基本随机函数 计算机产生随机数是需要随机数种子的，例如 给定一个随机数种子，就能利用梅森旋转算法产生一系列随机序列
# 每一个数都是随机数，只要随机种子相同，产生的随机数和数之间的关系都是确定的 随机种子确定了随机序列的产生
# 基本随机函数  seed() 初始化随机数种子
# random() 方法返回随机生成的一个实数，它在[0,1)范围内。
import random

# print(random.randint(1, 10))  # 产生 1 到 10 的一个整数型随机数
# print(random.random())  # 产生 0 到 1 之间的随机浮点数
# print(random.uniform(1.1, 5.4))  # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
# print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数
#
# a = [1, 3, 5, 6, 7]  # 将序列a中的元素顺序打乱
# random.shuffle(a)
# print(a)

# random.seed()
# random.seed(a=None,version=2)  # 设置随机种子 ，用于同步不同运行环境的随机数。
# random.getstate()  # 获得当前状态，用于恢复状态
# random.setstate()  # 恢复状态
# random.getrandbits(k)  # 生成占内存k位以内的随机整数，硬核秃头专属。
# random.random()  # 随机产生一个[0,1.)的数字
# random.uniform(a, b)  # 产生一个a,b区间的随机数
# random.randrange(0,101,1)   # 整数随机，等同于choice(range(start, stop, step))
# random.randint(a, b)  # 返回一个[a,b]的随机整数。功能等同于randrange(a, b+1)
# random.choice(seq)  # 返回对象中的一个随机元素
# print(random.choice(['win', 'lose', 'draw']))

# random.choices(population, weights=None, *, cum_weights=None, k=1)  # 随机选择，是random.choice(seq)的升级版本。
# print(random.choice(['win', 'lose', 'draw']))

# random.sample(population, k)  # 随机取样
# print(random.sample([10, 20, 30, 40, 50], k=3))
# choices与sample的区别： choices在抽取随机元素时是包含重复元素的，即：一个元素可能会被抽取多次。
# 反之，在sample中，抽取的元素是不重复的。所以，在抽取元素大于样本集总数时，choices会继续而sample会报错

# random.shuffle(x[,random])  # 打乱序列
# de = 'ace two three four'.split()
# print("执行shuffle函数前：{0}".format(de))
# random.shuffle(de)
# print("执行shuffle函数后：{}".format(de))

# 不同的分布模式
# random.triangular(low, high, mode)
# https://en.wikipedia.org/wiki/Triangular_distribution
# random.betavariate(alpha, beta)
# https://en.wikipedia.org/wiki/Beta_distribution
# random.expovariate(lambd)
# https://en.wikipedia.org/wiki/Exponential_distribution
# random.gammavariate(alpha, beta)
# https://en.wikipedia.org/wiki/Gamma_distribution
# random.gauss(mu, sigma)
# https://en.wikipedia.org/wiki/Normal_distribution
# random.lognormvariate(mu, sigma)
# https://en.wikipedia.org/wiki/Log-normal_distribution
# random.normalvariate(mu, sigma)
# https://en.wikipedia.org/wiki/Normal_distribution
# random.vonmisesvariate(mu, kappa)
# https://en.wikipedia.org/wiki/Von_Mises_distribution
# random.paretovariate(alpha)
# https://en.wikipedia.org/wiki/Pareto_distribution
# random.weibullvariate(alpha, beta)
# https://en.wikipedia.org/wiki/Weibull_distribution

# random.triangular(low, high, mode)  # 以三角分布的概率分布返回随机数

# import random
# import collections
#
# counter = collections.Counter()  # 用Counter统计次数
# for i in range(10000):
#     step = str(round(random.triangular(0, 9, 7)))
#     counter.update(step)
#
# print(counter)
#
# for i in range(10):
#     print(str(i), end='')
#     value = round(counter[str(i)] / 100.)
#     for j in range(value):
#         print('*', end='')
#     print('')

# random.betavariate(alpha, beta)   # 以beta分布的概率分布返回0到1之间的随机数。

# import random
# import collections
#
# counter = collections.Counter()
# for i in range(10000):
#     step = str(round(random.betavariate(2, 5) * 10))
#     counter.update(step)
#
# print(counter)
# for i in range(10):
#     print(str(i), end='')
#     value = round(counter[str(i)] / 100.)
#     for j in range(value):
#         print('*', end='')
#     print('')

# random.expovariate(lambd)   # 以指数分布的概率分布返回随机数。
# import random
# import collections
#
# counter = collections.Counter()
# for i in range(10000):
#     step = str(round(random.expovariate(1)))
#     counter.update(step)
#
# print(counter)
# for i in range(10):
#     print(str(i), end='')
#     value = round(counter[str(i)] / 100.)
#     for j in range(value):
#         print('*', end='')
#     print('')

# random.gammavariate(alpha, beta)  # 以gamma分布的概率分布返回随机数。
# import random
# import collections
#
# counter = collections.Counter()
# for i in range(10000):
#     step = str(round(random.gammavariate(9, 0.5)))
#     counter.update(step)
#
# print(counter)
#
# for i in range(10):
#     print(str(i), end='')
#     value = round(counter[str(i)] / 100.)
#     for j in range(value):
#         print('*', end='')
#     print('')

# random.gauss(mu, sigma)  # 以高斯分布的概率分布返回随机数。
# import random
# import collections
#
# counter = collections.Counter()
# for i in range(10000):
#     step = str(round(random.gauss(5, 1)))
#     counter.update(step)
#
# print(counter)
#
# for i in range(10):
#     print(str(i), end='')
#     value = round(counter[str(i)] / 100.)
#     for j in range(value):
#         print('*', end='')
#     print('')

# random.lognormvariate(mu, sigma)  # 以对数正态分布的概率分布返回随机数。
# import random
# import collections
#
# counter = collections.Counter()
# for i in range(10000):
#     step = str(round(random.triangular(5, 0.02)))
#     counter.update(step)
#
# print(counter)
#
# for i in range(10):
#     print(str(i), end='')
#     value = round(counter[str(i)] / 100.)
#     for j in range(value):
#         print('*', end='')
#     print('')

# random.normalvariate(mu, sigma)  # 同random.gauss(mu, sigma)
# random.vonmisesvariate(mu, kappa)  # 以von Mises分布的概率分布返回随机数。又作圆上正态分布
# import random
# import collections
#
# counter = collections.Counter()
# for i in range(10000):
#     step = str(round(random.vonmisesvariate(3.14, 2)))
#     counter.update(step)
#
# print(counter)
#
# for i in range(7):
#     print(str(i), end='')
#     value = round(counter[str(i)] / 100.)
#     for j in range(value):
#         print('*', end='')
#     print('')

# random.paretovariate(alpha)  # 以Pareto分布的概率分布返回随机数。
# import random
# import collections
#
# counter = collections.Counter()
# for i in range(10000):
#     step = str(round(random.paretovariate(2)))
#     counter.update(step)
#
# print(counter)
#
# for i in range(10):
#     print(str(i), end='')
#     value = round(counter[str(i)] / 100.)
#     for j in range(value):
#         print('*', end='')
#     print('')

# random.weibullvariate(alpha, beta)  # 以Weibull分布的概率分布返回随机数。
# import random
# import collections
#
# counter = collections.Counter()
# for i in range(10000):
#     step = str(round(random.weibullvariate(1, 5) * 5))
#     counter.update(step)
#
# print(counter)
#
# for i in range(10):
#     print(str(i), end='')
#     value = round(counter[str(i)] / 100.)
#     for j in range(value):
#         print('*', end='')
#     print('')

