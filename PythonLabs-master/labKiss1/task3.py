sign = '+-'
numbers = '0123456789'


def is_formula(formula) -> bool:
    """This function checks if a formula is correct"""
    if formula and formula[0] in numbers:
        for i in range(len(formula)):
            # 'delete' it until get to not numbers symbol
            if formula[0] in numbers:
                formula = formula[1:]
            else:
                break
        if not formula:
            return True
        if formula[0] in sign:
            return is_formula(formula[1:])
    return False


def main():
    """
    This function represents the input string (our expression)
    and outputs the result of this expression
    """
    user_expression = input('Please, enter your expression: ')
    if is_formula(user_expression):
        print('Your result = (True, ', eval(user_expression), '\b)')
    else:
        print('Your result = (False, None)')


if __name__ == '__main__':
    main()



