class A:

    def info(self):
        print("Ini Class A")

class B(A):
    def info(self):
        print("Ini Class B")
    pass

class C(A):
    def info(self):
        print("Ini Class C")
    pass

class D(B,C):
    pass

objek = D()
objek.info()
help(objek)