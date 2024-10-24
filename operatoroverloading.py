# Operator overloading
# if any operator perform additional actions other than what it is meant for, it is called operator overloading
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return 'Radius of the circle is: {}'.format(self.radius)

    def __add__(self, other_circle):
        return Circle(self.radius + other_circle.radius)

    def __sub__(self, other):
        return self.radius-other.radius

c1 = Circle(2)
c2 = Circle(6)
c3 = c1 + c2         # Cricle.__add__(c1,c2)
c4 = c2 - c1         # Circle.__sub__(c2,c1)
print("Difference of two circle is ", c4)
print(c3)

10+20                # int.__add__(10,20)
'a'+'b'              # str.__add__('a','b')

print(Circle.__add__(c1, c2))
