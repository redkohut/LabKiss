import os
import timeit
from random import randint


def test_readlines():
    s = 0
    with open('digits.txt', 'r') as f:
        lines = f.readlines(52428800)
        for line in lines:
            if line.strip().isdigit():
                s += int(line.strip())


def test_for_line_in_f():
    s = 0
    with open('digits.txt', 'r') as f:
        for line in f:
            if line.strip().isdigit():
                s += int(line.strip())


def test_generator():
    s = sum((int(row.strip()) for row in open('digits.txt') if row.strip().isdigit()))


def main():
    # with open('digits.txt', 'a') as f:
    #     while os.path.getsize("digits.txt") < 52428800:
    #         f.write(str(randint(0, 1000000)) + '\n')
    print(timeit.timeit(test_readlines, number=1))
    print(timeit.timeit(test_for_line_in_f, number=1))
    print(timeit.timeit(test_generator, number=1))


main()
