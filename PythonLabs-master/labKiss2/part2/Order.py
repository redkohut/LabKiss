from store_classes import Customer, Product


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

