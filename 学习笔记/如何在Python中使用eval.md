如何在Python中使用eval

Python中的 eval是什么？
在Python中，我们有许多内置方法，这些方法对于使Python成为所有人的便捷语言至关重要，而eval是其中一种。eval函数的语法如下：

    eval(expression, globals, locals)
   如上所示，eval函数采用三个参数：

    expression –需要一个字符串，该字符串将被解析并评估为Python表达式
    globals（可选）–一个字典，用于指定可用的全局方法和变量。
    locals（可选）-另一个字典，用于指定可用的本地方法和变量。
稍后将在本文中显示对global(全局变量)s和locals(本地变量)的使用。

eval在Python中做什么？
eval函数解析expression参数并将其评估为python表达式。换句话说，我们可以说这个函数解析了传递给它的表达式并在程序中运行python expression（code）。
为了评估基于字符串的表达式，Python的eval函数运行以下步骤：

    解析表达式
    编译成字节码
    将其评估为Python表达式
    返回评估结果

这意味着当我们将任何python表达式作为“字符串”传递给eval函数时，它会评估该表达式并将结果返回为整数或浮点数。以下是一些简单的示例，它们将使您更加清楚。
这是在Python中使用eval将字符串转换为整数，复数或浮点数的简单方法：


    <code> num =“ 23” 
    float_num =“ 53.332” 
    complex_num =“ 2 + 3j” 
    str1 =“ Not number” 
    print（eval（num），type（eval（num）））
    print（eval（float_num），type（ eval（float_num）））
    print（eval（complex_num），type（eval（complex_num）））
    print（eval（str1），type（eval（str1）））</ code>
    
    OUTPUT:
     23                                                                                                               
     53.332                                                                                                         
     (2+3j)                                                                                                       
     Traceback (most recent call last):                                                                                            
       File "main.py", line 8, in                                                                                          
         print(eval(str1),type(eval(str1)))                                                                                        
       File "", line 1                                                                                                     
         Not number                                                                                                                
                  ^                                                                                                                
     SyntaxError: unexpected EOF while parsing
     
如您所见，eval函数能够识别字符串中的表达式并将其转换为相应的类型。但是，当我们仅传递字符和字母时，它返回了一个错误。这应该清楚eval的实际作用。
这里有更多的例子，其中我们不仅仅涉及类型转换，实际上我们看到了eval函数评估字符串中的表达式。
我们还可以使用eval求解数学表达式：


    <code> expr =“（2+（3 * 2））/ 2” 
    print（eval（expr））</ code>
    
    OUTPUT:
    4.0

我们甚至可以在字符串中使用变量名，Python还将对它们进行评估，如下所示

    <code>num=10
    expr="(2+(3*2))/2 + num"
    print(eval(expr))</code>
    
    OUTPUT:
    14.0   
    
我们还可以在字符串内部使用内置函数，如下所示：

    <code>print(eval("sum([8, 16, 34])"))</code>
    
    OUTPUT:
    58    

为了更好地了解eval函数，让我们看看如果将表达式用两个字符串括起来，它将如何响应，如下所示：

    <code>#string in another string
    expr="'2+3'"
    print(eval(expr))
    print(eval(eval(expr)))</code>
    
    OUTPUT:
    2+3                                                                                                                           
    5
因此，第一个eval函数只是返回字符串中的表达式，但是在另一个eval函数中使用eval时，我们得到了表达式的答案。

如何在python中使用eval ？

在上一节中，我们已经了解了如何使用eval函数，但是在这里，我们将了解eval函数的其他参数如何影响其工作。因此，Python中的eval 还有两个参数，即viz-globals和locals。
全局变量是当前全局范围或命名空间中可用的对象。您可以从代码中的任何位置访问它们。
在执行时，传递给字典中全局变量的所有对象将对eval（）可用。请查看以下示例，该示例显示了如何使用自定义词典为eval函数提供全局名称空间：


    <code>num1 = 100  # A global variable
    print(eval("num1 + 100", {"num1": num1}))
    num2 = 200  # Another global variable
    print(eval("num1 + num2", {"num1": num1,"num2": num2}))
    print(eval("num1 + num2", {"num1": num1}))</code>
    
    OUTPUT:
     200                                                                                                                           
     300                                                                                                                           
     Traceback (most recent call last):                                                                                            
       File "main.py", line 5, in                                                                                          
         print(eval("num1 + num2", {"num1": num1}))                                                                                
       File "", line 1, in                                                                                         
     NameError: name 'num2' is not defined

