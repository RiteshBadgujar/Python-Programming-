class A:
    def __init__(self):
        print("Parent constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("Child constructor")

obj = B()
