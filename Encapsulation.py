class Student:
    def __init__(self, name):
        self.__name = name   # private variable

    def show_name(self):
        print("Name:", self.__name)

s = Student("Ritesh")
s.show_name()
