#状态模式

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

    

    
