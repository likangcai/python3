#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-18 22:53
# @Software: PyCharm
# @File    : class_04.py

# 1.变量  可以把变量简单理解为一个存储值的单词。
# 在Python里面，定义变量、给变量赋值都非常简单。比如你想把数字1存储到一个变量里面，而这个变量名叫one，
one = 1
# 除了整型以外，我们也可以设置布尔类型、字符串、单精度，以及一些其他数据类型
# 布尔类型 booleans
true_boolean = True
false_boolean = False

# 字符串类型 string
my_name = "Ying zi"

# 浮点数  float
book_price = 15.52

# 2.流程控制: 分支语句 if，这个语句用来判断是否符合条件，它的后面紧跟着逻辑表达式，表达式最后的值为True或False，如果是true，则执行if里面的语句。
if True:
    print("Hello python if")

if 2 > 1:
    print("2 is greater than 1")

# 当然，如果不满足条件，那么else就派上用场了！ 如果，if后面跟着的逻辑表达式最终值是false，则会运行else里面的程序
if 1 > 2:
    print("1 is greater than 2")
else:
    print("1 is not greater than 2")

# 也可以使用elif，是else if的缩写
if 1 > 2:
    print("1 is greater than 2")
elif 2 > 1:
    print("1 is not greater than 2")
else:
    print("1 is equal to 2")

# 3. 循环 / 迭代器  在Python中，我们有多种迭代的方式，我在这里说两种：
# While 循环: 当逻辑表达式为true的时候，while下缩进的代码块就会被循环执行. 所以下面的代码片段，将会从1打印到10
num = 1
while num < 10:
    print(num)
    num += 1  # num = num + 1
# 上面这种循环方式，需要一个循环条件，如果循环条件是true，就会继续进行迭代，在上面的例子中，当num变成11的时候，循环条件就会等于False"
loop_condition = True
while loop_condition:
    print("Loop Condition keeps: %s" % (loop_condition))
    loop_condition = False
# 只要循环条件为True，就会被一直循环执行，直到循环条件变成False
# For循环: 与其他语言一样，这用于计次循环，它循环的次数，取决于后面那个range方法
# range，代表从在循环里，它用于表示从x到n，如下，就是从1到11，第三个参数可空，意思是每次递进的加数，默认每循环一次给i加1，填2的话，就给i加2
for i in range(1, 11, 1):
    print(i)

# 列表: 集合 | 数组 | 数据结构   List 是一个可以用来存储一列值的集合（比如你想要的这些整数）。那么让我们使用它：
# my_integers = [1,2,3,4,5]
# List 有一个叫做索引的概念。第一个元素获取索引 0 （零）。第二个取 1 ，依此类推。
my_integers = [5, 7, 1, 3, 4]
print(my_integers[0])  # 5
print(my_integers[1])  # 7
print(my_integers[4])  # 4
# 现在你不想存储整数了。你只是想存储字符串
relatives_names = [
    "Toshiaki",
    "Juliana",
    "Yuji",
    "Bruno",
    "Kaio"
]
print(relatives_names[4])  # Kaio
# 如何将一个元素添加到 List 数据结构（一个项目到列表）。添加一个值到 List 最常见的方法是 append 。
bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
print(bookshelf[0])  # The Effective Engineer
print(bookshelf[1])  # The 4 Hour Work Week
# append  非常的简单。您只需要将元素（例如『 The Effective Engineer 』）作为『 append 』参数应用即可。

# 字典: 键-值 数据结构   Lists 使用整数来索引。但是如果我们不想使用整数来索引呢？一些其他的数据结构可以使用数字，字符串或者其他的类型来做索引.
# 让我们来学习 Dictionary 数据结构. Dictionary 是一个键值对集合
dictionary_example = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
# 键用来索引到值
dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian"
}

print("My name is %s" % (dictionary_tk["name"]))  # My name is Leandro
print("But you can call me %s" % (dictionary_tk["nickname"]))  # But you can call me Tk
print("And by the way I'm %s" % (dictionary_tk["nationality"]))  # And by the way I'm Brazilian

