#解释器模式
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
