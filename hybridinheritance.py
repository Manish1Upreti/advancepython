#Hybridinheritance  is the combination of more than one inheritance
class A:
    def __init__(self):
        print("Class A Constructor")
    def ShowA(self):
        print("Class A Instance Method")

class B (A):
    def __init__(self):
        super().__init__()
        print("Class B Constructor")
    def ShowB(self):
        print("Class B Instance Method")

class C (B,A):
    def __init__(self):
        super().__init__()
        print("Class C Constructor")
    def ShowC(self):
        print("Class C instance Method")

c = C()
c.ShowA()
c.ShowB()
c.ShowC()
c= C()