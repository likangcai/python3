#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-24 18:20
# @Software: PyCharm
# @File    : class_glob.py
'''
glob模块是最简单的模块之一，内容非常少。用它可以查找符合特定规则的文件路径名。跟使用windows下的文件搜索差不多。
查找文件只用到三个匹配符：’’, “?”, “[ ]”。””匹配任意0个或多个字符；”?”匹配任意单个字符；”[ ]”匹配指定范围内的字符，如：[0-9]匹配数字。
不区分大小写
'.'开头的不匹配
'''
import glob
# print(glob.glob(r’ . ./*’) )  # 上一级所有目录
# print(glob.glob("../*"))

# print(glob.glob(r’ ./*’) )  # 本级所有目录
# print(glob.glob("./*"))

# print(glob.glob(r’ ./ . ’) )  # 本级所有文件
# print(glob.glob("./*.*"))

# print(glob.glob(r’ ./ . ’) )  # 本级所有dll
# print(glob.glob("./*.dll"))

# print(glob.glob(r’ C:/ * ') )  # C盘所有目录
# print(glob.glob("c:/*"))

# print(glob.glob(“C:/[PB][RO]”) )  # C盘所有包含pr/po/br/bo的目录
# print(glob.glob("c:/*[PB][RO]*"))

# print(glob.glob(“C:/p？O”) )  # C盘所有包含P_o的目录
# print(glob.glob("c:/*P?O*"))

# print(glob.glob(“C://.txt”) )  # C盘两级目录所有的txt
print(glob.glob("c:/*/*.txt"))



