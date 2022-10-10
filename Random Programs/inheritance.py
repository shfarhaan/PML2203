class Dada:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")


class Baba(Dada):
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")


class Nana:
    def feature7(self):
        print("This is feature 7")

    def feature8(self):
        print("This is feature 8")


class Amma(Nana):
    def feature4(self):
        print("This is feature 4")

    def feature5(self):
        print("This is feature 5")


class Me(Baba, Amma):
    pass


a1 = Baba()

b1 = Amma()

c1 = Me()

print(c1.feature8())
