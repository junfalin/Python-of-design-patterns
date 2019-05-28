# 代理模式
class Source(object):
    def method(self): pass


class MySource(Source):
    def method(self):
        print('this my_source method')


class Proxy(Source):
    def __init__(self):
        super(Proxy, self).__init__()
        self.source = MySource()

    def method(self):
        self.before()
        self.source.method()
        self.after()

    def before(self):
        print("before proxy")

    def after(self):
        print("after proxy")


if __name__ == '__main__':
    proxy = Proxy()
    proxy.method()
