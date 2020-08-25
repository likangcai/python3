学习如何使用不同的Python模块从web下载文件。此外，你将下载常规文件、web页面、Amazon S3和其他资源。
最后，你将学习如何克服可能遇到的各种挑战，例如下载重定向的文件、下载大型文件、完成一个多线程下载以及其他策略。

使用Requests
你可以使用requests模块从一个URL下载文件。
考虑以下代码:

    import requestes
    url = 'https://www.python.org/static/img/python-logo@2x.png'
    myfile = requests.get(url)
    open('c:/users/123.png','wb').write(myfile.content)
你只需使用requests模块的get方法获取URL，并将结果存储到一个名为“myfile”的变量中。然后，将这个变量的内容写入文件。

使用wget
你还可以使用Python的wget模块从一个URL下载文件。你可以使用pip按以下命令安装wget模块:

    pip3 install wget
    考虑以下代码，我们将使用它下载Python的logo图像。
    import wget
    url = 'https://www.python.org/static/img/python-logo@2x.png'
    wget.download(url,'c:/users/123.png')
    在这段代码中，URL和路径(图像将存储在其中)被传递给wget模块的download方法。
    
下载重定向的文件

在本节中，你将学习如何使用requests从一个URL下载文件，该URL会被重定向到另一个带有一个.pdf文件的URL。该URL看起来如下:
https://readthedocs.org/projects/python-guide/downloads/pdf/latest/
要下载这个pdf文件，请使用以下代码

    import requests
    url = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
    myfile = requests.get(url,allow_redirects=True)
    open('c://users/12.pdf','wb').write(myfile.content)
在这段代码中，我们第一步指定的是URL。然后，我们使用request模块的get方法来获取该URL。
在get方法中，我们将allow_redirects设置为True，这将允许URL中的重定向，并且重定向后的内容将被分配给变量myfile。
最后，我们打开一个文件来写入获取的内容。
    
分块下载大文件
考虑下面的代码:

    import requests
    url = 'https://www.python.org/static/img/python-logo@2x.png'
    myfile = requests.get(url)
    open('c://users/12.png','wb').write(myfile.content)

首先，我们像以前一样使用requests模块的get方法，但是这一次，我们将把stream属性设置为True。
接着，我们在当前工作目录中创建一个名为PythonBook.pdf的文件，并打开它进行写入。
然后，我们指定每次要下载的块大小。我们已经将其设置为1024字节，接着遍历每个块，并在文件中写入这些块，直到块结束。
不漂亮吗?不要担心，稍后我们将显示一个下载过程的进度条。
下载多个文件(并行/批量下载)
要同时下载多个文件，请导入以下模块:

    import os
    import requests
    from time import time
    from multiprocessing.pool import ThreadPool
我们导入了os和time模块来检查下载文件需要多少时间。ThreadPool模块允许你使用池运行多个线程或进程。
让我们创建一个简单的函数，将响应分块发送到一个文件:

    def url_response(url):
        path,url = url
        r = requests.get(url,stream = True)
        with open(path,'wb') as f:
            for ch in r:
                f.write(ch)
这个URL是一个二维数组，它指定了你要下载的页面的路径和URL。

就像在前一节中所做的那样，我们将这个URL传递给requests.get。最后，我们打开文件(URL中指定的路径)并写入页面内容。
现在，我们可以分别为每个URL调用这个函数，我们也可以同时为所有URL调用这个函数。让我们在for循环中分别为每个URL调用这个函数，注意计时器:

    start = time()
    for x in urls:
        url_response(x)
    print(f"time to download:{time()-start}")
   
现在，使用以下代码行替换for循环
    
    ThreadPool(9).imap_unordered(url_response,urls)

使用进度条进行下载
进度条是clint模块的一个UI组件。输入以下命令来安装clint模块：
pip3 install clint

使用urllib下载网页
在本节中，我们将使用urllib下载一个网页。
urllib库是Python的标准库，因此你不需要安装它。

通过代理下载
如果你需要使用代理下载你的文件，你可以使用urllib模块的ProxyHandler。

使用urllib3
urllib3是urllib模块的改进版本。你可以使用pip下载并安装它:
pip3 install urllib3

使用Boto3从S3下载文件
要从Amazon S3下载文件，你可以使用Python boto3模块。
在开始之前，你需要使用pip安装awscli模块:
pip3 install awscli

要从Amazon S3下载文件，你需要导入boto3和botocore。Boto3是一个Amazon SDK，它允许Python访问Amazon web服务(如S3)。Botocore提供了与Amazon web服务进行交互的命令行服务。
Botocore自带了awscli。要安装boto3，请运行以下命令
在从Amazon下载文件时，我们需要三个参数：
 Bucket名称
你需要下载的文件名称
文件下载之后的名称
    
使用asyncio


asyncio模块主要用于处理系统事件。它围绕一个事件循环进行工作，该事件循环会等待事件发生，然后对该事件作出反应。这个反应可以是调用另一个函数。这个过程称为事件处理。asyncio模块使用协同程序进行事件处理。
要使用asyncio事件处理和协同功能，我们将导入asyncio模块:    
        


