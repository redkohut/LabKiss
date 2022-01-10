import os
import re
import menu_button
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


class Task2Part2t2:
    """
    -----------------------------------------------------
    This class represents the lab2_2_2 with a graphical
    interface using the tkinter module
    -----------------------------------------------------
    """
    def __init__(self, root):
        """constructor"""
        self.label_output = None
        self.label_result = None
        self.contents = None
        self.text_label = None
        self.bar_button = None
        self.root = root
        self.__task = 'Create a class that performs statistical processing of a text file\n' \
                      ' - counting characters, words, sentences, etc. Determine the required \n' \
                      'attributes-data and attributes-methods in class for working with the text file.'
        self.f1 = Frame(self.root, width=900, height=600, bg='#262626')
        self.label1 = Label(self.root, text='Laba 2 Part2_2', fg='#12c4c0', bg='#262626', font=('Comic Sans MS', 20))
        self.label2 = Label(self.root, text=self.__task, fg='#000000', bg='#12c4c0', font=('Comic Sans MS', 15))
        self.label1.place(x=55, y=2)
        self.label2.place(x=55, y=40)
        self.f1.place(x=0, y=0)

        self.problem_label = None
        self.problem_is_active = False
        self.file_text = None

        self.img1 = ImageTk.PhotoImage(Image.open("open.png"))
        self.open_buttons = Button(self.root,
                                   image=self.img1,
                                   command=self.open_bar,
                                   border=0,
                                   bg='#262626',
                                   activebackground='#262626')
        self.open_buttons.place(x=5, y=10)
        self.button_openfile1 = Button(text='Open file',
                                       font=('Comic Sans MS', 15),
                                       width=22,
                                       height=2,
                                       fg='white',
                                       border=0,
                                       bg='#12c4c0',
                                       activeforeground='#0f9d9a',
                                       activebackground='#12c4c0',
                                       command=self.open_file)
        self.button_openfile1.place(x=300, y=180)

    def open_bar(self):
        """The function that opens the menu_button"""
        self.bar_button = menu_button.MenuButton(self.root)

    def open_file(self):
        """The main function which opens the file and rules processes it"""
        if self.problem_is_active:
            self.problem_label.destroy()
        filepath = filedialog.askopenfilename(filetypes=(('text files', '*.txt'), ('all files', '*.*')))
        if not os.path.exists(filepath):
            self.problem_label = Label(self.root,
                                       text='No such file or directory. Try open file again',
                                       fg='#FF0000',
                                       bg='#262626',
                                       font=('Comic Sans MS', 20))
            self.problem_is_active = True
            self.problem_label.place(x=100, y=130)
            raise FileNotFoundError('Sorry, but no such file or directory')

        self.file_text = open(str(filepath), 'r')
        if len(self.file_text.read()) == 0:
            self.problem_label = Label(self.root, text='Sorry, but your text is null',
                                       fg='#FF0000',
                                       bg='#262626',
                                       font=('Comic Sans MS', 20))
            self.problem_is_active = True
            self.problem_label.place(x=100, y=130)
            raise ValueError('Sorry, but your text is null')

        self.button_openfile1.destroy()

        self.text_label = Label(self.root,
                                text=str(self.file_text.read()),
                                fg='white',
                                bg='#262626',
                                font=('Arial', 20))
        self.text_label.place(x=120, y=430)

        with open(str(filepath)) as f:
            self.contents = f.read()

        work_with_file1 = BackendTask222(self.contents)

        self.label_output = Label(self.root,
                                  text=(f'Number of words in text file: {work_with_file1.words}' +
                                        f'\nNumber of lines in text file: {work_with_file1.lines}') +
                                        f'\nNumber of characters in text file: {work_with_file1.characters}' +
                                        f'\nNumber of sentences in text file: {work_with_file1.sentences}',
                                  fg='white',
                                  bg='#262626',
                                  font=('Arial', 20))
        self.label_output.place(x=180, y=250)
        self.file_text.close()


class BackendTask222:
    """This class represents a backend of main class"""
    def __init__(self, text):
        if len(text) == 0:
            raise ValueError('Sorry, but your text is null')
        self.__text = text
        self.__characters = len(text)
        self.__words = len(text.split())
        self.__sentences = len(re.split(r'[.!?]+', text))-1
        self.__lines = len(re.split(r'[\n]+', text))

    @property
    def text(self):
        return str(self.__text)

    @text.setter
    def text(self, text):
        if not isinstance(text, str) or text == '':
            raise TypeError('type(sentense) != str or this string has null value')
        self.__text = text

    @property
    def characters(self):
        return str(self.__characters)

    @property
    def words(self):
        return str(self.__words)

    @property
    def sentences(self):
        return str(self.__sentences)

    @property
    def lines(self):
        return str(self.__lines)
