class A:
    def show(self):
        print("Parent class call.")
        print("Use super keyword.")

class B(A):
    def show(self):
        super().show()
        print("Child class call.")

obj = B()
obj.show()
