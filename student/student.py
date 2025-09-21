class Student:
    # Store a student’s name and a list of grades.
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        # Method to add a grade (0 to100 only). Invalid grades should raise an error.
        if grade >= 0 and grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError('Grade Must be between 0 and 100 inclusive')
    
    def average(self):
        # Method to calculate the average of grades. If no grades, return 0.
        if not self.grades:
            return 0
        
        total = 0
        for grade in self.grades:
            total += grade
        average = total / len(self.grades)
        return average


if __name__ == '__main__':
    # this is where the user faceing "program" goes
    student_name = input('Enter the new student name: ')
    new_student = Student(student_name)
    print(f'Welcome {new_student.name}')
    new_grade = input('Add grade to student: ')
    try:
        new_student.add_grade(int(new_grade))
    except ValueError as err:
        # To get the error message we included on line 12
        print(err)