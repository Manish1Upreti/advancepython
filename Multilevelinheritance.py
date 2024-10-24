# In multi-level inheritance, the class inherits the feature of another derived class (child class)
class Father(object):
    def __init__(self):
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Method")

class Son(Father):
    def __init__(self):
        super().__init__()     # Calling Father Class Constructor
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Method")

class GrandSon(Son):
    def __init__(self):
        super().__init__()      # Calling Son class Constructor
        print("GrandSon Class Constructor")
    def showG(self):
        print("GrandSon Class Method")

g = GrandSon()
