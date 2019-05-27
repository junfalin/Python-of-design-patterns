#访问者模式


class Vistor:
    def visit(self,subject):
        print(f"visit the object {subject.get_subject()}")


class Subject:
    def accept(self,vistor):
        vistor.visit(self)
    
    def get_subject(self):
        return "i`am subject"


if __name__ == "__main__":
    vistor1 = Vistor()
    vistor2 = Vistor()
    sub = Subject()
    sub.accept(vistor1)
    sub.accept(vistor2)

