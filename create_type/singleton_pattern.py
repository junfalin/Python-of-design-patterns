#单例模式
#最简单的方法 python中的模块module在程序中只被加载一次，本身就是单例的
"""
class singleton(object):
    pass
singleton = singleton()
#其他文件导入
"""

class Singleton(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_inst'):
            #cls._inst = super(Singleton, cls).__new__(cls,*args,**kwargs) #python2
            cls._inst = super(Singleton, cls).__new__(cls) #python3
        return cls._inst


if __name__ == "__main__":
    class A(Singleton):
        def __init__(self,*args,**kwargs):
            self.args=args
            self.kwargs=kwargs
    a = A('apple')
    b = A('banana')
    print(id(a),a.args,a.kwargs)
    print(id(b),b.args,a.kwargs)