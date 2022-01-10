from datetime import datetime as dt
from datetime import date as dat


class Ticket:
    """
    This class represents a tickets entity
    """
    __id_ticket = 0
    __number_tickets = 100

    def __init__(self, name, date, price):
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
        # if not isinstance(number_of_tickets, int):
        #     raise TypeError('The type of number_of_tickets should be a integer')
        # if number_of_tickets < 0:
        #     raise ValueError('The number_of_tickets should be greater than 0')

        Ticket.__number_tickets -= 1
        Ticket.__id_ticket += 1
        self.__id = Ticket.__id_ticket
        self.name = name
        self.date = date
        self.number_of_tickets = Ticket.__number_tickets
        self.price = price

    @property
    def id(self):
        return self.__id

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
            raise TypeError('The type of date should be a date')
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
    def number_of_tickets(self):
        return self.__number_of_tickets

    @number_of_tickets.setter
    def number_of_tickets(self, number):
        if not isinstance(number, int):
            raise TypeError('The type of number_of_tickets should be a integer')
        if number < 0:
            raise ValueError('The number_of_tickets should be greater than 0')
        self.__number_of_tickets = number

    def buy_ticket(self):
        if Ticket.__number_tickets - 1 < 0:
            raise ValueError('Sorry, but the tickets are ending')
        print('Number: ', Ticket.__number_tickets)
        self.__number_of_tickets = Ticket.__number_tickets

    def __str__(self):
        return f'{self.name}\n' \
                   f'   ID: {self.__id_ticket}\n' \
                   f'   Date: {self.date}\n' \
                   f'   Remaining number of tickets: {self.__number_tickets}\n' \
                   f'   Price: {self.price}'


class AdvanceTicket(Ticket):
    #__number_tickets = 0

    def __init__(self, name, date, price):
        super().__init__(name, date, price)
        self.price = self.price * 0.6
    #     AdvanceTicket.__number_tickets = number_of_tickets
    #
    # @staticmethod
    # def buy_ticket():
    #     if AdvanceTicket.__number_tickets - 1 < 0:
    #         raise ValueError('Sorry, but the tickets are ending')
    #     AdvanceTicket.__number_tickets -= 1


class StudentTicket(Ticket):
    #__number_tickets = 0

    def __init__(self, name, date, price):
        super().__init__(name, date, price)
        self.price = self.price * 0.5
    #     StudentTicket.__number_tickets = number_of_tickets
    #
    # @staticmethod
    # def buy_ticket():
    #     if StudentTicket.__number_tickets - 1 < 0:
    #         raise ValueError('Sorry, but the tickets are ending')
    #     StudentTicket.__number_tickets -= 1


class LateTicket(Ticket):
   # __number_tickets = 0

    def __init__(self, name, date, price):
        super().__init__(name, date, price)
        self.price = self.price * 1.1
    #    LateTicket.__number_tickets = number_of_tickets

    # @staticmethod
    # def buy_ticket():
    #     if LateTicket.__number_tickets - 1 < 0:
    #         raise ValueError('Sorry, but the tickets are ending')
    #     LateTicket.__number_tickets -= 1
