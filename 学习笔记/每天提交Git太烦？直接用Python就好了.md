ÿ���ύGit̫����ֱ����Python�ͺ���

����Э����������Ŀ��ÿ�쿪��ǰ����º��ύ Git �ֿ��ǻ�������������Ϊ������͵���ĳ���Ա��һ�����������ظ�������û�п����Զ���������ڿ���̨�� Shell �����ӵ��߼����������̿�����һ�����ѡ����ԣ��� Python ��ʵ����һ������ѡ����ʱ������Ҫ�� Python �в��� Git �Ŀ⡣

0. GitPython ���
GitPython��һ����Git�⽻����Python�⣬�����ײ����Plumbing����߲����Porcelain����������ʵ�־��󲿷ֵ�Git��д������������Ƶ����Shell�����Ļ��δ��롣��������һ�������Pythonʵ�֣�������һ����������ֱ��ִ��git�����һ����������GitDB��
GitDBҲ��һ��Python�⡣��Ϊ.git/objects������һ�����ݿ�ģ�ͣ�����ʵ��ֱ�ӵĶ�д�����ڲ�����ʽ��stream����д���������и�Ч���ڴ�ռ�õ͡�

1. GitPython��װ
    pip install GitPython
������GitDB���Զ���װ��������ִ�е�git������Ҫ���ⰲװ��

2. �����÷�

        init
        import git
        repo = git.Repo.init(path='.')
    
�������ڵ�ǰĿ¼������һ��Git�⡣��Ȼ��·�������Զ��塣
����git.Repoʵ����__enter__��__exit__�����Կ�����with����ʹ�á�

    with git.Repo.init(path='.') as repo:
        # do sth with repo
����������ֻ��ʵ����һЩ����������رպ���Ȼ���Զ�д������ʹ��������ʽ�ı�Ҫ�Բ��ߡ������¼��

clone
clone�����֡�һ�Ǵӵ�ǰ��clone����һ��λ�ã�

    new_repo = repo.clone(path='../new')
���Ǵ�ĳ��URL����clone������ĳ��λ�ã�

    new_repo = git.Repo.clone_from(url='git@github.com:USER/REPO.git', to_path='../new')
    
commit

    with open('test.file', 'w') as fobj:
        fobj.write('1st line\n')
    repo.index.add(items=['test.file'])
    repo.index.commit('write a line into test.file')
    
    with open('test.file', 'aw') as fobj:
        fobj.write('2nd line\n')
    repo.index.add(items=['test.file'])
    repo.index.commit('write another line into test.file')    
    
status
GitPython��δʵ��ԭ��git status�����Ǹ����˲��ֵ���Ϣ��

    >>> repo.is_dirty()
    False
    >>> with open('test.file', 'aw') as fobj:
    >>>     fobj.write('dirty line\n')
    >>> repo.is_dirty()
    True
    >>> repo.untracked_files
    []
    >>> with open('untracked.file', 'w') as fobj:
    >>>     fobj.write('')
    >>> repo.untracked_files
    ['untracked.file']
    
checkout�����������޸ģ�

    >>> repo.is_dirty()
    True
    >>> repo.index.checkout(force=True)
    <generator object <genexpr> at 0x7f2bf35e6b40>
    >>> repo.is_dirty()
    False
    branch
��ȡ��ǰ��֧��

    head = repo.head
�½���֧��

    new_head = repo.create_head('new_head', 'HEAD^')
�л���֧��

    new_head.checkout()
    head.checkout()
ɾ����֧��

    git.Head.delete(repo, new_head)
    # or
    git.Head.delete(repo, 'new_head')
    
merge
������ʾ�����һ����֧��other����merge��һ����֧��master����

    master = repo.heads.master
    other = repo.create_head('other', 'HEAD^')
    other.checkout()
    repo.index.merge_tree(master)
    repo.index.commit('Merge from master to other')
remote, fetch, pull, push
����remote��

    remote = repo.create_remote(name='gitlab', url='git@gitlab.com:USER/REPO.git')
    
Զ�̽���������

    remote = repo.remote()
    remote.fetch()
    remote.pull()
    remote.push()
ɾ��remote��

    repo.delete_remote(remote)
    # or
    repo.delete_remote('gitlab')    
    
����
��������Tag��Submodule����ز��������Ǻܳ��ã�����Ͳ������ˡ�
GitPython���ŵ�������������ʱ���Է���ػ�ȡ�ڲ���Ϣ��ȱ��������д����ʱ�о��ܲ�˳�֣���ѥɦ������Ȼ������֧��ֱ��ִ��git������

    git = repo.git
    git.status()
    git.checkout('HEAD', b="my_new_branch")
    git.branch('another-new-one')
    git.branch('-D', 'another-new-one')
    
3. ��������Git�ķ���
subprocess
�������ν����·��������һ�����̣�ִ��Shell�����ͨ��stdio���������ؽ����


    import subprocess
    subprocess.call(['git', 'status'])
    dulwich
dulwich��һ����Pythonʵ�ֵ�Git�����⣬�Ժ��п����о��ɡ�
�ٷ���վ��https://www.dulwich.io/

pygit2
pygit2�ǻ���libgit2ʵ�ֵ�һ��Python�⡣�ײ���C�����ϲ�Pythonֻ�ǽӿڣ�����Ч��Ӧ������ߵģ�Ȼ���»��Ƿ����ˡ���ȱ���ǣ���Ҫ������Ԥ�Ȱ�װlibgit2�����֮�£�GitPythonֻ��Ҫ����Ԥ��Git���򵥶��ˡ�
�ٷ���վ��http://www.pygit2.org/

�ο�
��GitPython Documentation��
��Welcome to GitDB��s documentation!��
��Git - �ײ����� (Plumbing) �͸߲����� (Porcelain)��
��GitPython | Hom��
    
5. ��¼
��git.Repo�ж�context��ؽӿڵ�ʵ�����£�


    def __enter__(self):
            return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    
    def __del__(self):
        try:
            self.close()
        except:
            pass
    
    def close(self):
        if self.git:
            self.git.clear_cache()
            gc.collect()
            gitdb.util.mman.collect()
            gc.collect()
    
�ɼ�ֻ��һЩ����������رյı�Ҫ�Բ��ߡ���ʹ�رգ�Ҳ��Ȼ���Զ����git.Repo��instance���ж�д������