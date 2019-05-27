# 迭代器模式


class Interator(object):
    def __init__(self, coll):
        self.collection = coll
        self.pos = -1

    def previous(self):
        if self.pos > 0:
            self.pos -= 1
        return self.collection.get(self.pos)

    def next(self):
        if self.pos < self.collection.size()-1:
            self.pos += 1
        return self.collection.get(self.pos)

    def hasnext(self):
        if self.pos < self.collection.size()-1:
            return True
        return False

    def hasprevious(self):
        if self.pos > 0:
            return True
        return False

class Collection(object):
    def __init__(self):
        self.collection = [1,2,3,4,5,6,7,8,9,10]

    def new_iterator(self):
        return Interator(self)

    def get(self, index):
        return self.collection[index]

    def size(self):
        return len(self.collection)


if __name__ == "__main__":
    coll = Collection()
    it = coll.new_iterator()
    while(it.hasnext()):
        print(f"{it.next()}")
    while(it.hasprevious()):
        print(f"{it.previous()}")