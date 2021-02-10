[toc]

---
#### 责任链模式
```
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
```
---
#### 命令模式
```
#顾名思义

class Order(object):
    def __init__(self, receiver):
        self.receiver = receiver

    def exc(self): 
        self.receiver.action()

class Receiver(object):
    def action(self):
        print('yeah sir!')


class Commander(object):
    def __init__(self,order):
        self.order = order

    def issue(self):
        self.order.exc()


if __name__ == "__main__":
    receiver = Receiver()
    order = Order(receiver)
    commander = Commander(order)
    commander.issue()
```
---
####解释器模式
```
class Expression(object):
    def interpret(self):pass


class Plus(Expression):
    def interpret(self,context):
        return context.get_num1() + context.get_num2()

class Context:
    def __init__(self,x,y):
        self.num1 = x
        self.num2 = y
    
    def get_num1(self):
        return self.num1
    
    def get_num2(self):
        return self.num2
    

if __name__ == "__main__":
    context = Context(10,23)
    exp = Plus()
    result = exp.interpret(context)
    print(f"result:{result} ")
```
---
#### 迭代器模式
```


class Interator(object):
    def __init__(self, coll):
        self.collection = coll
        self.pos = -1

    def previous(self):
        if self.pos > 0:
            self.pos -= 1
        return self.collection.get(self.pos)

    def next(self):
        if self.pos < self.collection.size()-1:
            self.pos += 1
        return self.collection.get(self.pos)

    def hasnext(self):
        if self.pos < self.collection.size()-1:
            return True
        return False

    def hasprevious(self):
        if self.pos > 0:
            return True
        return False

class Collection(object):
    def __init__(self):
        self.collection = [1,2,3,4,5,6,7,8,9,10]

    def new_iterator(self):
        return Interator(self)

    def get(self, index):
        return self.collection[index]

    def size(self):
        return len(self.collection)


if __name__ == "__main__":
    coll = Collection()
    it = coll.new_iterator()
    while(it.hasnext()):
        print(f"{it.next()}")
    while(it.hasprevious()):
        print(f"{it.previous()}")
```
---
####中介者模式
```
#顾名思义


class Customer:
    def __init__(self,mediator):
        self.mediator = mediator
    
    def get_mediator(self):
        return self.mediator

    def do_some(self):pass


class User1(Customer):
    def do_some(self):
        print("user1 do something")

class User2(Customer):
    def do_some(self):
        print("user2 do something")

class Mediator:
    def create_mediator(self):
        self.user1 = User1(self)
        self.user2 = User2(self)
    
    def all_do(self):
        self.user1.do_some()
        self.user2.do_some()

    def get_user1(self):
        return self.user1
    
    def get_user2(self):
        return self.user2



if __name__ == "__main__":
    mediator = Mediator()
    mediator.create_mediator()
    mediator.all_do()

```
---
#### 备忘录模式
```
import time
import copy
class Original:
    def __init__(self):
        self.create_time = int(time.time())

    def create_memento(self):
        return Memento(copy.deepcopy(self))

        


class Memento:
    def __init__(self,origin:Original):
        self.origin = origin

    def get_back(self):
        return self.origin
    


if __name__ == "__main__":
    ori = Original()
    print(f"#origin>id {id(ori)};{ori.__dict__}")
    mem = ori.create_memento()

    time.sleep(2)
    ori.create_time = int(time.time())
    print(f"#change origin>id {id(ori)};{ori.__dict__}")
    print(f"#back>id {id(mem.get_back())};{mem.get_back().__dict__}")

```
---
####观察者模式
```
class Observer(object):
    def action(self):pass


class Obs1(Observer):
    def action(self):
        print('obs1 copy that!')

class Obs2(Observer):
    def action(self):
        print('obs2 copy that!')


class Publisher:
    def __init__(self):
        self.observers = []

    def add_observer(self,obs):
        self.observers.append(obs)

    def del_observer(self,obs):
        self.observers.remove(obs)
    
    def nofity_observers(self):
        for obs in self.observers:
            obs.action()

    def operation(self):
        self.nofity_observers()

if __name__ == "__main__":
    publish = Publisher()
    publish.add_observer(Obs1())
    publish.add_observer(Obs2())
    publish.operation()
```
---
####状态模式
```

class State:
    def get_statu(self):
        return self.statu

    def set_statu(self,s):
        self.statu = s

    def operate1(self):
        print("execute operate1")
    
    def operate2(self):
        print("execute poerate2")
    

class Context:
    def __init__(self,state):
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self,state):
        self.state = state
    
    def method(self):
        if self.state.get_statu() == "statu1":
            self.state.operate1()
        elif self.state.get_statu() == "statu2":
            self.state.operate2()
        else:
            print("i don`t understand")
    
