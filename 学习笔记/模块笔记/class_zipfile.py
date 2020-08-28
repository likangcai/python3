#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-27 21:49
# @Software: PyCharm
# @File    : class_zipfile.py
# ZipFile的compression=缺省是 ZIP_STORED(仅存储不压缩)。
# 所以要指定为ZIP_DEFLATED(zip算法)，或ZIP_LZMA(lzma算法,压缩率高,就是慢了点)
# compresslevel= 要py3.7以上才支持。
# 写入文件，可以用write()，或writestr()
# 用write()，就不需要自己设置文件修改时间了。
# 例子1，创建zip，写注释，改文件的mtime
# import os
# import time
# import zipfile
# from numpy import finfo
#
# orgfilename = "log.txt"
# fstat = os.stat(orgfilename)  # 获取文件修改时间
# bname = os.path.basename(orgfilename)  # 去掉路径
# comment = 'This is a test comment.\n This is line 2.'  # 限制65535个字节
# # fzip = zipfile.ZipFile(orgfilename+'.zip','w',compression=zipfile.ZIP_DEFLATED)  # py<=3.6
# fzip = zipfile.ZipFile(orgfilename + '.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6)  # py>=3.7
# fzip.comment = comment.encode('utf-8')  # bytes,写入zip本身的comment. 无论什么时候写入,都是存在zip文件的末尾。
# with open(orgfilename, 'rb') as fin:
#     fzip.writestr('mydir/' + bname, fin.read())  # 把文件压缩写入zip。加了一层目录mydir在zip中.
# fzip.writestr('mydir/' + bname)  # 获取这个文件的info
# # 因为文件是通过writestr()写入的,所以文件修改时间需要自己设置。否则为当前时间。
# finfo.date_time = time.localtime(fstat.st_mtime)[0:6]  # 文件修改时间
# finfo.comment = comment.encode('utf-8')  # bytes, 写入对应文件的comment.实际存在文件的末尾。
# fzip.close()  # zip文件创建完成

# 例子2，注释中写 json 格式
# import json
#
# # zip文件的注释可以这么用
# COMM = {}
# COMM['d1'] = 123
# COMM['f1'] = 3.25
# COMM['s1'] = 'abcdefg'
# comment = json.dumps(COMM, indent=2)  # 用indent好看点
# fzip.comment = comment.encode('utf-8')  # bytes,写入zip本身的comment

# 例子3，读zip，读注释，解压文件
import json
import zipfile
from io import BytesIO

zipname = '123.zip'
fzip = zipfile.ZipFile(zipname, 'r')  # 打开zip文件
comm = fzip.comment.decode('utf-8')  # zip自身的注释,读取速度比较快
print('===> zip comment:')
print(comm)
zipdata = json.loads(comm)  # 获取comment中的json数据
print('===> data from json:')
print(repr(zipdata))
names = fzip.namelist()  # 获取压缩文件中的文件列表
finfo = fzip.getinfo(names[0])  # 读取第一个文件的属性
print('===> mtime of file:')
print('%02d-%02d-%02d %02d:%02d:%02d' % finfo.date_time)  # 文件修改时间
print('===> comment of file:')
print(finfo.comment.decode('utf-8'))  # 文件的注释
fout = BytesIO(fzip.read(names[0]))  # 读取第一个文件内容,放入内存. (也可以解压到磁盘去)
fzip.close()
fout.close()
