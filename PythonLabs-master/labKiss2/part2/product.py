class ProductInfo:
    """
    This class represents a binary tree node with Product's
    code and price
    """
    def __init__(self, code, price):
        self.__left = None
        self.__right = None
        self.__code = code
        self.__set_code(code)
        self.__price = price

    @property
    def code(self):
        return self.__code

    def __set_code(self, code):
        if not isinstance(self, code):
            raise TypeError('The type of code should be a integer')
        if code <= 0:
            raise ValueError('The value of code should be a greater than 0')
        self.__code = code

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('The type of price should be a int or float')
        if price <= 0:
            raise ValueError('The value of price should not be less than 0')
        self.__price = price

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, product_info):
        if not isinstance(product_info, ProductInfo):
            raise TypeError('The type of left should be a ProductInfo')
        if product_info:
            raise ValueError('The value of left equals null')
        self.__left = product_info

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, product_info):
        if not isinstance(product_info, ProductInfo):
            raise TypeError('The type of left should be a ProductInfo')
        if product_info:
            raise ValueError('The value of left equals null')
        self.__right = product_info


class PriceTree:
    """
    This class represents a binary tree of products nodes
    """
    def __init__(self):
        self.__root = None

    def insert(self, node):
        if not isinstance(node, ProductInfo):
            raise TypeError('The type of node should be a ProductInfo')
        if self.__root:
            self.__insert(self.__root, node)
        else:
            self.__root = node

    def __insert(self, root, node):
        if node.code < root.code:
            if root.left is None:
                root.left = node
            else:
                self.__insert(root.left, node)
        elif node.code > root.code:
            if root.right is None:
                root.right = node
            else:
                self.__insert(root.right, node)
        else:
            root.price = node.price

    def find(self, code):
        if not isinstance(code, int):
            raise TypeError('The type of code should be integer')
        return self.__find(self.__root, code)

    def __find(self, root, code):
        if root:
            if code < root.code:
                return self.__find(root.left, code)
            elif code > root.code:
                return self.__find(root.right, code)
            else:
                return root.price
        return None

    def delete_node(self, code):
        if not isinstance(code, int):
            raise TypeError('The type  of code should be a integer')
        self.__root = self.__delete_node(self.__root, code)

    def __delete_node(self, root, code):
        if code == root.code:
            if root.right and root.left:
                [parent_of_successor, successor] = self.__find_min(root, root.right)
                if parent_of_successor.left == successor:
                    parent_of_successor.left = successor.right
                else:
                    parent_of_successor.right = successor.right
                successor.left = root.left
                successor.right = root.right
                return successor
            else:
                if root.left:
                    return root.left
                else:
                    return root.right
        else:
            if code < root.code and root.left:
                root.left = self.__delete_node(root.left, code)
            elif root.right:
                root.right = self.__delete_node(root.right, code)
        return root

    def __find_min(self, parent, right_node):
        if right_node.left:
            return self.__find_min(right_node, right_node.left)
        else:
            return [parent, right_node]

    def __str__(self):
        tree_list = list()
        self.__make_Str(self.__root, tree_list)
        return ' '.join(map(lambda x: f'({x.code}, {x.price}', tree_list))

    def __make_str(self, node, tree_list):
        if node.left:
            self.__make_str(node.left, tree_list)
        tree_list.append(node)
        if node.right:
            self.__make_str(node.right, tree_list)