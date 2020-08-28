#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-28 19:40
# @Software: PyCharm
# @File    : class_06_SQLite.py
'''
SQLite是一款轻型的数据库，占用内存非常低，通常只需要几百K的内存就够用了。它将整个数据库，包括定义表、索引以及数据本身，
做为一个单独的可跨平台的文件存储在主机中，并且支持 Python、Java、C# 等多种语言，目前的版本已经发展到了 SQLite3。
Python中内置了SQLite模块，不需要任何配置，可以直接导入使用，下面简单介绍下在Python中操作SQLite数据库。
操作SQLite类似操作mysql数据库，需要执行以下几步：
1.导入sqlite3
2.创建connection连接对象
3.创建游标对象
4.执行SQL语句
5.关闭游标
6.关闭连接
要确保打开的Connection对象和Cursor对象都正确地被关闭，否则可能会出现资源泄露。  SQLite的SQL语法与mysql基本一致。
'''
# 创建数据库
# 执行完毕，会在当前目录产生一个db文件。
# import sqlite3
# # 创建连接对象
# con = sqlite3.connect('test.db')
# # 创建游标对象
# cur = con.cursor()
# # 执行SQL
# cur.execute('CREATE TABLE `students` (id int(10) PRIMARY KEY,name varchar(20),no int(20))')
# # 关闭游标
# cur.close()
# con.close()

# 新增数据
# import sqlite3
#
# # 创建连接对象
# con = sqlite3.connect('test.db')
# # 创建游标对象
# cur = con.cursor()
# # 新增单条数据
# # cur.execute('insert into students (id,name,no) values(1,'xiaoming',1001)')
# # 新增多条数据，用executemany()的方法来执行多次插入
# data = [(1, '小明', 1002), (2, '王二', 1002), (3, '张三', 1003)]
# cur.executemany('insert into students (id,name,no) values(?,?,?)', data)
# # 关闭游标
# cur.close()
# # 提交事务
# con.commit()
# # 关闭连接
# con.close()

# 删除数据
# import sqlite3
#
# # 创建连接对象
# con = sqlite3.connect('test.db')
# # 创建游标对象
# cur = con.cursor()
# # 执行SQL
# cur.execute('delete from students where id =3')
# # 提交事务
# con.commit()
# # 关闭游标
# cur.close()
# # 关闭连接
# con.close()

# 修改数据
# import sqlite3
#
# # 创建连接对象
# con = sqlite3.connect('test.db')
# # 创建游标对象
# cur = con.cursor()
# # 执行SQL
# cur.execute('update students set name = "张三" where id = 3')
# # 提交事务
# con.commit()
# # 关闭游标
# cur.close()
# # 关闭连接
# con.close()

# 查询数据
# 查询数据的三种方法：
# fetchone()：获取查询结果集中的一条记录。
# fetchmany(size)：获取指定数据的记录。
# fetchall():获取结果集的所有记录。

import sqlite3

# 创建连接对象
con = sqlite3.connect('test.db')
# 创建游标对象
cur = con.cursor()
# 执行SQL
cur.execute('select * from students')
# 查询结果集中的两条记录
# print(cur.fetchmany(2))
# 查询结果集中的所有记录
print(cur.fetchall())
# 关闭游标
cur.close()
# 关闭连接
con.close()

# 通过Pycharm查看SQLite数据库
# 1.打开Database组件   view--> tool windows-->Database
# 2.关联SQLite数据库   Database-->'+'-->Data Source-->SQLite-->File
# 首次连接需要安装SQLite驱动，直接下载即可。
# 3.关联成功后，就可以直接查看关联的db文件了。
