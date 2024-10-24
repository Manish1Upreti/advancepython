# Single Inheritance in which a class is derived from only one base class
class Father:
    property = "$250k"

    def show(self):
        print("Parent Class Instance Method")

    @classmethod
    def showproperty(cls):
        print("Parent class Class Method:", cls.property)

    @staticmethod
    def stat():
        land = "10 acer"
        print("Parent Class Static Methid", land)

class Son (Father):
    def disp(self):
        print("Child Class Instance Method")

s = Son()
s.show()
s.showproperty()
s.stat()
s.disp()