class A:
    def show(self):
        print("A class. ")

class B(A):
    pass

class C(A):
    def show(self): 
        print("C class.")

class D(B, C):
    pass

D().show()
