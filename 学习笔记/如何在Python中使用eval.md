�����Python��ʹ��eval

Python�е� eval��ʲô��
��Python�У�������������÷�������Щ��������ʹPython��Ϊ�����˵ı������������Ҫ����eval������һ�֡�eval�������﷨���£�

    eval(expression, globals, locals)
   ������ʾ��eval������������������

    expression �C��Ҫһ���ַ��������ַ�����������������ΪPython���ʽ
    globals����ѡ���Cһ���ֵ䣬����ָ�����õ�ȫ�ַ����ͱ�����
    locals����ѡ��-��һ���ֵ䣬����ָ�����õı��ط����ͱ�����
�Ժ��ڱ�������ʾ��global(ȫ�ֱ���)s��locals(���ر���)��ʹ�á�

eval��Python����ʲô��
eval��������expression��������������Ϊpython���ʽ�����仰˵�����ǿ���˵������������˴��ݸ����ı��ʽ���ڳ���������python expression��code����
Ϊ�����������ַ����ı��ʽ��Python��eval�����������²��裺

    �������ʽ
    ������ֽ���
    ��������ΪPython���ʽ
    �����������

����ζ�ŵ����ǽ��κ�python���ʽ��Ϊ���ַ��������ݸ�eval����ʱ�����������ñ��ʽ�����������Ϊ�����򸡵�����������һЩ�򵥵�ʾ�������ǽ�ʹ�����������
������Python��ʹ��eval���ַ���ת��Ϊ�����������򸡵����ļ򵥷�����


    <code> num =�� 23�� 
    float_num =�� 53.332�� 
    complex_num =�� 2 + 3j�� 
    str1 =�� Not number�� 
    print��eval��num����type��eval��num������
    print��eval��float_num����type�� eval��float_num������
    print��eval��complex_num����type��eval��complex_num������
    print��eval��str1����type��eval��str1������</ code>
    
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
     
����������eval�����ܹ�ʶ���ַ����еı��ʽ������ת��Ϊ��Ӧ�����͡����ǣ������ǽ������ַ�����ĸʱ����������һ��������Ӧ�����eval��ʵ�����á�
�����и�������ӣ��������ǲ������漰����ת����ʵ�������ǿ�����eval���������ַ����еı��ʽ��
���ǻ�����ʹ��eval�����ѧ���ʽ��


    <code> expr =����2+��3 * 2����/ 2�� 
    print��eval��expr����</ code>
    
    OUTPUT:
    4.0

���������������ַ�����ʹ�ñ�������Python���������ǽ���������������ʾ

    <code>num=10
    expr="(2+(3*2))/2 + num"
    print(eval(expr))</code>
    
    OUTPUT:
    14.0   
    
���ǻ��������ַ����ڲ�ʹ�����ú�����������ʾ��

    <code>print(eval("sum([8, 16, 34])"))</code>
    
    OUTPUT:
    58    

Ϊ�˸��õ��˽�eval�����������ǿ�����������ʽ�������ַ��������������������Ӧ��������ʾ��

    <code>#string in another string
    expr="'2+3'"
    print(eval(expr))
    print(eval(eval(expr)))</code>
    
    OUTPUT:
    2+3                                                                                                                           
    5
��ˣ���һ��eval����ֻ�Ƿ����ַ����еı��ʽ����������һ��eval������ʹ��evalʱ�����ǵõ��˱��ʽ�Ĵ𰸡�

�����python��ʹ��eval ��

����һ���У������Ѿ��˽������ʹ��eval������������������ǽ��˽�eval�����������������Ӱ���乤������ˣ�Python�е�eval ����������������viz-globals��locals��
ȫ�ֱ����ǵ�ǰȫ�ַ�Χ�������ռ��п��õĶ��������ԴӴ����е��κ�λ�÷������ǡ�
��ִ��ʱ�����ݸ��ֵ���ȫ�ֱ��������ж��󽫶�eval�������á���鿴����ʾ������ʾ����ʾ�����ʹ���Զ���ʵ�Ϊeval�����ṩȫ�����ƿռ䣺


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

