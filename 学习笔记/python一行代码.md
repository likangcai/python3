Python ֻ��һ�д��룬����ʵ����Щ�¶���

�������������棬ֻ��һ�� Python �����������¿�����Щʲô����������֮ǰ�����һ�� Python ����ʵ�� http ����

    HTTP ������
    python3 -m http.server
    python3 -m http.server 6321

FTP ������
�ٸ�����ܸ��������ʹ�� pyftpdlib ��ֱ��ʵ��һ�� FTP �����������ļ����䣺

    python3 -m pyftpdlib
    ftp://127.0.0.1:2121
    ��ѡ����
    -i ָ��IP��ַ��Ĭ��Ϊ������IP��ַ��
    -p ָ���˿ڣ�Ĭ��Ϊ2121��
    -w дȨ�ޣ�Ĭ��Ϊֻ����
    -d ָ��Ŀ¼ ��Ĭ��Ϊ��ǰĿ¼��
    -u ָ���û�����¼
    -P ���õ�¼����
    
��ʽ�� Json
����ʹ�� json.tool ����ʽ�� Json��

    cat 12.json | python -m json.tool
    
python -c
ʹ����� -c ��������ֱ�����ն���ʹ�� Python �򵥵Ĵ��룺

    python -c "a=[i for i in range(6)]; print(a)"
    
һ�д���ʵ�ֺ���
ʹ�� lambda ������һ�д���ʵ��һ������������������Ҫ���б��е�Ԫ�ؽ��м������������ֱ��������

    print(list(map(lambda x:x*2,[1,2,3,4,5])
    
��������
һ�д��뽻����������������̸�ˣ�

    a = 1
    b = 2
    a,b = b,a
    
һ�д��������б�
������Ҫͨ��Ƶ������һЩ��ֵ��Ȼ�� append ��һ���� list ������ȥ��ʱ�򣬱ȽϷ����������ֱ��������

    print([i for i in range(20) if i%2==0])
    
��Ҳ����ͨ�����ַ�ʽ����ȡ�ļ���

    print([line.strip() for line in open('123.txt')])
    
����ʹ�� pprint ���õ������

    import pprint
    pprint.pprint([line.strip() for line in open(123.txt)])
    
��������
����ʹ�� cProfile ��������� py ���ܣ�

    python -m cProfile todo/todolist.py
    
if..in..else
��ʱ��һЩ�򵥵��жϿ���ֱ����һ�д���㶨��������Ҫ�ж�һ��Ԫ���Ƿ����б��У���������������Ӧ�Ĳ����Ϳ�������

    print('yes') if 88 in [1,56,44,67,88] else print('no')
    print('yes') if 66 in [1,56,44,67,88] else print('no')