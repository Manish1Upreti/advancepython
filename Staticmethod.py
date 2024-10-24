# Static method are used when some processing is related to the class but does not need the class or its instances to perform any work
# We use static method when we want to pass some values from outside and perform some action in the method
#
class Car:

    @staticmethod       # Decorator
    def show_model(m, p):  # Static Method
        model = m
        price = p
        print("Model:", model, "price:", price)

tesla = Car()
Car.show_model("Tesla X", "$35000")  # Calling Static Method
