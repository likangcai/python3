#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-23 21:46
# @Software: PyCharm
# @File    : class_hashlib.py
'''
一：hashlib简介
1、什么叫hash: hash是一种算法（不同的hash算法只是复杂度不一样）
（3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法），该算法接受传入的内容，经过运算得到一串hash值
2、hash值的特点是(hash值/产品有三大特性：)：
    2.1、只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
    2.2、不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码（只能有内容返回hash值）
    2.3、只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的(如从网上下载文件要进行hash校验，保证网络传输没有丢包)
基于2.1和2.3可以做文件下载一致性的校验
基于2.1和2.2可以对用户密码进行加密
hash算法就像一座工厂，工厂接收你送来的原材料（可以用m.update()为工厂运送原材料），经过加工返回的产品就是hash值
'''
# 二：将指定的 “字符串” 进行加密。使用hashlib的分步解析
# 1）在进行md5哈希运算前，需要对数据进行编码，否则报错
# import hashlib
# obj = hashlib.md5()  # 构造一个hashlib的对象
# obj.update("小马过河")  # update 对指定字符串进行加密
# print(obj)

# 2）obj是hash对象
# import hashlib
# obj = hashlib.md5()
# obj.update("小马过河".encode("utf-8"))
# print(obj, type(obj))

# 3) hexdigest() 返回摘要，作为十六进制数据字符串值   hash.digest() 返回摘要，作为二进制数据字符串值
# import hashlib
# obj = hashlib.md5()
# obj.update("小马过河".encode("utf-8"))
# result = obj.hexdigest()
# print(result)

# 4）给加密增添难度
# import hashlib
# obj = hashlib.md5("mcw@xiaoma@aaaafffff".encode("utf-8"))  # 添加一些内容，提高加密复杂度。此处的字符串也要先编码，
# obj.update("小马过河".encode('utf-8'))
# result = obj.hexdigest()
# print(result)

# 5）用hashlib做成加密函数（添加基础的字符了的）
# import hashlib


# def get_md5(data):  # 传参为需要加密的字符串
#     obj = hashlib.md5("sidrsicxwersdfsaersdfsdfresdy54436jgfdsjdxff123ad".encode('utf-8'))
#     obj.update(data.encode('utf-8'))
#     result = obj.hexdigest()
#     return result
#
#
# val = get_md5('123')
# print(val)

# 三：应用场景案例：用户账号密码登录，对明文密码进行加密
# import hashlib
#
# USER_LIST = []
#
#
# def get_md5(data):
#     obj = hashlib.md5("12:;idrsicxwersdfsaersdfsdfresdy54436jgfdsjdxff123ad".encode('utf-8'))
#     obj.update(data.encode('utf-8'))
#     result = obj.hexdigest()
#     return result
#
#
# def register():
#     print('**************用户注册**************')
#     while True:
#         user = input('请输入用户名:')
#         if user == 'N':
#             return
#         pwd = input('请输入密码:')
#         temp = {'username': user, 'password': get_md5(pwd)}
#         USER_LIST.append(temp)
#
#
# def login():
#     print('**************用户登陆**************')
#     user = input('请输入用户名:')
#     pwd = input('请输入密码:')
#     for item in USER_LIST:
#         if item['username'] == user and item['password'] == get_md5(pwd):
#             return True
#
#
# register()
# result = login()
# if result:
#     print('登陆成功')
# else:
#     print('登陆失败')

'''
用户登录场景分析：实现用户注册，然后进行用户登录的代码分析。
代码分析：
1、用户登录需要使用密码，密码一定要加密，保证用户的信息安全。
　　1）加密可以使用hashlib模块进行加密。
　　2）加密可以写成加密函数
　　3）提高密码解密的复杂性，代码中多加字符串。（加密算法虽然依然非常厉害，但是也存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。）
2、用户注册写成用户注册的函数，用户登录写成用户登录的函数。
3、先执行用户注册的函数，再执行用户登录的函数
4、注册与登录需要交互，用到input函数接收用户输入
5、如果用户注册和用户登录用到死循环，那么就要判断用什么来终止循环（比如这里是输入N）
6、用户注册提交的密码加密的密文写入数据库。、用户注册提交的密码加密的密文写入数据库。
7、用户登录输入的密码，使用相同加密函数加密后与数据库密文比对，相等就登录，否则就失败
8、登录的本质是判断从用户接收的加密后密文和注册时存入数据库的密文对比，用户名密文对比成功，则继续往下执行登录后的操作。
9、用户输入密码要防止旁人看到，可以使用getpass模块
10、与密码相关的很重要，一定要加密。包括自己拥有的影响大的重要数据也要加密，防止黑客入侵获取而泄密。
'''
# 四、校验文件的一致性（如何保证下载的文件过程中不丢包，保证下载数据的完整性）

