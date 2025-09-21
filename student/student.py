# Pascal Case for classes
class Student():
    
    #  Store name, and list of grades
    def __init__(self, name):
        self.name = name
        self.grades = []
        
    

student_name = input("Enter the new student name: ")
new_student = Student (student_name)
print (f'welcome {new_student.name}')