# 我创建了一个关于我的 Dictionary. 我的名字，昵称和国籍。这些属性是 Dictionary 的键.
# 我们知道访问 List 使用下标，我们在这也使用下标 (  Dictionary 中的键的内容) 来访问存在 Dictionary 中的值.
# 另一件关于 Dictionary 非常帅气的事情就是我们可以使用任何东西来做为字典的值。在我创建的 Dictionary 中，我想添加键为 "age" 且值为我的整数年龄进去
dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian",
    "age": 24
}

print("My name is %s" % (dictionary_tk["name"]))  # My name is Leandro
print("But you can call me %s" % (dictionary_tk["nickname"]))  # But you can call me Tk
print("And by the way I'm %i and %s" % (
    dictionary_tk["age"], dictionary_tk["nationality"]))  # And by the way I'm Brazilian
# 这里我们有一个键 (age) 值 (24) 对 使用字符串来作为键，整数来作为值.
# 像我们学习 Lists 一样，让我们来学习如何在 Dictionary 中添加元素。在 Dictionary 中， 一个键指向一个值是很重要的

dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian"
}

dictionary_tk['age'] = 24
print(dictionary_tk)  # {'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}
# 我们只需要指定一个值到 Dictionary 的键上

# 迭代：循环 Python 中的数据结构
# 当我们在学习 Python 基础时，会发现列表的迭代是一件十分简单的事情 ，通常我们 Python 开发者会使用 For 来循环迭代它
bookshelf = [
    "The Effective Engineer",
    "The 4 hours work week",
    "Zero to One",
    "Lean Startup",
    "Hooked"
]

for book in bookshelf:
    print(book)
# 同样对于哈希类型的数据结构，比如像是 Python 中的字典，我们同样也可以对其使用 for 循环进行迭代操作，但是此时我们则需要用到 key
dictionary = {"some_key": "some_value"}
for key in dictionary:
    print("%s --> %s" % (key, dictionary[key]))

# 这是一个循环字典类型变量的小例子，对于 dictionary 变量我们使用 for 循环操作其中的 key，接着我们打印输出他的 key 以及其相对应匹配的 value 值。
# 当然我们还有另外一种方法去实现它，就是去使用 iteritems：
dictionary = {"some_key": "some_value"}
for key, value in dictionary.items():
    print("%s --> %s" % (key, value))

# 你看我们已经命名了两个参数 key,value，但这并不是必须的，你甚至可以给它们起任何一个名字
dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian",
    "age": 24
}
for attribute, value in dictionary_tk.items():
    print("My %s is %s" % (attribute, value))
# 可以看到我们已经使用了 attribute 作为了 Dictionary 的 key 参数，代码运行十分正确
'''
类型与对象
一点基础理论:
对象代表现实世界中像轿车、狗、自行车这些事物。对象具有数据和行为两个主要特征。
在面向对象编程中，我们把数据当作属性，把行为当作方法。即：
数据 → 属性 和 行为 → 方法
类型是创造单个对象实例的蓝本。在现实世界中，我们经常发现很多对象实例拥有相同的类型，比如轿车。他们都具有相同的构造和模型（具有发动机，轮子，门等等）。
每辆车都是根据同一张设计图制作的，并且具有相同的组成部分。
Python 的面向对象编程模式：ON   Python，作为一门面向对象编程的语言，具有类和对象的概念。
类是蓝图，对象是模型。
同样，一个类，它只是一个模型，或者一种定义属性和行为的方法（正如我们在理论部分所讨论的）。例如，车辆类有自己的属性，定义什么是车辆。
车轮的数量、能源的类型、座位容量和最大速度都是车辆的属性。
考虑到这一点，让我们看看类的 Python 语法：
'''


# 我们用一个类声明来定义类 ，仅此而已
class Vehicle:
    pass  # 占位符


