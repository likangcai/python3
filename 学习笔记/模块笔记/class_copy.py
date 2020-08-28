#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 影子
# @Time    : 2020-08-28 19:07
# @Software: PyCharm
# @File    : class_copy.py
# 1.浅拷贝(Shallow Copies)
# copy() 创建的 浅拷贝 是一个新的容器，它包含了对原始对象的内容的引用。也就是说仅拷贝父对象，不会拷贝对象的内部的子对象。
# 即浅复制只复制对象本身，没有复制该对象所引用的对象。比如,当创建一个列表对象的浅拷贝时，将构造一个新的列表，并将原始对象的元素添加给它。
# import copy
#
#
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         return self.name == other.name
#
#     def __gt__(self, other):
#         return self.name > other.name
#
#
# a = MyClass('a')
# my_list = [a]
# dup = copy.copy(my_list)
# print('             my_list:', my_list)
# print('                 dup:', dup)
# print('      dup is my_list:', (dup is my_list))
# print('      dup == my_list:', (dup == my_list))
# print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
# print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))
# 上面的浅拷贝实例中，dup 是由 my_list 拷贝而来, 但是 MyClass 实例不会拷贝，所以 dup 列表与 my_list 中引用的是同一个对象。

# 2.深拷贝(Deep Copies)
# deepcopy() 创建的 深拷贝 是一个新的容器，它包含了对原始对象的内容的拷贝。深拷贝完全拷贝了父对象及其子对象。
# 即创建一个新的组合对象，同时递归地拷贝所有子对象，新的组合对象与原对象没有任何关联。虽然实际上会共享不可变的子对象，但不影响它们的相互独立性。
# 将上面代码换成 deepcopy()，将会发现其中不同:
# import copy
#
#
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         return self.name == other.name
#
#     def __gt__(self, other):
#         return self.name > other.name
#
#
# a = MyClass('a')
# my_list = [a]
# dup = copy.deepcopy(my_list)
# print('             my_list:', my_list)
# print('                 dup:', dup)
# print('      dup is my_list:', (dup is my_list))
# print('      dup == my_list:', (dup == my_list))
# print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
# print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))
# 列表中的 MyClass 实例不再是同一个的对象引用，而是重新复制了一份, 但是当两个对象被比较时，它们的值仍然是相等的。

# 3.自定义拷贝行为
# 可以通过自定义 __copy__() 和 __deepcopy__() 方法来改变默认的拷贝行为。  __copy()__ 是一个无参数方法，它返回一个浅拷贝对象；
# __deepcopy()__ 接受一个备忘(memo)字典参数,返回一个深拷贝对象。需要进行深拷贝的成员属性都应该传递给 copy.deepcopy() ，
# 以及memo字典，以控制递归。(下面例子将解释memo字典)。
# 下面的示例演示如何调用这些方法：
# import copy
# class MyClass:
#     def __init__(self,name):
#         self.name = name
#
#     def __eq__(self, other):
#         return self.name == other.name
#
#     def __gt__(self, other):
#         return self.name > other.name
#
#     def __copy__(self):
#         print('__copy__()')
#         return MyClass(self.name)
#
#     def __deepcopy__(self, memo):
#         print('__deepcopy__({})'.format(memo))
#         return MyClass(copy.deepcopy(self.name,memo))
#
#
# a = MyClass('a')
# sc = copy.copy(a)
# dc = copy.deepcopy(a)
# memo字典用于跟踪已经拷贝的值，以避免无限递归

# 4.深拷贝中的递归
# 为了避免拷贝时有递归数据结构的问题， deepcopy()`` 使用一个字典来跟踪已经拷贝的对象。这个字典被传递给deepcopy()` 方法进行检查。
# 下面示例展示了一个相互关联的数据结构(有向图)，如何通过实现 __deepcopy__() 方法来防止递归。
import copy


class Grapth:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return 'Graph(name={}, id={})'.format(self.name, id(self))

    def __deepcopy__(self, memo):
        print('\nCalling __deepcopy__ for {!r}'.format(self))
        if self in memo:
            existing = memo.get(self)
            print('  Already copied to {!r}'.format(existing))
            return existing
        print('  Memo dictionary:')
        if memo:
            for k, v in memo.items():
                print('    {}: {}'.format(k, v))
        else:
            print('    (empty)')
        dup = Grapth(copy.deepcopy(self.name, memo), [])
        print('  Copying to new object {}'.format(dup))
        memo[self] = dup
        for c in self.connections:
            dup.add_connection(copy.deepcopy(c, memo))
        return dup


root = Grapth('root', [])
a = Grapth('a', [root])
b = Grapth('b', [a, root])
root.add_connection(a)
root.add_connection(b)
dup = copy.deepcopy(root)
# Graph 类包括一些基本的有向图方法。可以用一个名称和它所连接的现有节点的列表来初始化一个实例。 add_connection() 方法用于设置双向连接。它也被深拷贝操作符使用。
# __deepcopy__() 方法打印了它的调用信息，并根据需要管理memo字典内容。它不会复制整个连接列表，而是创建一个新的列表，并将单个连接的副本添加进去。
# 确保在每个新节点被复制时更新memo字典，并且避免递归或重复拷贝节点。与以前一样，该方法在完成时返回拷贝的对象。
# 第二次遇到根节点时，如果一个节点被已拷贝时， __deepcopy__() 检测递归，并从memo字典中重用现有的值，而不是创建一个新对象。
