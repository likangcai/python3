Python多进程及多线程基础

    关于进程和线程的基础知识，之前已经分享过一些文章，下面把一些基础知识，再总结下（重点：面试常问）：
    启动一个程序，就默认创建一个主进程，在一个主进程中默认创建一个主线程
    进程是系统资源分配和调度的基本单位，线程存在于进程中，线程是CPU调度和分配的基本单位。
    进程之间相互独立，同一个变量，多进程中各自会拷贝一份，而同一个进程的多个线程是共享内存的，所有变量都由所有线程共享，从而提升程序的运行效率。
    进程之间相互独立，一个进程的崩溃不会影响其他进程，而线程包含在进程之中，如果线程崩溃，则会导致其他线程崩溃，当然也会导致该进程崩溃。所以多进程开发模式要比多线程模式健壮性要强。
    
进程的运行状态

    1）新建状态：该进程正在被创建，尚未转到就绪状态。
    2）就绪状态：所有运行条件都已满足，正在等待CPU。
    3）运行状态（执行窗台）：进程正在处理器上运行。
    4）阻塞状态：进程正在等待某一事件而暂停运行。如等待可用资源或等待输入输出完成。即使处理器空闲，该进程也不能运行。
    5）死亡状态：进程正在从系统中消失。
    
    进程的三个基本状态是可以相互转换的
    就绪——>运行：当进程获得处理器时，由就绪状态转为运行状态。
    运行——>就绪：当进程被剥夺处理器时，如用完系统分配给他的时间片，出现更高级别的其它进程，进程由运行状态转为就绪状态。
    运行——>阻塞：当运行进程因某事件受阻，如所申请资源被占用，启动I/O传输未完成，进程由运行状态转为阻塞状态。
    阻塞——>就绪:当所等待事件发生，如得到申请资源，I/O传输完成，进程由阻塞变为就绪状态    
        
Python中如何使用多进程
Python中使用multiprocessing模块创建进程
multiprocessing模块提供了一个Process类创建进程对象。

    Process([group] ,[target], [ name ],[args], [ kwargs])
    group：指定进程组，大多数情况下用不到,一般情况下group只能赋值为None
    target：如果传递了函数的引用，可以任务这个子进程就执行这里的代码，target=函数名，函数名不能带括号
    args：给target指定的函数传递的参数，以元组的方式传递。args=(5,)，只有一个参数的话，要加个逗号才能表示元组
    kwargs：给target指定的函数传递命名参数，一般是以字典的形式传递，kwargs={"形参1"：“实参1”，“形参2”：“实参2”}
    name：给进程设定一个名字，可以不设定

Process创建的实例对象的常用方法

    start()：启动子进程实例（创建子进程）
    is_alive()：判断进程子进程是否还在活着
    join([timeout])：是否等待子进程执行结束，或等待多少秒
    terminate()：不管任务是否完成，立即终止子进程。
    name:当前进程实例别名，默认Process-N，N从1开始递增。
    pid:当前进程实例的PID值。

使用Process类来创建一个多进程

    #导入多进程模块
    import  multiprocessing
    import os
    def target_func():
        print("子进程名字",multiprocessing.current_process().name)
        print("子进程PID：",os.getpid())
        print("子进程的父进程ppid:",os.getppid())
    
    if __name__ == '__main__':
     
        for i in range(3):
            # 创建进程实例，指定要执行的目标函数
            p = multiprocessing.Process(target=target_func)
            p.start()#使用start方法启动进程
            p.join()#等待子进程结束
            print("主进程pid：",os.getpid())
     输出：
    子进程名字 Process-1
    子进程PID：3708
    子进程的父进程ppid: 4256
    主进程pid：4256
    子进程名字 Process-2
    子进程PID：8460
    子进程的父进程ppid: 4256
    主进程pid：4256
    子进程名字 Process-3
    子进程PID：4468
    子进程的父进程ppid: 4256
    主进程pid：4256

Python中如何使用多线程
在python中，使用threading模块来进行程序的多线程操作。threading模块提供了一个Thread类创建线程。

    1.target是线程执行函数的名字，函数的名字后面不要带有小括号。
    2.args：执行函数所需要的参数，这个参数要以元组的形式去传，如果只有一个元素，后面不要忘了逗号。
    3.kwargs：执行函数所需要的参数， 这个参数要以字典方式去传
    Thread类提供了以下方法:
    run(): 用以表示线程活动的方法。
    start():启动线程活动。
    join([time]): 等待至线程中止，直至启动的线程终止之前一直挂起；除非给出了timeout（秒），否则会一直阻塞。
    isAlive(): 返回线程是否活动的。
    getName(): 返回线程名。
    setName(): 设置线程名。
    threading常用方法及属性：
    threading.currentThread(): 返回当前的线程变量。
    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    threading.activeCount(): 返回当前活跃的线程数，1个主线程+n个子线程。
    
多线程简单使用

    import threading #导入多线程模块
    
    def eat():
        print('正在吃饭')
        print('线程名称 %s'%threading.current_thread().name)
    def dance():
        print('正在跳舞')
        print('线程名称 %s'%threading.current_thread().name)
    def song():
        print('正在唱歌')
        print('线程名称 %s'%threading.current_thread().name)
    
    if __name__ == '__main__':
    
        thread = [] #定义空列表用来保存线程
        t1 = threading.Thread(target=eat,args=('')) #定义第一条线程
        t2 = threading.Thread(target=dance,args=('')) #定义第二条线程
        t3 = threading.Thread(target=song,args=('')) #定义第三条线程
        thread.append(t1) #将线程依次加入到列表中
        thread.append(t2)
        thread.append(t3)
        for i in thread:
            i.start() #依次启动所有线程
        for i in thread:
            i.join()  #守护所有线程
    
    输出：
    正在吃饭
    线程名称 Thread-1
    正在跳舞
    线程名称 Thread-2
    正在唱歌
    线程名称 Thread-3 
