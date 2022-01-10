import json
from datetime import datetime as dt


class Ticket:
    """
    This class represents a tickets entity
    """
    __id_ticket = 0

    def __init__(self, name, date, number_of_tickets, price):
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

        Ticket.__id_ticket += 1
        self.__id = Ticket.__id_ticket
        self.name = name
        self.date = date
        self.number_of_tickets = number_of_tickets
        self.price = price

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

    # def return_ticket(self):
    #     with open('events.json', 'r') as file:
    #         json_dict = json.load(file)
    #     dict_of_attributes = json_dict[str(self.__id)]
    #     dict_of_attributes['number_of_tickets'] += 1
    #     json_dict[str(self.__id)] = dict_of_attributes
    #     with open('events.json', 'w') as file:
    #         json.dump(json_dict, file, indent=4)
    #     print('Ticket was returned!')
    #     self.number_of_tickets += 1

    # @classmethod
    # def construct_by_id(cls, id):
    #     with open('events.json', 'r') as file:
    #         json_dict = json.load(file)
    #         try:
    #             dict_of_attributes = json_dict[str(id)]
    #         except:
    #             raise
    #     if not dict_of_attributes['number_of_tickets']:
    #         raise ValueError('Tickets for this event have run out!')
    #     dict_of_attributes['number_of_tickets'] -= 1
    #     json_dict[str(id)] = dict_of_attributes
    #     with open('events.json', 'w') as file:
    #         json.dump(json_dict, file, indent=4)
    #     return cls(id, dict_of_attributes['name'], dict_of_attributes['date'],
    #                dict_of_attributes['number_of_tickets'], dict_of_attributes['price'])

    def __str__(self):
        return f'{self.name}\n' \
                   f'   ID: {self.__id_ticket}\n' \
                   f'   Date: {self.date}\n' \
                   f'   Remaining number of tickets: {self.number_of_tickets}\n' \
                   f'   Price: {self.price}'


class AdvanceTicket(Ticket):
    def __init__(self, id, name, date, number_of_tickets, price):
        super().__init__(id, name, date, number_of_tickets, price)
        self.price = self.price * 0.6


class StudentTicket(Ticket):
    def __init__(self, id, name, date, number_of_tickets, price):
        super().__init__(id, name, date, number_of_tickets, price)
        self.price = self.price * 0.5


class LateTicket(Ticket):
    def __init__(self, id, name, date, number_of_tickets, price):
        super().__init__(id, name, date, number_of_tickets, price)
        self.price = self.price * 1.1