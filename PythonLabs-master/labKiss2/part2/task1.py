from Order import Order
from store_classes import Customer, Product


def main():
    try:
        phone = Product(1000, 'Iphone 8', '1000x300x100')
        video_card = Product(500, 'Apple', '300, 100, 40')
        customer = Customer('Movchanuk', 'Denchik', 'Olegovich', '0970807396')
        order = Order(customer, phone, video_card)
        print('Total value of order for ' + str(customer.name) + ' = ' + str(order.get_total_order_value()))
        print(video_card)
        print(customer)
        print(order)
        new_product = Product(100, 'something', 'some dimensions')
        order.add_product(new_product)
        print(order)
        copy_of_new_product = Product(100, 'something', 'some dimensions')
        order.del_product(copy_of_new_product)
        print(order)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
