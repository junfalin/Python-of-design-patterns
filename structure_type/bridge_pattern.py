# 桥梁模式

class Source(object):
    def method(self):pass


class Sub1(Source):
    def method(self):
        print('i am sub1 method!')


class Sub2(Source):
    def method(self):
        print('i am sub2 method!')



class Bridge(object):
    source = None

    def get_source(self):
        return self.source

    def set_source(self,s):
        self.source = s

    def method(self):
        self.source.method()


if __name__ == '__main__':
    bridge = Bridge()
    sub1 = Sub1()
    bridge.set_source(sub1)
    bridge.method()

    sub2 = Sub2()
    bridge.set_source(sub2)
    bridge.method()