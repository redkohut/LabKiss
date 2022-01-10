from math import gcd


class Rational:
    """
    This class represents a rational number for performing arithmetic with fractions
    Parameters
    --------------------------------------------------------------------------------
    numerator, denominator : type == 'int'
        fraction parts
    """
    def __init__(self, numerator=0, denominator=0):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError('The values must be type float')
        if not denominator:
            raise ZeroDivisionError('The denominator cannot be equals 0')
        common_divisor = gcd(numerator, denominator)
        self.__numerator = numerator // common_divisor
        self.__denominator = denominator // common_divisor

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, number):
        if not isinstance(number, int):
            raise TypeError('The type of numerator must be int')
        self.__numerator = number

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, number):
        if not isinstance(number, int):
            raise TypeError('The type of denominator must be int')
        if number == 0:
            raise ZeroDivisionError('The denominator cannot be equals zero')
        self.__denominator = number

    @property
    def get_float(self):
        return self.__numerator / self.__denominator

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'


if __name__ == '__main__':
    try:
        rational1 = Rational()
        print(rational1)
        print(rational1.get_float)

        rational2 = Rational(10, 20)
        print(rational2)
        print(rational2.get_float)

        rational3 = Rational(0, 10)
        print(rational3)
        print(rational3.get_float)
    except Exception as e:
        print(e)
