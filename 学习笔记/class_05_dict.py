#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-21 17:15
# @Software: PyCharm
# @File    : class_05_dict.py
# Python字典操作总结
'''
字典相对于列表，查找速度快，不会随着元素增多而变慢，时间复杂度O(1)，并且字典是另一种可存储任意类型对象。
字典中存储的元素都是键值对（key:value）,键值之间用冒号(:)分割, 每个字典元素(键值对)之间用逗号(,)分割, 整个字典包括在花括号 {} 中。
{key1:value1,key2:value2,key3:value3}
字典的key是唯一的，并且可以是任意的不可变对象（int、str、bool、tuple ...），但是一般我们都使用str作为字典的key。
字典的值不需要唯一, 可以为任何的数据类型，字典的key不能重复的，否则后边的会替换到前边的值。
'''
# 1.元素访问  直接通过key来获取, 如果key不存在，则会抛出错误。使用 get 方法来根据键获得值, key不存在则默认返回 None，返回值也可自定义。
d = {'name': 'Tom', 'age': 18, 'gender': 'male'}
#  使用key获取
print(d['name'])
#  使用get方法获取
print(d.get('name'))
print(d.get('weight', "170"))

# 2.删除清空元素  使用 pop 方法根据 key 来删除字典中的元素。 del 删除字典或指定的键值对。  使用clear清空元素。
d = {'name': 'Tom', 'age': 18, 'gender': 'male'}
# 删除某个key指定的元素
d.pop('name')
del d['age']
# 删除整个字典
del d
# 清空字典
d.clear()

# 3.新增或修改元素（有则更新，无则新增） 直接通过key来进行修改或者新增，当key存在为修改，键不存在, 默认为新增元素。
d = {'name': 'Tom', 'age': 18, 'gender': 'male'}
d['name'] = 'Lily'  # 修改元素
d['weight'] = 180  # 新增元素，使用update可以批量更新

# 4.遍历元素  字典是非序列式容器, 无法通过逐个元素获取, 需要先将字典转换成类似列表的形式, 再对其进行遍历。
# 1.通过字典的 keys 方法，获得字典key的列表， 然后根据key进行遍历。
d = {'name': 'Tom', 'age': 18, 'gender': 'male'}
for k in d.keys():
    print(k, d[k])

# 2.通过字典的 values 方法，获得字典值的列表。
d = {'name': 'Tom', 'age': 18, 'gender': 'male'}
for value in d.values():
    print(value)

# 3.通过字典的 items 方法，返回可迭代对象，内部是元组，元组有2个数据，一个是字典key，一个是字典的value
d = {'name': 'Tom', 'age': 18, 'gender': 'male'}
for item in d.items():
    print(item)

