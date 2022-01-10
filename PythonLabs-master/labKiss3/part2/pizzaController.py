from typesPizza import MondayPizza, TuesdayPizza, WednesdayPizza
from typesPizza import ThursdayPizza, FridayPizza, SaturdayPizza, SundayPizza
from typesPizza import UsuallyPizza1, UsuallyPizza2
from datetime import datetime as dt


class PizzaController:
    ingredients = {'pineapple': 25,
                   'cheese': 30,
                   'tomatoes': 20,
                   'onion': 18,
                   'fried chicken': 40
                   }
    __pizza = {'MondayPizza': MondayPizza('Margherita', 300, ['crust', 'tomato sauce', 'mozzarella cheese']),
               'TuesdayPizza': TuesdayPizza('Hawaiian', 320, ['tomato sauce', 'cheese', 'ham', 'pineapple']),
               'WednesdayPizza': WednesdayPizza('Pepperoni', 310, ['mozzarella cheese', 'bacon', 'tomato sauce']),
               'ThursdayPizza': ThursdayPizza('Meat-Lover’s', 340, ['pepperoni', 'sausage', 'meatballs', 'mushrooms']),
               'FridayPizza': FridayPizza('Cheese', 290, ['mozzarella cheese', 'oregano',  'pizza sauce']),
               'SaturdayPizza': SaturdayPizza('Brasilia', 305, ['mozzarella cheese', 'bacon', 'sweet pepper']),
               'UsuallyPizza1': UsuallyPizza1('Meat', 322, ['beef', 'sausage', 'cheese']),
               'UsuallyPizza2': UsuallyPizza2('BBQ', 335, ['chicken', 'sausage', 'cheese'])
               }


    @staticmethod
    def get_pizza_order(name_of_pizza):
        if name_of_pizza in PizzaController.__pizza:
            return ValueError('Sorry, but [name_of_pizza] not contain in the list')
        return PizzaController.__pizza[name_of_pizza]

    @staticmethod
    def get_pizza_of_the_day():
        now_day = dt.now().strftime("%A")
        for key in PizzaController.__pizza.keys():
            if now_day in key:
                return PizzaController.__pizza[key]


if __name__ == '__main__':
    print(PizzaController.get_pizza_of_the_day())
    print(str(dt.today().isoweekday()))
