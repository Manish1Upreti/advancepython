# Constructor in Inheritance
class Father:
    def __init__(self, m):     # Constructor
        self.property = m     # Instance Variable
        print("Father Class Constructor")

    def show(self):
        print("Father Class instance Method")

class Son (Father):
    def disp(self):
        print("Son Class instance Method", self.property + 10000)

s = Son(250000)
s.disp()
s.show()
