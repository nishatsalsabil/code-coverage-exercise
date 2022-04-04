from student.student import Student, get_student_with_more_classes


samara = Student("Samara", "Junior", ["Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition"])
samara.add_class("Painting")
class_num = samara.get_num_classes()
print(class_num)
print(samara.summary())
print()

claire = Student("Claire", "Freshman", ["Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science"])
claire.add_class("Painting")
class_num = claire.get_num_classes()
print(class_num)
print(claire.summary())
print()

print(f"Samara is ID: {samara}")
print(f"Claire is ID: {claire}")
print(f"Student with more classes is ID: {get_student_with_more_classes(claire, samara)}")