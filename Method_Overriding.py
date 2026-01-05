class A:
    def show(self):
        print("Parent class call. ")

class B(A):
    def show(self):
        print("Child class call. ")

obj = B()
obj.show()
