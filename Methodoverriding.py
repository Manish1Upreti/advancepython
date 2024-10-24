# Methodoverriding
# if we write method in both classes, parent class and child class then the parent class's method is not available to the child class
# in this case only child class's method is accessible which means child class's method is replacing parent class's method
 # so use super() method to access parent method having same name
class Add:
    def result(self, a, b):
        m = a
        n = b
        print("Addition:", m+n)

class Multi(Add):
    def result(self):
        m = int(input("Enter one Number"))
        n = int(input("Enter another Number"))
        super().result(m, n)                     # Calling Parent Class's Method (as having same name as result)
        print("Multiplication", m*n)

m = Multi()
m.result()