# -----------文件一致校验----------------
'''可以拷贝一个文件放在两个不同的盘中，然后通过判断两个文件的hash值是否相等，判断两个文件是否是同一个文件'''
# import hashlib
# m = hashlib.md5()
# with open(r'G:/logging模块配图.png','rb') as f:
#     for line in f:
#         m.update(line)
# print(m.hexdigest())
#
# import hashlib
# m = hashlib.md5()
# with open(r'H:/logging模块配图.png','rb') as f:
#     for line in f:
#         m.update(line)
# print(m.hexdigest())

# 五、对明文密码进行加密

# 应用：对明文密码进行加密（暴力破解-------用明文密码用一种算法算出一个hash值，与截取的hash值进行比对，比对成功说明明文密码一致，就可以破解用户的密码）
'''如用户在某网站进行注册信息，这个时候防止信息被恶意拦截获取，可以对用户明文密码进行加密，存成hash值得形式，这样用户每次登陆虽然输的是明文密码，校验hash值即可'''
# password = input('>>>>>:').strip()
# import hashlib
#
# m = hashlib.md5()
# m.update(password.encode('utf-8'))
# print(m.hexdigest())
#
# # 对密码进行加盐（暗号）----------进一步加强密码的安全性
# password = input('>>>>>:').strip()
# import hashlib
#
# m = hashlib.md5()
# m.update('一行白鹭上青天'.encode('utf-8'))  # 对密码加盐
# m.update(password.encode('utf-8'))
# print(m.hexdigest())

# 六、破解用户注册的密码
'''
# 模拟撞库破解密码
import hashlib

passwds = [  # 可以通过random实现对passwds中的内容
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
]


def make_passwd_dic(passwds):  # 通过明文密码列表，造出与之对应的hash值得字典
    dic = {}
    for passwd in passwds:
        m = hashlib.md5()  # 使用md5算法，造了一个工厂
        m.update(passwd.encode('utf-8'))  # 给工厂运送原材料(即我们要加密的内容)
        dic[passwd] = m.hexdigest()  # 产出hash值（即最终的产品），将其加入到我们事先造好的空字典中，字典形式:{密码：hash值}
    return dic


def break_code(cryptograph, passwd_dic):  # 判断拦截的hash值是否与字典中事先造好的hash值相等，相等则说明成功进行破解
    for k, v in passwd_dic.items():
        if v == cryptograph:
            print('密码是===>\033[46m%s\033[0m' % k)


cryptograph = 'aee949757a2e698417463d47acac93df'  # 我们拦截拿到的密码，经过加密的hash值
break_code(cryptograph, make_passwd_dic(passwds))  # 将要破解的密码hash值，和事先造好的hash的字典当做函数的实参传给对应的形参
'''

# 七、hmac模块的加密方式，与hashlib类似
'''python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 进行进一步的处理然后再加密:'''
import hmac

h = hmac.new('天王盖地虎'.encode('utf8'))  # hmac必须要加盐
h.update('hello'.encode('utf8'))
print(h.hexdigest())
# 要想保证hmac最终结果一致，必须保证：
# 1:hmac.new括号内指定的初始key一样
# 2:无论update多少次，校验的内容累加到一起是一样的内容
# 下面单重方式得到的结果是一样的
import hmac

h1 = hmac.new(b'tom')  # 初始值必须保证一致，最终得到的结果就会不一样
h1.update(b'hello')
h1.update(b'world')
print(h1.hexdigest())
h2 = hmac.new(b'tom')  # 初始值必须保证一致，最终得到的结果就会不一样
h2.update(b'helloworld')
print(h2.hexdigest())
h3 = hmac.new(b'tomhelloworld')  # 初始值不一样，所以与上面两种的结果不一样
print(h3.hexdigest())
