#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-07-12 21:43
# @Software: PyCharm
# @File    : class_01_1.py
#语法：必须要遵守的规范 方法使用
#标识符：凡是在python 我们自己命名的 自己取名字 都是标识符
#项目名 包名 模块名
#变量名 函数名 类名
#1、字母 下划线 数字组成 命名的时候 不能以数字开头
#2、见名知意  不同的字母和数字之间用下划线隔开
#class_basic_1(推荐使用)  classbasic1(不推荐使用)
#3、项目名 包名 模块名 变量名 函数名 都是小写字母 不同的字母之间用下划线隔开
#4、类名 首字母大写驼峰命名  StudentInfo   HttpRequest
#5、不能以关键字作为标识符 int str float class if...

#行和缩进 利用缩进来控制代码的级别
# a = 1
# if a > 0:  #父级
#     print('这个是子集！') #子集
# elif a < 0:
#     print("这个也属于子集")

#注释  #表示单行注释  快捷键ctrl+/   ''''''成对的三个单行引号括起来的内容就是多行注释
#注释：这是一个备注信息，代码不会执行

#多行语句 连接符 \
# print('hello '
#       'python '
#       '6666')

# print('hello\
#        python\
#        6666')

#python的引号 单引号 双引号 三引号
#成对的单引号 成对的双引号 三引号 括起来的内容 都是字符串
#字符串里面的元素是由一个一个的字符组成
#字符串都是有索引的 从0开始数值
#字符串的取值方式 字符串名[索引值]
# a = '5'
# b = '54656'
# c = '''65683.5'''
# #type()可以帮你判断数据的类型
# print(type(a))
# print(type(b))
# print(type(c))
# print(a[2])
# print(a[-2])

#怎么处理字符串里面的特殊字符 转义 加r/R 加\
#\n \t \r

#字符串的运算 + *
#+ 是拼接字符串的意思
a = '你好'
b = 'python'
c = a + b
# print(c)
# print(type(c))

#*重复字符串输出
# print(a*2)

#判断字符串in  not in 成员运算符 返回值 布尔值 True Fals
# a = 'hello'
# print('t' in a)



#什么时候用什么引号  看自己，没有要求
# str_1 = 'hello,"影子"'
#单引号 替换双引号
#我们如果要把双引号或者单引号作为字符串输出的一部分
# 单引号和双引号分开 不能同时存在两个一样的单引号或者双引号

#转义 把一些特殊字符变成普通字符 r R \
#换行符 \n
# print("这是第一行\n这是第二行")
# print("这是第一行\\n这是第二行")
# print(r"这是第一行\n这是第二行")
# print(R"这是第一行\n这是第二行")

#python文件里面的输入和输出
# print('hello')  #输出内容到控制台
# # input("请输入内容：") #从控制台获取一个数据 数据类型是字符串
# a = input('输入内容存放在变量a中：')
# print(a)
# print(type(a))

#变量x=1 y=2
#标识符
#一旦你创建了一个变量 然后赋值 就会存储在python内存里面
# a = 1
# print(a) #如果你要用一个变量 在引用之前 要确定是否已经定于并且赋值

#变量命名规范：字母 下划线 数字组成 命名的时候 不能以数字开头 都是小写字母

#python常见的数据类型
#数字 字符串 元组 列表 字典
#数字：整数 浮点数

#python里面常用的数字的数据 int float 关键字
# a = 1
# #type() 可以帮你判断数据的类型
# b = 2.009
# print(type(b))
# print('%d'%a) #是格式化输出

