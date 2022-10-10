class A:
    def __init__(self, feature1):
        print("This is feature1")

    def feature2(self, feature2):
        print("This is feature2")


class B:
    def __init__(self, feature3):
        print("This is feature3")

    def feature4(self, feature4):
        print("This is feature4")


class C(A, B):
    def feature5(self, feature5):
        print("This is feature5")

    def feature6(self, feature6):
        print("This is feature6")

#
# a1 = A()
# b1 = B()
# c1 = C()
#
