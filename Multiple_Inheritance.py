class A:
    def msgA(self):
        print("Hello from A..")

class B:
    def msgB(self):
        print("Hello from B..")

class C(A, B):
    pass

obj = C()
obj.msgA()
obj.msgB()
