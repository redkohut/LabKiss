# Task 2.
# Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.
import json
import os
import re


class text_processing:
    def __init__(self, ourSentense):
        if not isinstance(ourSentense, str) or ourSentense == '':
            raise TypeError('type(sentense) != str or type equals null string')
        self.sentense = ourSentense

    @property
    def sentense(self):
        return self.__sentense

    @sentense.setter
    def sentense(self, sentense):
        if not isinstance(sentense, str) or sentense == '':
            raise TypeError('type(sentense) != str or this string has null value')
        self.__sentense = sentense


def main():
    print('Please, choose what do you want to do with this program[Enter 1 or 2]:'
          '\n\t1) Use our file\n\t2) Create your own file')
    client_choice = int(input('Enter your choice: '))

    if not isinstance(client_choice, int):
        raise TypeError('Type(your choice) != int. Please, fix this')
    elif client_choice == 1:
        # is our own file, which all text is correct
        print('Ok, thanks!')
        file = open('task2_part2.txt', 'r')
        if not os.path.exists(file.name):
            raise FileNotFoundError('Your file not found')
    elif client_choice == 2:
        # in this version the client will be able to enter their own input data
        print('Ok, thanks!')
        file = open('task2_2_own.txt', 'w+')
        text = input('What do u want to write?: ')
        # if not isinstance(text, str) or text == '':

        if text != '' and len(text) >= 8 and ' ' in text:
            print('All good')
        else:
            raise ValueError('Please, ')



    else:
        raise ValueError('Sorry, but your input is not correct. Must be 1 or 2!')

    print('Your choice is ', client_choice)


if __name__ == '__main__':
    main()