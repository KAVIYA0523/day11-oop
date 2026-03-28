class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student(1, "Kaviya", 85)
s1.display()