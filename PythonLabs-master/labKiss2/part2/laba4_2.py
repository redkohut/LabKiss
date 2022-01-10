from datetime import date
class Notebook:
    """This class is a template for creating a notebook"""
    __id = 0

    def __init__(self, *person):
        self.notes = list(person)
        Notebook.__id += 1
        self.id = Notebook.__id

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        if not isinstance(notes, list):
            raise TypeError('The type of notes must be list')
        if not all(isinstance(note, Person) for note in notes):
            raise TypeError('The note should be of type Person')
        self.__notes = notes

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise TypeError('The type of id must be integer')
        self.__id = id

    def __iadd__(self, obj):
        if not isinstance(obj, Person):
            raise TypeError('The type of object must be Person')
        self.notes.append(obj)
        return self

    def __isub__(self, obj):
        if not isinstance(obj, Person):
            raise TypeError('The type of object must be Person')
        self.notes.remove(obj)
        return self

    def __mul__(self, value):
        output_list = list()
        if isinstance(value, str) and len(value) != 10 and all(num in '0123456789' for num in value):
            for note in self.notes:
                if note.telephone == value:
                    # find notes for
                    output_list.append(note)
        elif isinstance(value, str):
            for note in self.notes:
                if note.name == value or note.surname == value:
                    output_list.append(note)
        elif isinstance(value, date):
            for note in self.notes:
                if note.birthday == value:
                    output_list.append(note)
        if output_list:
            return output_list
        else:
            raise ValueError('The strange argument')

    def __str__(self):
        notes = '\n\t'.join(map(str, self.__notes))
        return f'Notebook {self.id} consists of {len(self.__notes)} notes:\n\t{notes}'


if __name__ == '__main__':
    number = '0970807&96'
    print(all(c in '0123456789' for c in number))


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



