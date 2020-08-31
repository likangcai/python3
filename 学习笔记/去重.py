#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-31 19:58
# @Software: PyCharm
# @File    : 去重.py
# 10行Python代码自动清理电脑内重复文件，解放双手！
# 「给定一个文件夹，使用Python检查给定文件夹下有无文件重复，若存在重复则删除」
# 主要涉及的知识点有：
# os模块综合应用
# glob模块综合应用
# 利用filecmp模块比较两个文件
# 遍历获取给定文件夹下的所有文件，然后通过嵌套循环两两比较文件是否相同，如果相同则删除后者。
# 如何判断两个文件是否相同？
# 在这里我们可以使用filecmp模块，来看看官方的介绍文档：  filecmp.cmp(f1, f2, shallow=True)
# 比较名为f1和f2的文件，如果它们似乎相等则返回True，否则返回False
# 如果shallow为真，那么具有相同os.stat()签名的文件将会被认为是相等的。否则，将比较文件的内容。
# 假设x和y两个文件是相同的   print(filecmp.cmp(x, y))
# import os
# import glob
# import filecmp
# dir_path = r'C:\\xxxx'

# 遍历获取所有文件的绝对路径，我们可以利用glob模块的通配符结合recursive参数即可完成
# for file in glob.glob(path + '/**/*', recursive=True):
#     pass

# 由于遍历获取每一个文件或者文件夹后，需要判断是否是文件，如果是文件则可能将绝对路径存放到列表中，这里需要再完成两个事情：首先创建一个空列表，
# 后面用list.append(i)添加文件路径 接着利用os.path.isfile(i)判断是否是文件，返回True则执行添加元素的操作

# file_lst = []
# for i in glob.glob(dir_path + '/**/*', recursive=True):
#     if os.path.isfile(i):
#         file_lst.append(i)
# 上一步我们获取了目标文件夹下的所有文件路径，接下来就可以嵌套遍历这个路径列表，其中filecmp.cmp进行文件判断，os.remove进行文件删除

# for x in file_lst:
#     for y in file_lst:
#         if x != y:
#             if filecmp.cmp(x, y):
#                 os.remove(y)
# 这里的代码已经实现了大致逻辑，但有一个细节需要考虑到：有可能循环到文件已经被前面的判断删除了，导致os.remove(file)由于文件不存在而报错

# 因此，可以用os.path.exists对文件存在进行判断
# for x in file_lst:
#     for y in file_lst:
#         if x != y and os.path.exists(x) and os.path.exists(y):
#             if filecmp.cmp(x, y):
#                 os.remove(y)

import os
import glob
import filecmp

dir_path = r"H:\quchong"  # 目标文件夹路径
file_lst = []
for i in glob.glob(dir_path + '/**/*', recursive=True):
    if os.path.isfile(i):
        file_lst.append(i)

for x in file_lst:
    for y in file_lst:
        if x != y and os.path.exists(x) and os.path.exists(y):
            if filecmp.cmp(x, y):
                os.remove(y)
