# Super Method  which help to access both constructor
class Father:                     # Parent Class
    def __init__(self, m):
        self.property = m    # instance variable
        print("Father Class Constructor")
    def show(self):
        print("Father Class Instance Method")

class Son (Father):
    def __init__(self, m, j):
        super().__init__(m)         # Calling Parent Class Constructor
        print("Son class constructor")
        self.job = j

    def disp(self):
        print("Son class instance method", self.property, "Son Job:", self.job)

s = Son(250000, "Programmer")
s.disp()