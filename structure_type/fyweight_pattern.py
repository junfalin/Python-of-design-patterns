# 享元模式
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