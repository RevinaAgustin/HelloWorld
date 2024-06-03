class A:
    def info(self):
        print("ini class A")

class B:
    def info(self):
        print("ini class B")

class c(B, A):
    #def info(self):
        print("ini class C")

objek = c()
objek.info()
#objek.info_b()
help(objek)