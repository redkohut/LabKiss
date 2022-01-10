class Product:
    """ This class represents a product entity """
    def __init__(self, price=0, description='None', dimensions='None'):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int) and not isinstance(value, int):
            raise TypeError('price(type) != float or int')
        elif value <= 0:
            raise ValueError('price cannot be negative')
        self.__price = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str) or value == '':
            raise TypeError('type(description) != str or value equals null')
        self.__description = value

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, value):
        if not isinstance(value, str) or value == '':
            raise TypeError('type(dimensions) != str or value equals null')
        self.__dimensions = value

    def __str__(self):
        return f'Customer [price = {self.price}, description = {self.description}, dimensions = {self.dimensions}'


class Customer:
    """ This class represents a customer entity """
    def __init__(self, surname='None', name='None', patronymic='None', mobile_phone='0970807396', age=0):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone
        self.age = age

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError('type(surname) != str')
        self.__surname = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('type(name) != str')
        self.__name = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        if not isinstance(value, str):
            raise TypeError('type(patronymic) != str')
        self.__patronymic = value

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        if not isinstance(value, str) or value.find('-') != -1:
            raise TypeError('type(mobile_phone) != str or not correct input')
        elif len(value) != 10:
            raise ValueError('len(number of mobile_phobe) != 10')
        self.__mobile_phone = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('type(age) != int')
        elif value < 0 or value > 110:
            raise ValueError('person cannot be that old ( < 0 or > 110)')
        self.__age = value

    def __str__(self):
        return f'Customer [surname = {self.surname}, name = {self.name}, patronymic = {self.patronymic}, ' \
               f'mobile_phone = {self.mobile_phone}, age = {self.age}]'


class Order:
    """
    This class represents an order entity

    """

    def __init__(self, customer=Customer(), *products):
        self.customer = customer
        self.products = products

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        if any(not isinstance(product, Product) for product in products):
            raise TypeError("Products must be of Product type")
        self.__products = list(products)

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be of Customer type")
        self.__customer = customer

    def get_total_order_value(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        return total_price

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Product must be of Product type")
        self.products.append(product)

    def del_product(self, product):
        self.products.remove(product)

    def __str__(self):
        products_str = ',\n\t'.join(map(str, self.products))
        return f'Order [customer = {self.customer}, products:\n\t{products_str}\n]'
