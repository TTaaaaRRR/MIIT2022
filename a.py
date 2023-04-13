from studentdb import Students
import random

names = ['Антон', 'Михаил', 'Фёдор', 'Александр', 'Павел']
departments = ['АВИШ', 'ИТТСУ', 'ИЭ']
marks = [2, 3, 4, 5]

DB = Students("stud.sqlite")

for _ in range(0, 100):
    DB.addStudent(random.choice(names), random.choice(departments), random.choice(marks), random.choice(marks), random.choice(marks))

#for student in DB.getStudents():
#    print(student)

DB.otchisl()
print("\nStudents removed\n")

print(len(DB.getStudents()))

