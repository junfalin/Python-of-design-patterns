#策略模式


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
