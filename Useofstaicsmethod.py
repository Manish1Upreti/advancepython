# Passing Member of one Class to another class
class Student1:
    def __init__(self):
        n = input("Enter your Name:")
        r = int(input("Enter Roll:"))
        self.name = n
        self.roll = r

    def disp(self):
        print("Student Name:", self.name)
        print("Student Roll:", self.roll)

class User:
    # Static Method
    @staticmethod
    def show(s):
        print("User name: ", s.name)
        print("User Roll:", s.roll)
        s.disp()

# Creating Object of Student Class
stu = Student1()

User.show(stu)
