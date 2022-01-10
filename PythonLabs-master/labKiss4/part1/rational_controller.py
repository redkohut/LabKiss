from math import gcd


class Rational:
    """
    --------------------------------------------------------------------------------
    This class represents a rational number for performing arithmetic with fractions
    Parameters
    --------------------------------------------------------------------------------
    numerator, denominator : 'int'
    """

    def __init__(self, numerator=0, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError('The values must be type float')
        if not denominator:
            raise ZeroDivisionError('The denominator cannot be equals 0')
        self.numerator = numerator
        self.denominator = denominator
        self.__gcd()

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

    def __gcd(self):
        if self.numerator != 0:
            own_divisor = gcd(self.numerator, self.denominator)
            self.numerator //= own_divisor
            self.denominator //= own_divisor
            if self.numerator < 0 and self.denominator < 0:
                self.numerator *= -1
                self.denominator *= -1

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('The type must be Rational')
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('The type must be Rational')
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('The type must be Rational')
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('The type must be Rational')
        return Rational(self.numerator * other.denominator, other.numerator * self.denominator)

    def __iadd__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('The type must be Rational')
        self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        self.denominator = self.denominator * self.numerator
        self.__gcd()
        return self

    def __isub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('The type must be Rational')
        self.numerator = self.numerator * other.denominator - self.denominator * other.numerator
        self.denominator = self.denominator * self.numerator
        self.__gcd()
        return self

    def __imul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('The type must be Rational')
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        self.__gcd()
        return self

    def __idiv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('The type must be Rational')
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        self.__gcd()
        return self

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

