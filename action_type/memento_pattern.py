# 备忘录模式
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

