import unittest
from student.student import Student

class TestStudent(unittest.TestCase):

    def test_creat_student_object(self):
        new_student = Student ('Taif')
        self.assertEqual(new_student.name,"Taif")