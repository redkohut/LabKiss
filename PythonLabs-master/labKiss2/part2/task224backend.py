from product import ProductInfo, PriceTree


def create_tree():
    binary_tree = PriceTree()
    binary_tree.insert(ProductInfo(1, 123))
    binary_tree.insert(ProductInfo(3, 1223))
    binary_tree.insert(ProductInfo(2, 623))
    binary_tree.insert(ProductInfo(9, 31))
    binary_tree.insert(ProductInfo(5, 29233))
    # print(binary_tree)
    # binary_tree.delete_node(1)
    # print(binary_tree)
    # binary_tree.delete_node(5)
    # print(binary_tree)
    return binary_tree


def main():
    try:
        tree = create_tree()
        input_args = [int(x) for x in input('Enter product code and number of products separated by space: ').split()]
        if len(input_args) != 2:
            raise Exception('Wrong input')
        price = tree.find(input_args[0])
        if price is None:
            print('There are no such product in the tree')
        else:
            print(f'Cost of {input_args[1]} product(s) with code {input_args[0]} = {price * input_args[1]}')
    except Exception as e:
        print(e)


main()
