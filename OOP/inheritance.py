class A:
    def feature1(self):
        print("This is feature1")

    def feature2(self):
        print("This is feature2")

class B:
    def feature3(self):
        print("This is feature3")

    def feature4(self):
        print("This is feature4")


class C(A, B):
    def feature5(self):
        print("This is feature5")

    def feature6(self):
        print("This is feature6")

a1 = A()
b1 = B()
c1 = C()


