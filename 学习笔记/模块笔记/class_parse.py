#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-09-04 12:31
# @Software: PyCharm
# @File    : class_parse.py
# 从一段指定的字符串中，取得期望的数据，正常人都会想到正则表达式吧？
# 写过正则表达式的人都知道，正则表达式入门不难，写起来也容易。
# 但是正则表达式几乎没有可读性可言，维护起来，真的会让人抓狂，别以为这段正则是你写的就可以驾驭它，过个一个月你可能就不认识它了。
# 今天介绍一个好东西，可以让你摆脱正则的噩梦，那就是 Python 中一个非常冷门的库 --  parse
# 下面是 ovs 一个条流表，现在我需要收集提取一个虚拟机（网口）里有多少流量、多少包流经了这条流表。也就是每个 in_port 对应的 n_bytes、n_packets 的值 。
# cookie=0x9816da8e872d717d, duration=298506.364s, table=0, n_packets=480, n_bytes=20160,
# priority=10,ip,in_port="tapbbdf080b-c2" actions=NORMAL
# from parse import parse

# flow = 'cookie=0x9816da8e872d717d, duration=298506.364s, table=0, n_packets=480, n_bytes=20160, priority=10,' \
#        'ip,in_port="tapbbdf080b-c2" actions=NORMAL'
# result = parse('cookie={cookie},duration={duration},table={table},n_packets={n_packets},n_bytes={n_bytes},'
#                'priority={priority},ip,in_port="{in_port}" actions={action}', flow)
#
# print(result)
# print(result["in_port"])
# print(result["n_packets"])
# print(result["n_bytes"])

# 2. parse 的结果
# parse 的结果只有两种结果： 没有匹配上，parse 的值为None
# print(parse("halo", "hello") is None)
# # 如果匹配上，parse 的值则 为 Result 实例
# print(parse("hello", "hello world"))
# print(parse("hello", "hello"))

# 如果你编写的解析规则，没有为字段定义字段名，也就是匿名字段， Result 将是一个 类似 list 的实例，演示如下：
# profile = parse("I am {}, {} years old, {}", "I am Jack, 27 years old, male")
# print(profile)
# print(profile[0])
# print(profile[1])
# print(profile[2])

# 而如果你编写的解析规则，为字段定义了字段名， Result 将是一个 类似 字典 的实例，演示如下：
# profile = parse("I am {name}, {age} years old, {gender}", "I am Jack, 27 years old, male")
# print(profile['name'])
# print(profile['age'])
# print(profile['gender'])

# 3. 重复利用 pattern
# 和使用 re 一样，parse 同样支持 pattern 复用。
# from parse import compile
# pattern = compile("I am {}, {} years old, {}")
# print(pattern.parse("I am Jack, 27 years old, male"))
# print(pattern.parse("I am Tom, 26 years old, male"))

# 4. 类型转化
# 从上面的例子中，你应该能注意到，parse 在获取年龄的时候，变成了一个"27" ，这是一个字符串，有没有一种办法，可以在提取的时候就按照我们的类型进行转换呢？
# from parse import parse
# profile = parse("I am {name}, {age:d} years old, {gender}", "I am Jack, 27 years old, male")
# print(profile)
# print(type(profile["age"]))
# # 匹配时间
# print(parse('Meet at {:tg}', 'Meet at 9/2/2020 11:00 PM'))

# 5. 提取时去除空格
# 去除两边空格
from parse import parse

print(parse('hello {} , hello python', 'hello     world    , hello python'))
print(parse('hello {:^} , hello python', 'hello     world    , hello python'))
# 去除左边空格
print(parse('hello {:>} , hello python', 'hello     world    , hello python'))
# 去除右边空格
print(parse('hello {:<} , hello python', 'hello     world    , hello python'))

# 6. 大小写敏感开关
# Parse 默认是大小写不敏感的，你写 hello 和 HELLO 是一样的。
# 如果你需要区分大小写，那可以加个参数，演示如下：
print(parse('SPAM', 'spam'))
print(parse('SPAM', 'spam') is None)
print(parse('SPAM', 'spam', case_sensitive=True) is None)

# 7. 匹配字符数
# 精确匹配：指定最大字符数
print(parse('{:.2}{:.2}', 'hello'))  # 字符数不符
print(parse('{:.2}{:.2}', 'hell'))  # 字符数相符
# 模糊匹配：指定最小字符数
print(parse('{:.2}{:2}', 'hello'))
print(parse('{:2}{:2}', 'hello'))
# 若要在精准/模糊匹配的模式下，再进行格式转换，可以这样写
print(parse('{:2}{:2}', '1024'))
print(parse('{:2d}{:2d}', '1024'))

# 8. 三个重要属性
# Parse 里有三个非常重要的属性
# fixed：利用位置提取的匿名字段的元组
# named：存放有命名的字段的字典
# spans：存放匹配到字段的位置
# 下面这段代码，带你了解他们之间有什么不同
profile = parse("I am {name}, {age:d} years old, {}", "I am Jack, 27 years old, male")
print(profile.fixed)
print(profile.named)
print(profile.spans)

# 9. 自定义类型的转换
# 匹配到的字符串，会做为参数传入对应的函数
# 比如我们之前讲过的，将字符串转整型
print(parse("I am {:d}", "I am 27"))
print(type([0]))
# 其等价于
def myint(string):
    return int(string)
print(parse("I am {:myint}", "I am 27", dict(myint=myint)))
print(type([0]))
# 利用它，我们可以定制很多的功能，比如我想把匹配的字符串弄成全大写
def shouty(string):
    return string.upper()
print(parse('{:shouty} world', 'hello world', dict(shouty=shouty)))

# 10.总结 在一些简单的场景中，使用 parse 可比使用 re 去写正则开发效率不知道高几个 level，用它写出来的代码富有美感，可读性高，后期维护起代码来一点压力也没有，推荐你使用
