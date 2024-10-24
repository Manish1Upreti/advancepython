# Method Overloading
# In java when more than one method with the same name is defined in the same class it is known as method overloading
# In python if a method is written such that it can perform  more than one task it is called method overloading
 # this is java type
# class Myclass:
#     def sum(self, a):  # 1st instance method
#         print("1st Sum Method", a)
#
#     def sum(self):  # 2nd instance method
#         print("2nd Sum Method")
#
# obj = Myclass()
# obj.sum()

# Method overloading in python
class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = 'Provide at least Two Numbers'
        return s

obj = Myclass()
print(obj.sum(20, 30, 40))
print(obj.sum(10, 20))
print(obj.sum())
