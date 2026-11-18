class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, name):
        self.name = name
        self.students = [] # List of Students
        self.teachers = [] # List of Teachers

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

# Keep the class name consistent for code that uses lowercase ``school``.
# A subclass preserves School's constructor and avoids replacing it with a
# zero-argument placeholder in code that imports ``school``.
class school(School):
    """Lowercase-compatible alias with the same constructor as School."""
    pass

#Example usage
school1 = School(name="Philippine Science High School MRC")
t1 = Teacher("Sir Leonil")
t2 = Teacher("Ma'am Carmel")
s1 = Student("Veronica Sawyer")
s2 = Student("Jason Dean")
school1.add_student(s1)
school1.add_student(s2)
school1.add_teacher(t1)
school1.add_teacher(t2)
school2 = School(name="Westerburg High School")
t3 = Teacher("Ma'am Ream")
s3 = Student("Heather Chandler")
s4 = Student("Heather Duke")
s5 = Student("Heather McNamara")
school2.add_student(s3)
school2.add_student(s4)
school2.add_student(s5)
school2.add_teacher(t3)

print("School Name:", school1.name)
print("Students:")
for student in school1.students:
    print("-", student.name)
print ("--------------------------------")
print("Teachers:")
for teacher in school1.teachers:
    print("-", teacher.name)
print ("--------------------------------")
print("\nSchool Name:", school2.name)
print("Students:")
for student in school2.students:
    print("-", student.name)
print ("--------------------------------")
print("Teachers:")
for teacher in school2.teachers:
    print("-", teacher.name)
    