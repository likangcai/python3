#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-23 16:31
# @Software: PyCharm
# @File    : class_re.py

# re模块-->正则表达式
# Python自带了匹配字符串的模块re，我们可以通过该模块对字符串进行（模糊）匹配，提取出我们需要的内容。
# re模块中很多功能都是基于正则表达式实现的。正则表达式是一种特殊的字符序列，它能帮助我们去检查字符串是否与某种模式相匹配。

# 1、re.compile(pattern, flags=0)
# 将正则表达式编译成正则对象，搭配match、search、findall等等进行匹配。
# import re
# prog = re.compile('[abc]')  # 匹配字符集abc与字符串匹配的第一个字符
# print(prog.search('abcd').group())
#
# str = 'abcder'
# bl = prog.search(str).group()
# print(bl)

# 2、re.match(pattern, string, flags=0)
# 从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# import re

# # \w 用来匹配单次字符 包括 a-z A-Z 0-9 _
# r = re.match('h\w+', 'how are you')
# # 获取匹配到的结果
# print(r.group())
# r = re.match('h(\w+)', 'how are you')
# # groups 获取模型中匹配到的结果，返回匹配到的字符串的分组部分
# print(r.groups())
#
# # 引用别名word1、word2，他们相当于key,value就是匹配到的内容
# r = re.match('(?P<word1>h)(?P<word2>\w+)', 'how are you')
# print(r.group())
# print(r.groups())
# print(r.groupdict())

# 3、re.search(pattern,string,flags=0)
# 扫描整个字符串，返回第一个成功的匹配，如果匹配失败，返回None。
# import re
#
# # \w 用来匹配单次字符 包括 a-z A-Z 0-9 _
# r = re.search('a\w+', 'how are you')
# # 获取匹配到的结果
# print(r.group())
# r = re.search('a(\w+)', 'how are you')
# # groups 获取模型中匹配到的结果，返回匹配到的字符串的分组部分
# print(r.groups())
# # 引用别名word1,word2他们相当于key,value就是匹配到的内容
# r = re.search('(?P<word1>a)(?P<word2>\w+)', 'how are you')
# print(r.group())
# print(r.groups())
# print(r.groupdict())

# 4、re.findall(pattern, string, flags=0)
# 以string列表形式返回string中pattern的所有非重叠匹配项。从左到右扫描该字符串，并以找到的顺序返回匹配项。
# 如果该模式中存在一个或多个组，则返回一个组列表；否则，返回一个列表。如果模式包含多个组，则这将是一个元组列表。空匹配项包含在结果中。
# import re
#
# # 匹配包含所有带有o的单次
# r = re.findall('\wo\w+', 'how are you')
# print(r)
# # * 前的字符可以是0个或者多个，返回list
# r = re.findall('好*', '你好吗？我很好。你好才是真的好。你好好了')
# print(r)
# r = re.findall('你好*', '你好吗？我很好。你好才是真的好。你好好了')
# print(r)
# # + 用于匹配字符一次或者多次
# r = re.findall('好+', '你好吗？我很好。你好才是真的好。你好好了')
# print(r)
# r = re.findall('你好+', '你好吗？我很好。你好才是真的好。你好好了')
# print(r)
# # $ 用来匹配结尾
# r = re.findall('测试$', '测试小姐姐还没对象')
# print(r)
# r = re.findall('测试$', '小姐姐我的代码还没测试')
# print(r)
# # ^ 用来匹配开始
# r = re.findall('^小姐姐', '小姐姐我的代码还没测试')
# print(r)
# # ^ 用于字符集中表示取反
# # 匹配所有除字母外的字符
# r = re.findall('[^a-z]', '123abcde789')
# print(r)

# 5、re.split(pattern, string, maxsplit=0, flags=0)
# split能够按照所能匹配的字串将字符串进行切分，返回切分后的字符串列表
import re

# 按照； 或者 ，对字符串进行分割
r = re.split('[;,]]', 'abc,qwer;opq,mn')
print(r)

