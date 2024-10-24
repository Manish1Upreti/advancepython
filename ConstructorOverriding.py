# If we write constructor in both classes, parent class and
# child class then the parent class constructor is not available to the child class
# Constructor overriding is used when programmer want to modify the existing behavior of a constructor
class Father:
    def __init__(self):
        self.property = 250000
        print("Father Class Constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def __init__(self, p):
        self.property = p
        self.car = "BMW"
        print("Son Class Constructor")

    def disp(self):
        print("Son Property:", self.property, "Son Car:", self.car)

s = Son(10000)
s.disp()
print(s.car)
print(s.property)
s.show()
