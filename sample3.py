class Book:
    def __init__(self, n):
        self.name = n

    def show(self):
        print("Name of book is ", self.name)

def bookname(obj):  # using Function
    obj.name = input("Enter book name:")
    return Book(obj.name)

b = Book("k")
bookname(b)
b.show()