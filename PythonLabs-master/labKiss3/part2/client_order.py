from typesPizza import Pizza


class Order:
    """
    This class represents a simple process ordering
    """
    def __init__(self, order_id, customer_id, pizza, price, additional_ingredients=None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.pizza = pizza
        self.price = price
        self.additional_ingredients = additional_ingredients

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, id):
        if not isinstance(id, int):
            raise TypeError('The type of orderID should be integer')
        self.__order_id = id

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, id):
        if not isinstance(id, int):
            raise TypeError('The type of orderID should be integer')
        self.__customer_id = id

    @property
    def pizza(self):
        return self.__pizza

    @pizza.setter
    def pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError('The type of pizza should be a Pizza')
        self.__pizza = pizza

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('The type of price should be a itn or float')
        if price <= 0:
            raise ValueError('The value of price must be a greater than 0')
        self.__price = price

    @property
    def additional_ingredients(self):
        return self.__additional_ingredients

    @additional_ingredients.setter
    def additional_ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise TypeError('The type of ingredients should be a list')
        if any(not isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError('The type of all ingredients should be a string')
        self.__additional_ingredients = ingredients

    def __str__(self):
        return f'\tOrder of client:\n' \
               f'OrderID: {self.order_id}\n' \
               f'ClientID: {self.customer_id}\n' \
               f'Additional ingredients: {self.additional_ingredients}\n' \
               f'Total price: {self.price}'