# Hierarchical Inheritance
class Father:
    def __init__(self):
        print("Father Class Constructor")
    def ShowF(self):
        print("Father class Instance method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor")
    def ShowS(self):
        print("Son Class instance method")

class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter Class Constructor")

    def ShowD(self):
        print("Daughter Class Instance Method")

d = Daughter()
d.ShowF()
d.ShowD()

s = Son()
s.ShowF()
s.ShowS()
