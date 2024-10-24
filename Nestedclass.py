# A class within a class is called as nested classs
class Army:                 # outer class
    def __init__(self):
        self.name = 'Rahul'
        self.gn = self.Gun()  # Creating inner class object
    def show_name(self):
        print("Name:", self.name)


    class Gun:
        def __init__(self):
            self.name = "AK47"
            self.capacity = "75 Rounds"
            self.length = '34.3 In'

        def dis(self):
            print("Gun Name:", self.name)
            print("Capacity:", self.capacity)
            print("Length:", self.length)

a = Army()
a.show_name()

# g = Army().Gun()
# or
g = a.gn
g.dis()
