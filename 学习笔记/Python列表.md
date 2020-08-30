Python�б������ȫ���ܽ�

1.�б����Ԫ��

�б��п���ʹ��append��insert��extend����ʵ��Ԫ�ص���ӡ�
append�����Ԫ����ӵ��б�ĩβ

    A = ["a", "b", "c"]
    A.append("d")
    print(A)
    ���
    ['a', 'b', 'c', 'd']
insert(index, object) ��ָ��λ��indexǰ����Ԫ��object

    A = ["a", "b", "c"]
    A.insert(0, "d")
    print(A)
    ���
    ['d', 'a', 'b', 'c']
ͨ��extend���Խ���һ�������е�Ԫ����һ��ӵ��б���(�ϲ�)

    A = [1, 2]
    B = [3, 4]
    A.extend(B)
    print(A)
    ���
    [1, 2, 3, 4]
2.�б�ɾ��Ԫ��

�б���ʹ�÷���del��pop��removeʵ��Ԫ��ɾ��
del�������±����ɾ��

    list01=["python","java","go"]
    del list01[2]
    print(list01)
    ���
    ['python', 'java']
pop��������ɾ�����һ��Ԫ�أ�Ĭ��ɾ������Ϊ-1�����ݣ�

    list01=["python","java","go"]
    list01.pop()
    print(list01)
    list01.pop(1)
    print(list01)
    ���
    ['python', 'java']
    ['python']
remove�������Ƴ��б��е�һ��ƥ����

    list01=["python","java","go"]
    list01.remove("java")
    print(list01)
    ���
    ['python', 'go']
3.�б�Ԫ�ص��޸�

�б����ͨ��ָ���±�������Ԫ�أ�Ҳ����ͨ��ָ���б��±긳ֵ��

    fruits = ["apple", "banana", "cherry"]
    fruits[-1]="pear"
    print(fruits)
    ���
    ['apple', 'banana', 'pear']
4.����Ԫ��

��ν�Ĳ��ң����ǿ���ָ����Ԫ���Ƿ���ڣ��б��й��ڲ��ҵķ�����Ҫ�����¼��֣�in, not in, index, count
in, not in
in�����ڣ�,���������ô���Ϊtrue������Ϊfalse
not in�������ڣ��������������ô���Ϊtrue������false

    namelist = ['xiaoMing','xiaoZhang','xiaoHua']
    print("xiaoMing" in namelist)
    print("xiaoMing" not in namelist)
    ���
    True
    False
index�������Ҳ��ң����ط��������ĵ�һ��Ԫ�ص�������û���ҵ����򱨴�

    namelist = ['xiaoMing', 'xiaoZhang', 'xiaoHua']
    print(namelist.index("xiaoMing"))
    print(namelist.index('xiaoZhang', 0, 2))  # ָ����Χ������ҿ�
    ���
    0
    1
count������Ҫͳ�Ƶ�Ԫ�����б��еĸ���

    A = ["a", "b", "c","a","a"]
    print(A.count("a"))
    ���
    3
5.�б������

sort�����ǽ�list��ASCII�����У�Ĭ��Ϊ��С���󣬲���reverse=True�ɸ�Ϊ�����ɴ�С��
sorted()����ı�ԭ����list�����ǻ᷵��һ���µ��Ѿ�����õ�list
sort()����������list�����壬sorted()�������κ�һ���ɵ���������᷵��none

    A = [5, 1, 4, 2, 3]
    A.sort()# Ĭ�ϴ�С��������
    print(A)
    A.sort(reverse=True) # �Ӵ�С����
    print(A)
    ���
    [1, 2, 3, 4, 5]
    [5, 4, 3, 2, 1]
6.�б�ı���

    namelist = ['xiaoMing','xiaoZhang','xiaoHua']
    for name in namelist:
        print(name)
7.�б����Ƭ����

��Ƭ������slice�����Դ�һ���б��л�ȡ���б��б��һ���֣�������ʹ��һ�Է����š���ʼƫ����start����ֹƫ����end �Լ���ѡ�Ĳ���step ������һ����Ƭ����Ƭʹ�� ����ֵ ���޶���Χ����һ��������� ���г�С�����С�
ʹ�÷����� �б�[��ʼ����:��������:����]
��ʼ������ ��������ָ����������������ҿ��� [��ʼ����, ��������)�����Բ�������������Ԫ�ء�
���������0��ʼ����ʼ�������ֿ���ʡ�ԣ���ð�Ų���ʡ�ԡ���ĩβ�����������������ֿ���ʡ�ԣ�ð�Ų���ʡ��
��������0��ʼ����������-1��ʼ��

    testlist = ['a','b','c','d','e']
    print(testlist[:])#�����б�
    print(testlist[3:])#��testlist[3]����β
    print(testlist[:3])#�ӿ�ʼ��testlist[3]
    print(testlist[1:3:1])#�ӵ�2������3��Ԫ�أ�����1
    print(testlist[:-1])#�ӿ�ʼ��������2��Ԫ��
    print(testlist[-2:])#�ӵ�����2��Ԫ�ص���β
    print(testlist[::-1])#�б�����
    ���
    ['a', 'b', 'c', 'd', 'e']
    ['d', 'e']
    ['a', 'b', 'c']
    ['b', 'c']
    ['a', 'b', 'c', 'd']
    ['d', 'e']
    ['e', 'd', 'c', 'b', 'a']
zip(list1,list2) ����
enumerate(list1) 
list2.append(e for e in list1)