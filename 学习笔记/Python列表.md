Python列表操作最全面总结

1.列表添加元素

列表中可以使用append、insert、extend方法实现元素的添加。
append会把新元素添加到列表末尾

    A = ["a", "b", "c"]
    A.append("d")
    print(A)
    输出
    ['a', 'b', 'c', 'd']
insert(index, object) 在指定位置index前插入元素object

    A = ["a", "b", "c"]
    A.insert(0, "d")
    print(A)
    输出
    ['d', 'a', 'b', 'c']
通过extend可以将另一个集合中的元素逐一添加到列表中(合并)

    A = [1, 2]
    B = [3, 4]
    A.extend(B)
    print(A)
    输出
    [1, 2, 3, 4]
2.列表删除元素

列表中使用方法del、pop、remove实现元素删除
del：根据下标进行删除

    list01=["python","java","go"]
    del list01[2]
    print(list01)
    输出
    ['python', 'java']
pop：弹出，删除最后一个元素（默认删除索引为-1的数据）

    list01=["python","java","go"]
    list01.pop()
    print(list01)
    list01.pop(1)
    print(list01)
    输出
    ['python', 'java']
    ['python']
remove：用于移除列表中第一个匹配项

    list01=["python","java","go"]
    list01.remove("java")
    print(list01)
    输出
    ['python', 'go']
3.列表元素的修改

列表可以通过指定下标来访问元素，也可以通过指定列表下标赋值。

    fruits = ["apple", "banana", "cherry"]
    fruits[-1]="pear"
    print(fruits)
    输出
    ['apple', 'banana', 'pear']
4.查找元素

所谓的查找，就是看看指定的元素是否存在，列表中关于查找的方法主要有如下几种：in, not in, index, count
in, not in
in（存在）,如果存在那么结果为true，否则为false
not in（不存在），如果不存在那么结果为true，否则false

    namelist = ['xiaoMing','xiaoZhang','xiaoHua']
    print("xiaoMing" in namelist)
    print("xiaoMing" not in namelist)
    输出
    True
    False
index：从左到右查找，返回符合条件的第一个元素的索引，没有找到，则报错

    namelist = ['xiaoMing', 'xiaoZhang', 'xiaoHua']
    print(namelist.index("xiaoMing"))
    print(namelist.index('xiaoZhang', 0, 2))  # 指定范围，左闭右开
    输出
    0
    1
count：返回要统计的元素在列表中的个数

    A = ["a", "b", "c","a","a"]
    print(A.count("a"))
    输出
    3
5.列表的排序

sort方法是将list按ASCII码排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。
sorted()不会改变原来的list，而是会返回一个新的已经排序好的list
sort()方法仅仅被list所定义，sorted()可用于任何一个可迭代对象，其会返回none

    A = [5, 1, 4, 2, 3]
    A.sort()# 默认从小到大排序
    print(A)
    A.sort(reverse=True) # 从大到小排序
    print(A)
    输出
    [1, 2, 3, 4, 5]
    [5, 4, 3, 2, 1]
6.列表的遍历

    namelist = ['xiaoMing','xiaoZhang','xiaoHua']
    for name in namelist:
        print(name)
7.列表的切片操作

切片操作（slice）可以从一个列表中获取子列表（列表的一部分）。我们使用一对方括号、起始偏移量start、终止偏移量end 以及可选的步长step 来定义一个分片。切片使用 索引值 来限定范围，从一个大的序列 中切出小的序列。
使用方法： 列表[开始索引:结束索引:步长]
开始索引、 结束索引指定的区间属于左闭右开型 [开始索引, 结束索引)，所以不包含索引结束元素。
如果索引从0开始，开始索引数字可以省略，但冒号不能省略。到末尾结束，结束索引数字可以省略，冒号不能省略
正索引从0开始，负索引从-1开始。

    testlist = ['a','b','c','d','e']
    print(testlist[:])#整个列表
    print(testlist[3:])#从testlist[3]到结尾
    print(testlist[:3])#从开始到testlist[3]
    print(testlist[1:3:1])#从第2个到第3个元素，步长1
    print(testlist[:-1])#从开始到倒数第2个元素
    print(testlist[-2:])#从倒数第2个元素到结尾
    print(testlist[::-1])#列表逆序
    输出
    ['a', 'b', 'c', 'd', 'e']
    ['d', 'e']
    ['a', 'b', 'c']
    ['b', 'c']
    ['a', 'b', 'c', 'd']
    ['d', 'e']
    ['e', 'd', 'c', 'b', 'a']
zip(list1,list2) 遍历
enumerate(list1) 
list2.append(e for e in list1)