�����������ʾ���п����ģ�����evalֻ�ܷ���num1��num2�����ǵ��Ҵ�globals�ֵ���ɾ��num2ʱ�����׳���һ��������Ϊ�������޷�ʶ��num2��
���ǣ�Ϊʲô��������û�н�ֵ���ݸ�globals����������ʾ���ж�û�з������ִ���
��ʵ֤���������ڲ��ṩglobals����������µ���eval����ʱ���ú�����ʹ��globals�����������ص��ֵ���Ϊ��ȫ�������ռ����������ʽ��
��ˣ��������ʾ���У����ǿ������ɷ������б�������Ϊ�����ǵ�ǰȫ�ַ�Χ�а�����ȫ�ֱ�����
���ڣ���������ֵ䴫�ݸ�ȫ�ֱ����ᷢ��ʲô�������ǿ�����

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

��ˣ�eval�������Գɹ�ʶ�����ͣ����޷�ʶ����� a������˷��ش���
��������ȫ�ֱ����ṩ�Զ���ʵ�ʱ������������ __builtins__����ֵ���������������ֵ�����ڽ������ʽ֮ǰ�����Զ��ڡ� __builtins__���²���������ֵ�����á���������ȷ��eval�����������������ʽʱ����ȫ��������Python���������ơ���˵�����������ʾ���У����ͨ��evalʶ�����͡�
���������ǿ���ʲô�Ǿֲ������Լ����������չeval�����Ĺ��ܡ���ȫ�ֱ�����ͬ���ֲ������ں����ڲ������������ں����ⲿ���ʡ�
���Ƶأ�locals��������һ���ֵ䣬���ֵ������������һЩ���󣬶�eval������������Щ������Ϊ���ض����뿴��������ӣ�

    <code>print(eval("sum([a, 2, 2])",{}, {"a":2}))
    print(a)</code>
    
    OUTPUT:
     6                                                                                                                             
     Traceback (most recent call last):                                                                                            
       File "main.py", line 2, in                                                                                          
         print(a)                                                                                                                  
     NameError: name 'a' is not defined
     
��ע�⣬Ҫ�򱾵����ṩ�ֵ䣬��������Ҫ��ȫ�����ṩ�ֵ䡣���ܽ��ؼ��ֲ�����eval����һ��ʹ��
���ƺ��������󣬵����������ʾ���У���ͬʱʹ����globals��locals���������������������Ӱ������

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
 
���ڣ�����ϣ���ú�����eval�����������ã���˽�����ӵ������ֵ��С����ڣ�eval��������ʶ��abs������������ʶ���κ�����������

    <code>print(eval('abs(-1)',{"__builtins__":None},{"abs":abs}))</code>
    
    OUTPUT:
    1
    
ȫ�ֱ����;ֲ�����֮�����Ҫʵ�������ǣ��������Կ�в����ڣ�Python���Զ����� __builtins__��������ȫ�ֱ����������Ƿ�Ϊȫ�ֱ����ṩ�Զ���ʵ䣬���ᷢ�������������һ���棬����򱾵����ṩ�Զ���ʵ䣬����ִ��eval�����ڼ�ôʵ佫���ֲ��䡣

�����ľ�����
Python�е�eval���������ã���Ҳ����Ҫ�İ�ȫ������eval��������Ϊ�ǲ���ȫ�ģ���Ϊ���������������û���ִ̬������Python���롣�Ƕ�������ʲôӰ�죿
���������ڷ����������е�Ӧ�ó�����Ҫ���û����롣���ڣ��������������ʹ��eval���������û����Է��ʷ����������û���������������һЩ���ɵĴ��룺

    <code> __ import __��'subprocess'����getoutput��'rm �Crf *'��
    </ code>
����Ĵ��뽫ɾ��Ӧ�ó���ǰĿ¼�е������ļ�����϶���Ӱ�����ǡ�
��ˣ���ñ���ʹ��eval���������������ȻҪʹ��eval���������ǿ��Խ���globals��locals�����������书�ܡ�������������һ���п�������������������eval������ʹ��ֻ��ʹ��python��abs������
���磬��������һ��Ӧ�ó��򣬿����ڸ������ֻ����и������ֵ��ܺ����ҵ���Сֵ��������ʹ��eval����㷽��

    <code> print��eval��input��������
    #input��sum��[1,3,4]��
    #output��8 
    #input��min��[1,3,4]��
    #output��1 </ code>
    
���ǣ�����һ�ֲ��õı�̷�ʽ�������޷������û����������ݣ�������ǿ�������globals��locals������ʹ��eval����ʶ��sum������min��������ĺ�������϶��������Ĵ�����ͬ�������飬����Ҫ��ȫ�öࡣ




