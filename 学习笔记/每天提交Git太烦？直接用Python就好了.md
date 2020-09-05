每天提交Git太烦？直接用Python就好了

对于协作开发的项目，每天开发前后更新和提交 Git 仓库是基本操作。但作为总是想偷懒的程序员，一定会想这种重复操作有没有可能自动化？如果在控制台用 Shell 做复杂的逻辑运算与流程控制是一个灾难。所以，用 Python 来实现是一个愉快的选择。这时，就需要在 Python 中操作 Git 的库。

0. GitPython 简介
GitPython是一个与Git库交互的Python库，包括底层命令（Plumbing）与高层命令（Porcelain）。它可以实现绝大部分的Git读写操作，避免了频繁与Shell交互的畸形代码。它并非是一个纯粹的Python实现，而是有一部分依赖于直接执行git命令，另一部分依赖于GitDB。
GitDB也是一个Python库。它为.git/objects建立了一个数据库模型，可以实现直接的读写。由于采用流式（stream）读写，所以运行高效、内存占用低。

1. GitPython安装
    pip install GitPython
其依赖GitDB会自动安装，不过可执行的git命令需要额外安装。

2. 基本用法

        init
        import git
        repo = git.Repo.init(path='.')
    
这样就在当前目录创建了一个Git库。当然，路径可以自定义。
由于git.Repo实现了__enter__与__exit__，所以可以与with联合使用。

    with git.Repo.init(path='.') as repo:
        # do sth with repo
不过，由于只是实现了一些清理操作，关闭后仍然可以读写，所以使用这种形式的必要性不高。详见附录。

clone
clone分两种。一是从当前库clone到另一个位置：

    new_repo = repo.clone(path='../new')
二是从某个URL那里clone到本地某个位置：

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
GitPython并未实现原版git status，而是给出了部分的信息。

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
    
checkout（清理所有修改）

    >>> repo.is_dirty()
    True
    >>> repo.index.checkout(force=True)
    <generator object <genexpr> at 0x7f2bf35e6b40>
    >>> repo.is_dirty()
    False
    branch
获取当前分支：

    head = repo.head
新建分支：

    new_head = repo.create_head('new_head', 'HEAD^')
切换分支：

    new_head.checkout()
    head.checkout()
删除分支：

    git.Head.delete(repo, new_head)
    # or
    git.Head.delete(repo, 'new_head')
    
merge
以下演示如何在一个分支（other），merge另一个分支（master）。

    master = repo.heads.master
    other = repo.create_head('other', 'HEAD^')
    other.checkout()
    repo.index.merge_tree(master)
    repo.index.commit('Merge from master to other')
remote, fetch, pull, push
创建remote：

    remote = repo.create_remote(name='gitlab', url='git@gitlab.com:USER/REPO.git')
    
远程交互操作：

    remote = repo.remote()
    remote.fetch()
    remote.pull()
    remote.push()
删除remote：

    repo.delete_remote(remote)
    # or
    repo.delete_remote('gitlab')    
    
其它
其它还有Tag、Submodule等相关操作，不是很常用，这里就不介绍了。
GitPython的优点是在做读操作时可以方便地获取内部信息，缺点是在做写操作时感觉很不顺手，隔靴搔痒。当然，它还支持直接执行git操作。

    git = repo.git
    git.status()
    git.checkout('HEAD', b="my_new_branch")
    git.branch('another-new-one')
    git.branch('-D', 'another-new-one')
    
3. 其它操作Git的方法
subprocess
这就是所谓『老路』。在另一个进程，执行Shell命令，并通过stdio来解析返回结果。


    import subprocess
    subprocess.call(['git', 'status'])
    dulwich
dulwich是一个纯Python实现的Git交互库，以后有空再研究吧。
官方网站：https://www.dulwich.io/

pygit2
pygit2是基于libgit2实现的一个Python库。底层是C，而上层Python只是接口，运行效率应该是最高的，然而孤还是放弃了。其缺点是，需要环境中预先安装libgit2。相比之下，GitPython只需要环境预置Git，简单多了。
官方网站：http://www.pygit2.org/

参考
《GitPython Documentation》
《Welcome to GitDB’s documentation!》
《Git - 底层命令 (Plumbing) 和高层命令 (Porcelain)》
《GitPython | Hom》
    
5. 附录
在git.Repo中对context相关接口的实现如下：


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
    
可见只是一些清理操作，关闭的必要性不高。即使关闭，也仍然可以对这个git.Repo的instance进行读写操作。