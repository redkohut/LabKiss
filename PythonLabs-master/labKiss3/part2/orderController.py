from client_order import Order
from pizzaController import PizzaController
import os, json

class OrderController:
    """
    This class represents a method to get a new order
    """
    def __init__(self):
        self.__load = False
        self.__orders = None

    @property
    def orders(self):
        if not self.__load:
            self.__load_orders()
            self.__load = True
        return self.__orders

    def __load_orders(self):
        if os.path.isfile('orders.json'):
            with open('orders.json', 'r') as f:
                self.__orders = json.load(f, object_hook=OrderController.__decode_order)
        else:
            self.__orders = []

    def order_pizza(self, customer, addons_price, addons):
        orders = self.orders
        pizza = PizzaController.get_pizza_of_the_day()
        price = pizza.price + addons_price
        order = Order(len(orders) + 1, customer, pizza, price, addons)
        orders.append(order)
        with open('orders.json', "w") as f:
            json.dump(orders, f, default=self.__encode_order, indent=4)

    @staticmethod
    def __encode_order(order):
        if isinstance(order, Order):
            order_dict = {"order id": order.order_id,
                          "customer": order.customer_id,
                          "pizza": order.pizza.__class__.__name__,
                          "price": order.price,
                          "addons": order.additional_ingredients
                          }
            return order_dict

    @staticmethod
    def __decode_order(dct):
        if 'order id' in dct:
            pizza = PizzaController.get_pizza_of(dct['pizza'])
            return Order(dct['order id'], dct['customer'], pizza, dct['price'], dct['addons'])
        return dct
