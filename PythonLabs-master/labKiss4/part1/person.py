from datetime import date


class Person:
    """This class representing a simple way to initialize a Person"""
    __id = 0

    def __init__(self, name='None', surname='None', telephone='0123456789', birthday=date.today()):
        Person.__id += 1
        self.person_id = Person.__id
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('The type of name must be a string')
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError('The type of surname must be a string')
        self.__surname = surname

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        if not all(number in '0123456789' for number in telephone):
            raise ValueError('The telephone number must contain only numbers 0123456789')
        self.__telephone = telephone

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, dat):
        if not isinstance(dat, date):
            raise TypeError('The type of birthday date must be datetime.date')
        self.__birthday = dat

    def __str__(self):
        return f'User [name = {self.name}, surname = {self.surname}, telephone = {self.telephone}, ' \
               f'birthday = {self.birthday}]'