if __name__ == "__main__":
    s = State()
    context = Context(s)
    s.set_statu("statu1")
    context.method()
    s.set_statu("statu2")
    context.method()
    s.set_statu("statu3")
    context.method()

    

    
```
---
####策略模式
```


class Calculator(object):
    def calculate(self,exp):pass

    def split(self,exp,opt):
        arr = exp.split(opt)
        for i,v in enumerate(arr):
            arr[i] = int(v)
        return arr




class Plus(Calculator):
    def calculate(self,exp):
        result = self.split(exp,'+')
        return result[0] + result[1]


class Multiply(Calculator):
    def calculate(self,exp):
        result = self.split(exp,'*')
        return result[0] * result[1]


if __name__ == "__main__":
    exp = '2+12'
    cal = Plus()
    print(f"result {cal.calculate(exp)}")
    exp = '10*5'
    cal = Multiply()
    print(f"result {cal.calculate(exp)}")
```
---
#### 模板方法
```


class Human(object):
    def breath(self): pass

    def speak(self): pass

    def walk(self): pass

    def eat(self): pass

    def fight(self): pass

    def active(self):
        self.breath()  # 呼吸
        self.walk()  # 走两步
        self.eat()  # 饿了吃东西
        self.speak()  # 吃撑了乱说话
        self.fight()  # 说错话要打架


class YellowPeople(Human):
    def breath(self):
        print("breathing")

    def speak(self):
        print("speak chinese")

    def walk(self):
        print('walk fast')

    def eat(self):
        print('eat rice')

    def fight(self):
        print("Chinese KungFu,come on!")


if __name__ == "__main__":
    yellow_people = YellowPeople()
    yellow_people.active()
```
---
####访问者模式
```


class Vistor:
    def visit(self,subject):
        print(f"visit the object {subject.get_subject()}")


class Subject:
    def accept(self,vistor):
        vistor.visit(self)
    
    def get_subject(self):
        return "i`am subject"


if __name__ == "__main__":
    vistor1 = Vistor()
    vistor2 = Vistor()
    sub = Subject()
    sub.accept(vistor1)
    sub.accept(vistor2)

```
---
#### 抽象工厂模式
```

class Sender(object):
    def auto_send(self):
        pass


class SmsSender(Sender):
    def auto_send(self):
        print('i am sms sender')


class MailSender(Sender):
    def auto_send(self):
        print('i am mail sender')


class SenderProduce(object):
    def produce(self): pass


class SendMailFactory(SenderProduce):
    def produce(self):
        return MailSender()


class SendSmsFactory(SenderProduce):
    def produce(self):
        return SmsSender()


if __name__ == "__main__":
    factory = SendMailFactory()
    sender = factory.produce()
    sender.auto_send()
```
---
#### 建造者模式
```
#
class SmsSender:
    def auto_send(self):
        print('i am sms sender')


class MailSender:
    def auto_send(self):
        print('i am mail sender')



class Builder:
    product = {}
    product.setdefault('sms',[])
    product.setdefault('mail',[])

    def produce_sms(self,count):
        for _ in range(count):
            self.product['sms'].append(SmsSender())
    
    def procude_mail(self,count):
        for _ in range(count):
            self.product['mail'].append(MailSender())

if __name__ == "__main__":
    builder = Builder()
    builder.produce_sms(10)
    builder.procude_mail(10)
    print(builder.product)
```
---
#### 工厂方法模式
```

class Sender(object):
    def auto_send(self):pass


class SmsSender(Sender):
    def auto_send(self):
        print('i am sms sender')


class MailSender(Sender):
    def auto_send(self):
        print('i am mail sender')


class SenderFactory:
    @staticmethod
    def produceSms():
        return SmsSender()
    
    @staticmethod
    def produceMail():
        return MailSender()




if __name__ == "__main__":
    factory = SenderFactory()
    sms = factory.produceSms()
    sms.auto_send()
```
---
#### 原型模式
```

class Point:
    __slots = __ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)


