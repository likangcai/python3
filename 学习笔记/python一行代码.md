Python 只用一行代码，可以实现哪些事儿？

今天我们来玩玩，只用一行 Python 代码或命令，看下可以玩些什么。比如我们之前就玩过一行 Python 命令实现 http 服务：

    HTTP 服务器
    python3 -m http.server
    python3 -m http.server 6321

FTP 服务器
再给你介绍个，你可以使用 pyftpdlib 来直接实现一个 FTP 服务器进行文件传输：

    python3 -m pyftpdlib
    ftp://127.0.0.1:2121
    可选参数
    -i 指定IP地址（默认为本机的IP地址）
    -p 指定端口（默认为2121）
    -w 写权限（默认为只读）
    -d 指定目录 （默认为当前目录）
    -u 指定用户名登录
    -P 设置登录密码
    
格式化 Json
可以使用 json.tool 来格式化 Json：

    cat 12.json | python -m json.tool
    
python -c
使用这个 -c 参数可以直接在终端中使用 Python 简单的代码：

    python -c "a=[i for i in range(6)]; print(a)"
    
一行代码实现函数
使用 lambda 可以用一行代码实现一个匿名函数，比如想要将列表中的元素进行计算操作，可以直接这样：

    print(list(map(lambda x:x*2,[1,2,3,4,5])
    
变量交换
一行代码交换两变量，老生常谈了：

    a = 1
    b = 2
    a,b = b,a
    
一行代码生成列表
当你需要通过频繁计算一些数值，然后 append 到一个空 list 的里面去的时候，比较方便的做法是直接这样：

    print([i for i in range(20) if i%2==0])
    
你也可以通过这种方式来读取文件：

    print([line.strip() for line in open('123.txt')])
    
可以使用 pprint 更好的输出：

    import pprint
    pprint.pprint([line.strip() for line in open(123.txt)])
    
分析性能
可以使用 cProfile 来分析你的 py 性能：

    python -m cProfile todo/todolist.py
    
if..in..else
有时候一些简单的判断可以直接用一行代码搞定，比如你要判断一个元素是否在列表中，根据是与否进行相应的操作就可以这样

    print('yes') if 88 in [1,56,44,67,88] else print('no')
    print('yes') if 66 in [1,56,44,67,88] else print('no')