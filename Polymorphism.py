# Polymorphism is a word that come from two word poly means many and morphs means forms
# If a variable, object or method perform different behavior according to situation, it is called polymorphism
# Duck Typing
# Operator Overloading
# Method Overloading
# Method Overriding

# Duck Typing
class Duck:
    def walk(self):
        print("Walk duck thapak thapak")
class Donkey:
    def walk(self):
        print("Walk Donkey tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow")

def myFunction(obj):           # function
    if hasattr(obj, 'walk'):   # using strong typing as hasattr()
        obj.walk()
    if hasattr(obj, 'talk'):
        obj.talk()

d = Duck()
d.walk()
myFunction(d)

du = Donkey()
du.walk()
myFunction(du)

a = 10
print(type(a))

c = Cat()
myFunction(c)