if __name__ == "__main__":

    point = Point(2, 6)
    # point.__dict__={'name':point.__class__.__name__}#测试
    from copy import deepcopy

    point_copy = deepcopy(point)
    print(f"point:id {id(point)};{point.__dict__}")
    print(f"point_copy:id {id(point_copy)};{point_copy.__dict__}")

    point1 = make_object(Point, 10, 30)
    point2 = point1.__class__(7, 8)
    print(f"point1:id {id(point1)};{point1.__dict__}")
    print(f"point2:id {id(point2)};{point2.__dict__}")
```
---
####单例模式
```
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
            cls._inst = super().__new__(cls) #python3
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
```
---
#### 适配器模式
```
class InStudentInfo(object):

    def get_name(self):
        print("my name is In_student")

    def get_age(self):
        print("my age is 18")

    def get_home(self):
        print("i`am from Fujian")

    def get_home_number(self):
        print("my number is: 100200300")


class OutStudent:
    def get_baseinfo(self):
        return {"name": 'out_student', "age": 19}

    def get_homeinfo(self):
        return {"home": "Shanghai", "num": 123123123}


class OutStudentInfo(InStudentInfo,OutStudent):
    def __init__(self):
        self.base_info = super(OutStudentInfo,self).get_baseinfo()
        self.home_info = super(OutStudentInfo,self).get_homeinfo()

    def get_name(self):
        name = self.base_info.get('name')
        print("my name is ",name)
        return name

    def get_age(self):
        age = self.base_info.get('age')
        print("my age is ",age)
        return age

    def get_home(self):
        home = self.home_info.get('home')
        print("i`am from ",home)
        return home

    def get_home_number(self):
        number = self.home_info.get('num')
        print("my number is:",number)
        return number


if __name__ == "__main__":
    #student = InStudentInfo()
    student = OutStudentInfo()
    student.get_name()
    student.get_age()
    student.get_home()
    student.get_home_number()
```
---
#### 桥梁模式
```

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
```
---
#### 组合模式
```
# 二叉树


class Node(object):
    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.children = []

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def add(self, node):
        self.children.append(node)

    def remove(self, node):
        self.children.remove(node)

    def get_children(self):
        return


class Tree(object):
    def __init__(self):
        self.root = Node('root')


if __name__ == '__main__':
    tree = Tree()
    leaf1 = Node('leaf1')
    leaf2 = Node('leaf2')

    leaf1.add(leaf2)
    tree.root.add(leaf1)
```
---
#### 装饰器模式
```


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
```
---
####门面模式
```

class CPU(object):
    def start(self):
        print("cpu start")

    def shutdown(self):
        print('cpu shutdown')


class Memory(object):
    def start(self):
        print("memory start")

    def shutdown(self):
        print('memory shutdown')


class Disk(object):
    def start(self):
        print("disk start")

    def shutdown(self):
        print('disk shutdown')



class Computer(object):
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()


    def start(self):
        print("start the computer!")
        self.cpu.start()
        self.memory.start()
        self.disk.start()
        print("start computer finished！")

    def shutdown(self):
        print('shutdown the computer!')
        self.cpu.shutdown()
        self.memory.shutdown()
        self.disk.shutdown()
        print('computer closed!')


if __name__ == '__main__':
    computer = Computer()
    computer.start()
    computer.shutdown()
```
---
#### 享元模式
```
from enum import Enum
POKER = Enum("Poker","plum diamonds heart spade")


class Poker(object):
    pool = dict()

    def __new__(cls, shape_type, *args, **kwargs):
        model = cls.pool.get(shape_type, None)
        if not model:
            model = super().__new__(cls)
            cls.pool[shape_type] = model
            model.shape_type = shape_type
        return model

    def show_model(self, number):
        print(f"This is <{self.shape_type}:{number}>")


if __name__ == '__main__':
    num = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for n in num:
        poker = Poker(POKER.plum)
        poker.show_model(n)

        poker = Poker(POKER.diamonds)
        poker.show_model(n)

        poker = Poker(POKER.heart)
        poker.show_model(n)

        poker = Poker(POKER.spade)
        poker.show_model(n)

        print()
    print(Poker.pool)
```
---
#### 代理模式
```
class Source(object):
    def __init__(self):
        self.name = "source"

    def method(self): pass


class MySource(Source):
    def method(self):
        print('this my_source method')


class Proxy(Source):
    def __init__(self):
        super().__init__()
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
    print(proxy.name)
```
---
