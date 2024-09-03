class Student:

    class_year = 2024
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1

student1 = Student("Motu", 22)
student2 = Student("Patlu", 24)
student3 = Student("Dholu", 21)
student4 = Student("Bholu", 21)

print(f"My graduating class of {Student.class_year} had {Student.num_of_students} students in it")
print(f"{student1.name} - {student1.age}")
print(f"{student2.name} - {student2.age}")
print(f"{student3.name} - {student3.age}")
print(f"{student4.name} - {student4.age}")