# 对象是一个类的实例，我们用命名类来创建一个实例。
car = Vehicle()
print(car)


# 这里 ‘car’ 是 ‘Vehicle’ 类的一个对象（或者说实例）
# 我们的 ‘Vehicle’ 类有四个属性：轮子数量，能源类型，座位容量，和最大速度。我们创建一个 ‘Vehicle’ 对象时设置所有这些属性
# 定义我们的类初始化时要接收数据时
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity


# 我们使用了 ‘init’方法。我们称它为构造方法。所以创建 ‘vehicle’ 对象时可以定义这些属性。假设我们喜欢 Tesla Model S，我们要创建这种对象。
# 它有 4 个轮子，使用电能，有 5 个座位，最大时速 250km/h (155mph）
tesla_model_s = Vehicle(4, 'electric', 5, 250)


# 所有属性都设置完成了。但是我们如何获取这些属性值？我们发送一个消息到对象来问他们。 我们称之为方法。方法是对象的行为。
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def number_of_wheels(self):
        return self.number_of_wheels

    def set_number_of_wheels(self, number):
        self.number_of_wheels = number


# 这里创建了两个方法:number_of_wheels和set_number_of_wheels.我们称它为获取&设置.因为第一个获取了属性值，然后第二个设置了一个新的属性值。

# Python 中，我们可以用 “@property” (“decorator”) 去定义 "getters" 和 “setters”。
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    @property
    def number_of_wheels(self):
        return self.number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.number_of_wheels = number


# 同时，我们可以使用这些方法作为属性：

tesla_model_s = Vehicle(4, 'electric', 5, 250)
print(tesla_model_s.number_of_wheels)
tesla_model_s.number_of_wheels = 2
print(tesla_model_s.number_of_wheels)


# 这个与定义方法有些许不同。这些方法的工作机制与属性不同。例如，当我们设置轮子数量时，我们需要把 2 赋值给一个变量，只需要设
# 置 “number_of_wheels” 的值为 2。这是一种写 “pythonic”、 ”getter“、“setter” 代码的方法。

# 而且同时我们也可以使用其他方法，比如 “make_noise” 方法
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def make_noise(self):
        print('VRUUUUUUUM')


tesla_model_s = Vehicle(4, 'electric', 5, 250)
tesla_model_s.make_noise()

'''
封装：信息隐藏
封装是一种限制直接访问对象数据和方法的机制。但是它加快了对象方法中数据的访问。
" 封装可以在定义中隐藏数据和函数成员，意味着从外部隐藏了对象定义中的内部描述 “--- Wikipedia
对象从外部隐藏了其内部描述。只有对象可以与它的内部数据进行交互。
首先，我们需要了解 “public” 和 “non-public” 变量实例的工作机制。
Public 变量实例  对于一个 Python 类型，我们可以使用构造方法初始化一个公共变量实例。我们看这个：
'''


# 构造方法
class Person:
    def __init__(self, first_name):
        self.first_name = first_name


# 这里我们使用 “first_name” 的值作为一个参数传递给公共变量实例。

tk = Person('TK')
print(tk.first_name)


# 在类中：
class Person:
    first_name = 'TK'


# 这里，我们不需要使用 “first_name” 作为一个参数，所有的对象实例都有一个用 “TK” 初始化的类属性。
tk = Person()
print(tk.first_name)

# 记住 “Person” 类，我们想要设置另一个值给它的 “first_name” 变量：
tk = Person('TK')
tk.first_name = 'Kaio'
print(tk.first_name)  # => Kaio
# 好了，我们刚刚设置了另一个值（"kaio"）给对象变量 “first_name”，并且它更新了它的值。就是这么简单，因为这个 “public” 变量，我们可以这样做。

