#门面模式

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