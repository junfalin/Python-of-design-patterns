# 原型模式

class Point:
    __slots = __ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)


if __name__ == "__main__":

    point = Point(2, 6)
    # point.__dict__={'name':point.__class__.__name__}#测试
    from copy import deepcopy

    point_copy = deepcopy(point)
    print(f"point:id {id(point)};{point.__dict__}")
    print(f"point_copy:id {id(point_copy)};{point_copy.__dict__}")

    point1 = make_object(Point, 10, 30)
    point2 = point1.__class__(7, 8)
    print(f"point1:id {id(point1)};{point1.__dict__}")
    print(f"point2:id {id(point2)};{point2.__dict__}")
