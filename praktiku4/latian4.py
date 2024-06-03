class A:
    def info(self):
        print("Ini Class A")
        pass

class B(A):
    def info(self):
        print("Ini Class B")
        pass


class C(A):
    def info(self):
        print("Ini Class C")
        pass


class D(B):
    def info(self):
        print("Ini Class D")
        pass


class E(D,C):
    pass

object = E()
object.info()
help(object)