'''
Non-public 变量实例
“在这里，我们不用‘私有‘来形容 ，因为在 Python 中没有真正 “私有” 的属性（避免了一般情况下不必要的工作）。”--- PEP 8
和公共变量实例一样，我们可以在构造函数或类内部定义非公共变量实例。语法上的差异是： 对于非公共变量实例，我们在变量名前加一道下划线 (_)。
“在 Python 中，无法从内部访问‘私有’变量实例的对象是不存在的。但是，大多数 Python 代码遵循一个惯例：一个名字前有一道下划线的对象应该被认为
是 API 中非公共的部分，例如_spam，无论它是一个函数、方法或是数据成员。” --- Python Software Foundation
'''


class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email


# 看到 email 变量了吗？这就是定义一个非公共变量的方法。

tk = Person('TK', 'tk@mail.com')
print(tk._email)


# 所谓非公共变量只是一个惯例，没有机制禁止我们从外部访问并更新它。但按照惯例，我们应该把它作为 API 中非公共的部分来对待。
# 在类内部，我们通常使用方法来操作 “非公共变量”，让我们实现两个方法（email 和 update_email）来理解。
class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email

    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email


# 现在，我们可以通过这些方法来访问、更新非公共变量。

tk = Person('TK', 'tk@mail.com')
print(tk.email())
tk._email = 'new_tk@mail.com'
print(tk.email())
tk.update_email('new_tk@mail.com')
print(tk.email())
'''
我们以 first_name TK 和 email tk@mail.com 初始化一个 Person 对象。
通过方法访问非公共变量 email，并打印出来。
从类外部直接设置一个新的 email。
我们应该把非公共变量作为 API 中非公共的部分来对待。
通过实例方法更新非公共变量 email。
成功！我们可以通过预设的方法来更新它。
'''


# 公共方法
# 通过 公共方法 , 我们也可以在我们类的外部使用这些方法了：

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._age


# 让我们来试下：

tk = Person('TK', 25)
print(tk.show_age())


# 非公共方法
# 但是通过 非公共方法 我们却无法做到这一点。 我们先来实现一个同样的 Person 类，不过这回我们加个下划线 (_) 来定义一个 show_age 的非公共方法。

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def _show_age(self):
        return self._age


# 那么现在，我们来试着通过我们的对象调用这个 非公共方法：

tk = Person('TK', 25)
print(tk._show_age())


# 我们可以访问并且更新它。 非公共方法 只是一类约定俗成的规定，并且应当被看做接口中的非公共部分。
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._get_age()

    def _get_age(self):
        return self._age


tk = Person('TK', 25)
print(tk.show_age())  # => 25

# 这里我们有一个 _get_age 非公共方法和一个 show_age 公共方法。show_age 可以由我们的对象调用（在类的外部）而_get_age 只
# 能在我们类定义的内部使用 (内部 show_age 方法)。但是再次强调下，这只是个约定俗成的规定。

'''
封装总结
通过封装我们可以从外部隐藏对象的内部表示。
继承：行为和特征
某些对象具有共同点：如行为和特征。
例如，我从我父亲那里继承了一些特征和行为。我继承了他的眼睛和头发作为特征，继承了他的急躁和内向作为行为。
在面向对象编程中，类能够从其他类中继承特征（数据）和行为（方法）。
'''


# 假定一辆车。轮子的数量、载客量和最高时速是车的所有属性。那么我们可以认为 ElectricCar 类从这个 Car 类中继承了这些属性。

class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity


# 我们的 Car 类实现之后:

my_car = Car(4, 5, 250)
print(my_car.number_of_wheels)
print(my_car.seating_capacity)
print(my_car.maximum_velocity)


# 在 Python 中我们可以将父类作为子类定义时的参数。一个 ElectricCar 类能从之前的 Car 类中继承。

class ElectricCar(Car):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)


# 简单如上。我们不需要实现任何其他的方法，因为这个类已经有了（继承自 Car 类）。让我们确认一下：

my_electric_car = ElectricCar(4, 5, 250)
print(my_electric_car.number_of_wheels)
print(my_electric_car.seating_capacity)
print(my_electric_car.maximum_velocity)
