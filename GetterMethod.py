# This method is used to  just access or read data of the variables
class Car:
    def __init__(self):
        self.model = "Tesla V"    # Instance Variable

    def get_model(self):         # Accessor Method
        return self.model

tesla = Car()
m = tesla.get_model()          # Calling Accessor method
print(m)
