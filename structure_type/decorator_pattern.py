# 装饰器模式


class Source(object):
    def do_something(self): pass


class MySource(Source):
    def do_something(self):
        print('i am original method')


class Decorator(Source):
    def __init__(self, obj):
        self.obj = obj

    def do_something(self):
        print("before decorator!")
        self.obj.do_something()
        print("after decorator!")


if __name__ == "__main__":
    my_source = MySource()
    obj = Decorator(my_source)
    obj.do_something()