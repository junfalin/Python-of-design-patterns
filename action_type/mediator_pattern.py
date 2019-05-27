#中介者模式
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