如您在上面的示例中看到的，首先eval只能访问num1和num2，但是当我从globals字典中删除num2时，它抛出了一个错误，因为它现在无法识别num2。
但是，为什么在我甚至没有将值传递给globals参数的上述示例中都没有发生这种错误？
事实证明，当您在不提供globals参数的情况下调用eval函数时，该函数将使用globals（）函数返回的字典作为其全局命名空间来评估表达式。
因此，在上面的示例中，我们可以自由访问所有变量，因为它们是当前全局范围中包含的全局变量。
现在，如果将空字典传递给全局变量会发生什么，让我们看看：

    <code>a=2
    print(eval("sum([2, 2, 2])", {}))
    print(eval("sum([a, 2, 2])", {}))</code>
    
    OUTPUT:
    6                                                                                                                             
     Traceback (most recent call last):                                                                                            
       File "main.py", line 3, in                                                                                          
         print(eval("sum([a, 2, 2])", {}))                                                                                         
       File "", line 1, in                                                                                         
     NameError: name 'a' is not defined

因此，eval函数可以成功识别函数和，但无法识别对象“ a”，因此返回错误。
当我们向全局变量提供自定义词典时，它包含键“ __builtins__”的值，但如果不包含该值，则在解析表达式之前，将自动在“ __builtins__”下插入对内置字典的引用。这样可以确保eval（）函数在评估表达式时将完全访问所有Python的内置名称。这说明了在上面的示例中，如何通过eval识别函数和。
现在让我们看看什么是局部变量以及它们如何扩展eval函数的功能。与全局变量不同，局部对象在函数内部声明，不能在函数外部访问。
类似地，locals参数采用一个字典，在字典中我们添加了一些对象，而eval（）函数将这些对象视为本地对象。请看下面的例子：

    <code>print(eval("sum([a, 2, 2])",{}, {"a":2}))
    print(a)</code>
    
    OUTPUT:
     6                                                                                                                             
     Traceback (most recent call last):                                                                                            
       File "main.py", line 2, in                                                                                          
         print(a)                                                                                                                  
     NameError: name 'a' is not defined
     
请注意，要向本地人提供字典，您首先需要向全局人提供字典。不能将关键字参数与eval（）一起使用
这似乎令人困惑，但是在下面的示例中，我同时使用了globals和locals参数，您将看到它们如何影响结果。

    <code>print(eval("abs(-1)"))
    #By keeping __builtins__":None,eval will recognise no in-buiilt function
    print(eval('abs(-1)',{"__builtins__":None}))</code>
    
    OUTPUT:
    1
    Traceback (most recent call last):                                                                                            
       File "main.py", line 1, in                                                                                          
         print(eval('abs(-1)',{"__builtins__":None}))                                                                              
       File "", line 1, in                                                                                         
     TypeError: 'NoneType' object is not subscriptable
 
现在，我们希望该函数在eval函数中起作用，因此将其添加到本地字典中。现在，eval函数可以识别abs函数，而不能识别任何其他函数。

    <code>print(eval('abs(-1)',{"__builtins__":None},{"abs":abs}))</code>
    
    OUTPUT:
    1
    
全局变量和局部变量之间的主要实际区别是，如果该密钥尚不存在，Python会自动将“ __builtins__”键插入全局变量。无论是否为全局变量提供自定义词典，都会发生这种情况。另一方面，如果向本地人提供自定义词典，则在执行eval函数期间该词典将保持不变。

评估的局限性
Python中的eval（）很有用，但也有重要的安全隐患。eval函数被认为是不安全的，因为它允许您或其他用户动态执行任意Python代码。那对我们有什么影响？
假设您正在服务器上运行的应用程序中要求用户输入。现在，如果您在输入上使用eval函数，则用户可以访问服务器本身。用户可以像这样传递一些可疑的代码：

    <code> __ import __（'subprocess'）。getoutput（'rm –rf *'）
    </ code>
上面的代码将删除应用程序当前目录中的所有文件，这肯定会影响我们。
因此，最好避免使用eval函数，但是如果仍然要使用eval函数，我们可以借助globals和locals参数来限制其功能。正如我们在上一节中看到的那样，我们限制eval函数，使其只能使用python的abs函数。
例如，假设我有一个应用程序，可以在给定数字或所有给定数字的总和中找到最小值。像这样使用eval的最方便方法

    <code> print（eval（input（）））
    #input：sum（[1,3,4]）
    #output：8 
    #input：min（[1,3,4]）
    #output：1 </ code>
    
但是，这是一种不好的编程方式。我们无法控制用户的输入内容，因此我们可以利用globals和locals参数，使得eval不能识别sum（）和min（）以外的函数。这肯定会和上面的代码做同样的事情，但是要安全得多。




