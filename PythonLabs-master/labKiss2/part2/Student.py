class Student:
    """This class represents a student entity"""
    __record_book_id = 0

    def __init__(self, name='Unknown', surname='Unknown', grades=None):
        Student.__record_book_id += 1
        self.__book_id = Student.__record_book_id
        self.name = name
        self.surname = surname
        self.grades_student = grades

    @property
    def book_id(self):
        return self.__book_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or new_name == '':
            raise TypeError('Name must be a string')
        self.__name = new_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        if not isinstance(new_surname, str) or new_surname == '':
            raise TypeError('Surname must be a string')
        self.__surname = new_surname

    @property
    def grades_student(self):
        return self.__grades_student

    @grades_student.setter
    def grades_student(self, new_grades):
        if not isinstance(new_grades, dict):
            raise TypeError('Grades must be of type dict')
        if any(not isinstance(key, str) for key in new_grades.keys()):
            raise TypeError('Grade\'s key must be a string')
        if any(not isinstance(value, int) for value in new_grades.values()):
            raise TypeError('Grade\'s value must be a integer')
        if any(value < 0 or value > 100 for value in new_grades.values()):
            raise ValueError('Grade must be consist in range from 0 to 100')
        self.__grades_student = new_grades

    def average_grade_student(self):
        return sum(self.__grades_student.values()) / len(self.__grades_student)

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.name, self.surname) == (other.name, other.surname)
        else:
            return False

    def __hash__(self):
        return hash((self.name, self.surname))

    def __str__(self):
        return f'Record number = {self.__book_id} --- ' \
               f'{self.__name} {self.__surname} and his grades:{self.__grades_student}'


