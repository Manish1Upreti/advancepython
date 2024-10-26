class Employee:
    empCount = 0       # Class variable
    def __init__(self):
        self.name = input("Enter name: ")
        self.designation = input("Enter Designation: ")
        Employee.empCount += 1

    def show(self):
        print("Name is ", self.name, "Designation is", self.designation)


emp = Employee()
emp.show()
print("Total no of Employee is ", Employee.empCount)
