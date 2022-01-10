import sys

operation_type = {'add': '+',
                  'sub': '-',
                  'div': '/',
                  'mul': '*'
                  }


def main():
    """This function represents the processing of simple arithmetic operations"""
    if len(sys.argv) != 4 or not sys.argv[2].isdigit() or not sys.argv[3].isdigit():
        raise TypeError('Problems with arguments! Please enter correct')
    elif not sys.argv[1] in operation_type:
        raise ValueError('There is no such type of operation in the program')
    else:
        if not sys.argv[3]:
            raise ZeroDivisionError('You cannot divide by zero')
        else:
            result = str(eval(sys.argv[2] + ' ' + operation_type[sys.argv[1]] + ' ' + sys.argv[3]))
            print('Your result: ' + result)


if __name__ == '__main__':
    main()
