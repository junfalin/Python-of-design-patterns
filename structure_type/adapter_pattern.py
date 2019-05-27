# 适配器模式
class InStudentInfo(object):

    def get_name(self):
        print("my name is In_student")

    def get_age(self):
        print("my age is 18")

    def get_home(self):
        print("i`am from Fujian")

    def get_home_number(self):
        print("my number is: 100200300")


class OutStudent:
    def get_baseinfo(self):
        return {"name": 'out_student', "age": 19}

    def get_homeinfo(self):
        return {"home": "Shanghai", "num": 123123123}


class OutStudentInfo(InStudentInfo,OutStudent):
    def __init__(self):
        self.base_info = super(OutStudentInfo,self).get_baseinfo()
        self.home_info = super(OutStudentInfo,self).get_homeinfo()

    def get_name(self):
        name = self.base_info.get('name')
        print("my name is ",name)
        return name

    def get_age(self):
        age = self.base_info.get('age')
        print("my age is ",age)
        return age

    def get_home(self):
        home = self.home_info.get('home')
        print("i`am from ",home)
        return home

    def get_home_number(self):
        number = self.home_info.get('num')
        print("my number is:",number)
        return number


if __name__ == "__main__":
    #student = InStudentInfo()
    student = OutStudentInfo()
    student.get_name()
    student.get_age()
    student.get_home()
    student.get_home_number()
