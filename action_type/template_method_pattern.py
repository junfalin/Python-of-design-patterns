# 模板方法


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
