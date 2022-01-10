from datetime import datetime as dt


class Event:
    """
    This class represents a single event
    """
    __id_event = 0

    def __init__(self, name, date, price, number_of_tickets):
        if not isinstance(name, str) or name == '':
            raise TypeError('The type of name should be a string')
        if not isinstance(date, dt):
            raise TypeError('The type of date should be a datetime')
        if date < dt.now():
            raise ValueError('Sorry, but data cannot be less than data.now')
        if not isinstance(price, (float, int)):
            raise TypeError('The type of price should be a int or float')
        if price <= 0:
            raise ValueError('The value of price should be greater than 0')
        if not isinstance(number_of_tickets, int):
            raise TypeError('The type of number_of_tickets should be a integer')
        if number_of_tickets < 0:
            raise ValueError('The number_of_tickets should be greater than 0')

        Event.__id_event += 1
        self.__id = Event.__id_event
        self.name = name
        self.date = date
        self.price = price
        self.number_of_tickets = number_of_tickets

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
        if not isinstance(date, dt):
            raise TypeError('The type of date should be a datetime')
        if date < dt.now():
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
    def number_of_tickets(self):
        return self.__number_of_tickets

    @number_of_tickets.setter
    def number_of_tickets(self, number):
        if not isinstance(number, int):
            raise TypeError('The type of number_of_tickets should be a integer')
        if number < 0:
            raise ValueError('The number_of_tickets should be greater than 0')
        self.__number_of_tickets = number

    def __str__(self):
        return f'{self.__id} event: ' \
               f'name = {self.__name}, ' \
               f'price = {self.__price}, ' \
               f'date = {self.__date}' \
               f'number of tickets: {self.__number_of_tickets}'
