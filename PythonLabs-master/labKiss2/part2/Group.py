from Student import Student


class Group:
    """This class represents a group entity"""
    __group_id = 0

    def __init__(self, *students_list):
        Group.__group_id += 1
        self.__id = Group.__group_id
        self.max_size = 20
        # if len(students_list) > self.max_size:
        #     raise ValueError('Sorry, but need to limit the list of students')
        self.students = list(students_list)

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        if not isinstance(students, list):
            raise TypeError('Students must be a type(list)')
        if not all(isinstance(student, Student) for student in students):
            raise TypeError('Student must be a type(Student)')
        if 0 > len(students) > self.__max_size:
            raise ValueError('Sorry, but need to limit the students list')
        self.__students = students

    @property
    def max_size(self):
        return self.__max_size

    @max_size.setter
    def max_size(self, max_size):
        if not isinstance(max_size, int):
            raise TypeError('New max size of group must be a type(Student)')
        if max_size < 0:
            raise ValueError('New max size should not be less than 0')
        self.__max_size = max_size

    @property
    def id(self):
        return self.__id

    def add(self, student):
        if not isinstance(student, Student):
            raise TypeError('Student must be a type(Student)')
        if len(self.__students) == self.__max_size:
            raise ValueError(f'The {self.__group_id} must have at least not more {self.__max_size} students')
        if student in self.__students:
            raise ValueError(f'The {self.__group_id} already has this student')
        self.__students.append(student)

    def delete(self, student):
        if not isinstance(student, Student):
            raise TypeError('Student must be a type(Student)')
        if not student in self.__students:
            raise ValueError(f'The {student} can not be found in the list of students')
        self.__students.remove(student)

    def top_five_students(self):
        self.__students.sort(reverse=True, key=lambda x: x.average_grade_student())
        list_students = '\n\t'.join(map(str, self.__students[:5]))
        return list_students

    def __str__(self):
        list_students = '\n\t'.join(map(str, self.__students))
        return f'Group {self.id} consist of {len(self.__students)}:\n\t{list_students}'
