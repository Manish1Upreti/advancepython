# Class Variable or Static Variable with Class Method

class Car:
    Ad = "Yes"              # Class Variable global

    def __init__(self, m):
        self.model = m   # Instance Variable

    def show_model(self):         # Instance Method
        print("Model:", self.model)  # Accessing Instance variable

    @classmethod                      # Class Method is usually use for class variable
    def is_Ad(cls, hp):
        cls.horsepower = hp    # class variable local
        print("Auto Drive: ", cls.Ad)    # Accessing Class Variable
        print("Power", cls.horsepower)

tesla = Car("Tesla V")
bmw = Car("BMW X")
jawazar = Car("TATA W")

tesla.show_model()
bmw.show_model()

print("Tesla Auto Drive:", Car.Ad)
print("BMW Auto Drive:", Car.Ad)

Car.is_Ad("200 hp")      #  calling Class Method

Car.Ad = "No"           # Modifying Class Variable
print("Jawazar Auto Drive:", Car.Ad)

Car.Ad = "NOT AUTO Drive"
print("Jawazar is :", Car.Ad)
