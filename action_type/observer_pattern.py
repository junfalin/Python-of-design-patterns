#观察者模式
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
