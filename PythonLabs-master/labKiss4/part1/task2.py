from datetime import date
from person import Person
from notebbok import Notebook


def main():
    person1 = Person('Denchik', 'Perec', '0102102102', date(2003, 7, 19))
    person2 = Person('Masha', 'Taivovna', '0101101101', date(2004, 8, 4))
    person3 = Person('Zhenchik', 'Zakharchuk', '0970807396', date(2003, 2, 26))
    person4 = Person('Ann', 'Coolenko', '0938938902', date(2000, 3, 23))
    notebook = Notebook(person1, person2, person3)
    notebook += person4
    print(notebook)
    notebook -= person3
    print(*(notebook*'Denchik'))


if __name__ == '__main__':
    main()
