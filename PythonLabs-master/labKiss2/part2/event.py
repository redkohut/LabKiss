from datetime import datetime as dt
from datetime import date as dat


class Event:
    """
    This class represents a single event
    """
    __id_event = 0

    def __init__(self, name, id, date, price, number_of_tickets):
        if not isinstance(name, str) or name == '':
            raise TypeError('The type of name should be a string')
        if not isinstance(date, dat):
            raise TypeError('The type of date should be a datetime')
        if date < dat.today():
            raise ValueError('Sorry, but data cannot be less than data.now')
        if not isinstance(price, (float, int)):
            raise TypeError('The type of price should be a int or float')
        if price <= 0:
            raise ValueError('The value of price should be greater than 0')
        if not isinstance(id, int):
            raise TypeError('The type of id should be an integer')

        self.id = id
        self.name = name
        self.date = date
        self.price = price
        self.number = number_of_tickets

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, idd):
        if not isinstance(idd, int):
            raise TypeError('The type of id should be an integer')
        self.__id = idd

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or name == '':
            raise TypeError('The type of name should be a string')
        self.__name = name

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if not isinstance(date, dat):
            raise TypeError('The type of date should be a datetime')
        if date < dat.today():
            raise ValueError('Sorry, but data cannot be less than data.now')
        self.__date = date

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError('The type of price should be a int or float')
        if price <= 0:
            raise ValueError('The value of price should be greater than 0')
        self.__price = price

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError('The type of number_of_tickets should be an integer')
        self.__number = number

    def __str__(self):
        return f'{self.__name} event: ' \
               f'id = {self.__id}, ' \
               f'standard price = {self.__price}, ' \
               f'event date = {self.__date}' \

