# A python class is a group of attributes and methods.
# Attributes are represented by variable that contains data.
# Method performs an actions or task. It is similar to function
# Object is class type variable or class instance.
class Car(object):
    def __init__(self, m):  # Constructor
        self.model = m  # Variable 0r Attribute

    def show_model(self, p, dom):     # Method
        self.price = p
        self.DOM = dom
        print('Model:', self.model, "Price:", self.price, "DOM:", self.DOM )


bmw = Car('BMW-VI')
bmw.show_model(10000, 1997)

VW = Car('VW-X')
VW.show_model(20000, 1998)

Toyota = Car('Toyota-Z')
Toyota.show_model(15000, 2001)



