class Person:
    skills = []


    def persondetail(self):
        self.firstname = input("Enter Name: ")
        self.lastname = input("Enter Lastname: ")
        self.age = int(input("Enter age: "))
        self.country = input("Enter Country: ")
        self.city = input("Enter city: ")

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)


p1 = Person()
p1.persondetail()

print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
print(p1.skills)
# p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
# print(p2.person_info())
# print(p1.skills)
# print(p2.skills)