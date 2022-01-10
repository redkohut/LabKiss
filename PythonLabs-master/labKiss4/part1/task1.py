from rational_controller import Rational


def main():
    rational1 = Rational(1, 2)
    rational2 = Rational(3, 4)

    print(rational1 + rational2)
    print(rational1 - rational2)
    print(rational1 / rational2)
    print(rational1 * rational2)

    rational1 += rational2
    print(rational1)

    rational1 -= rational2
    print(rational1)

    rational1 *= rational2
    print(rational1)

    rational1 /= rational2
    print(rational1)


if __name__ == '__main__':
    main()
