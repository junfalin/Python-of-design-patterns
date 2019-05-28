# 责任链模式
"""
有多个对象，每个对象持有对下一个对象的引用，
这样就会形成一条链，请求在这条链上传递，
直到某一对象决定处理该请求。
但是发出者并不清楚到底最终那个对象会处理该请求
"""
# 链接上的请求可以是一条链，可以是一个树，还可以是一个环，模式本身不约束这个，需要我们自己去实现，同时，在一个时刻，命令只允许由一个对象传给另一个对象，而不允许传给多个对象。
#


class Opertor(object):
    def opertor(self): pass


class Handle(object):
    handle = None

    def get_handel(self):
        return self.handle

    def set_handle(self, handle):
        self.handle = handle


class Myhandle(Handle, Opertor):
    def __init__(self, name):
        self.name = name

    def opertor(self):
        print(f"{self.name}")
        if self.get_handel() is not None:
            self.get_handel().opertor()


if __name__ == "__main__":
    h1 = Myhandle('h1')
    h2 = Myhandle('h2')
    h3 = Myhandle('h3')

    h1.set_handle(h2)
    h2.set_handle(h3)

    h1.opertor()
