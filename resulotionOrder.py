class A:

    def info(self):
        print("Ini Class A")

class B:

    def info(self):
        print("Ini Class B")

class C(B,A):
    def info(self):
        print("Ini Class C")



objek = C()
objek.info()
# objek.info_a()
# objek.info_b()
help(objek)