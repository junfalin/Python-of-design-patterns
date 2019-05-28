# 命令模式
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
