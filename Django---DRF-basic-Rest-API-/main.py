# class student():
#         s =[]
#         a = int(input("enter number of student you want:"))
#         for i in range(0,a):
#                 name = input("eenter name:")
#                 marks = int(input("Enter marks:"))
#                 roll = int(input("enter roll:"))
#                 s.append(name)
#                 s.append(marks)
#                 s.append(roll)
# print(student)                


class Student:
    def __init__(self, name, marks, roll):
        self.name = name
        self.marks = marks
        self.roll = roll

students = []
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input("Enter the name of student {}: ".format(i+1))
    marks = int(input("Enter the marks of student {}: ".format(i+1)))
    roll = int(input("Enter the roll of student {}: ".format(i+1)))
    student = Student(name, marks, roll)
    students.append(student)

for student in students:
    print(student.name, student.marks, student.roll)
