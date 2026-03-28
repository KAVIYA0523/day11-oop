class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)

p1 = Person("Kaviya", 22, "Chennai")
p1.profile()