class Pizza:
    """
    This class represents a parent class of all types Pizza
    """
    def __init__(self, name, price, adding_ingredient=None):

        self.name = name
        self.price = price
        self.ingredients = adding_ingredient

    # @property
    # def type(self):
    #     return self.__type
    #
    # @type.setter
    # def type(self, type):
    #     if not isinstance(type, str) or type == '':
    #         raise TypeError('The type should be a string')
    #     self.__type = type

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('The type of name should be a string')
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('The type of price should be a int or float')
        if price <= 0:
            raise ValueError('The price must be a greater than zero')
        self.__price = price

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise TypeError('The type of ingredients should be a list')
        if any(not isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError('The type of ingredient should be a string')
        self.__ingredients = ingredients


class MondayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Monday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'


class ThursdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Thursday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'


class WednesdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Wednesday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'


class TuesdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Tuesday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'


class FridayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Friday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'


class SaturdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Saturday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'


class SundayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Sunday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'


class UsuallyPizza1(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Top pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'


class UsuallyPizza2(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Top pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'

