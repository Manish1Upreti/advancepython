# This method is used to access or read and modify data of the variables
class Car:
    def __init__(self):
        self.model = "Tesla V"     # Instance Variable

    def show_Model(self):
        print(self.model)

    def set_model(self):
        self.model = "Tesla X"    # Mutator Method

tesla = Car()
# Before Setting
tesla.show_Model()
# After Setting
tesla.set_model()
tesla.show_Model()


# with parameter
class Car:
    def set_model(self, m):
        self.model = m

bmw = Car()
bmw.set_model("bmw x")
print(bmw.model)