# Multiple Inheritance
# (If class is derived from more than one parent class then it is called  multiple inheritance)

class Father:
    def __init__(self):
        super().__init__()
        print("Father Class Constructor")
    def showF(self):
        print("Father Class instance Method")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother Class Constructor")
    def showM(self):
        print("Mother Class Instance Method")

class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Instance Method")

s = Son()
s.showF()
s.showM()
s.showS()
