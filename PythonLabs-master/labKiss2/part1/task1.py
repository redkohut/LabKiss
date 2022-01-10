class Rectangle:
    """
    This class represents a rectangle entity
    Parameters
    ----------------------------------------
    length, width : 'float'
    Sides of the rectangle
    """
    def __init__(self, length=1, width=1):
        if width < 0.0 or width > 20.0 or length < 0.0 or width > 20.0:
            raise ValueError('length numbers must be larger than 0.0 and less than 20.0')
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if not isinstance(length, float):
            raise TypeError('type(length) != float, the value must be type float')
        if length < 0.0 or length > 20.0:
            raise ValueError('length number must be larger than 0.0 and less than 20.0')
        else:
            self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError('type(length) != float, the value must be typy integer')
        if width < 0.0 or width > 20.0:
            raise ValueError('length number must be larger than 0.0 and less than 20.0')
        else:
            self.__width = width

    def get_perimetr(self):
        return (self.__width+self.__length)*2

    def get_area(self):
        return self.__length*self.length


def main():
    # try to initialize with error
    temp_rect1 = Rectangle(1.2, 5.6)
    temp_rect2 = Rectangle()
    print('Area: ', temp_rect1.get_area())
    print('Perimeter: ', temp_rect1.get_perimetr())

    try:
        temp_rect2.length = 3.4
        temp_rect2.width = -6.4
        print('Area: ', temp_rect2.get_area())
        print('Perimeter: ', temp_rect2.get_perimetr())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
