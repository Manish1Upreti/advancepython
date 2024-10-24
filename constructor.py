#Constructor
# Python supports a special type of method called constructor for initializing the instance variable of a class
class Car:
    # Constructor without parameter
    def __init__(self):
        self.model = "XYZ"

    def show_model(self):
        print("Model:", self.model)

hundai = Car()
hundai.show_model()

class Car1:
    # Constructor
    def __init__(self, m, P=200):
        self.model = m    # Instance Variable
        self.power = P

    def show_model(self, p):   # Instance Method
        price = p   # Local Variable
        print("Model:", self.model, "Power:", self.power)  # Accessing Instance Variable
        print("Price:", price)

# Passing Argument to Constructor
hundai = Car1("XYZ")
bmw = Car1("V", 500)

# Accessing Method from outside class
hundai.show_model(1000)
bmw.show_model(2000)

print(id(hundai))
print(id(bmw))
