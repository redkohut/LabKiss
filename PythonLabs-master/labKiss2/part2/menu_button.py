from tkinter import *
from PIL import ImageTk, Image
import task2_ui
import task3_ui
import laba3_1_ui


class MenuButton:
    """
    ----------------------------------------------------
    This class represents the main bar of buttons
    with a graphical interface using the tkinter module
    ----------------------------------------------------
    """

    def __init__(self, root):
        self.lab3_part1_1 = None
        self.lab2_part2_3 = None
        self.lab2_part2_2 = None
        self.root = root
        self.f1 = Frame(root, width=300, height=600, bg='#12c4c0')
        self.f1.place(x=0, y=0)
        self.button_parent = None
        self.button(0, 40, 'LABA 2  Part2 Task2', '#0f9d9a', '#12c4c0', self.go_lab2_part2_2)
        self.button(0, 70, 'LABA 2  Part2 Task3', '#0f9d9a', '#12c4c0', self.go_lab2_part2_3)
        self.button(0, 100, 'LABA 2  Part2 Tass4', '#0f9d9a', '#12c4c0', None)
        self.button(0, 130, 'LABA 3  Part1 Task1', '#0f9d9a', '#12c4c0', self.go_lab3_part1_1)
        self.button(0, 160, 'LABA 3  Part1 Task2', '#0f9d9a', '#12c4c0', None)
        self.button(0, 190, 'LABA 3  Part2 Task1', '#0f9d9a', '#12c4c0', None)
        self.button(0, 220, 'LABA 3  Part2 Task2', '#0f9d9a', '#12c4c0', None)
        self.button(0, 250, 'LABA 3  Part2 Task3', '#0f9d9a', '#12c4c0', None)
        self.button(0, 280, 'LABA 3  Part2 Task4', '#0f9d9a', '#12c4c0', None)
        self.button(0, 310, 'LABA 4  Part1 Task1', '#0f9d9a', '#12c4c0', None)
        self.button(0, 340, 'LABA 4  Part1 Task2', '#0f9d9a', '#12c4c0', None)
        self.button(0, 370, 'LABA 4  Part2 Task1', '#0f9d9a', '#12c4c0', None)
        self.button(0, 400, 'LABA 4  Part2 Task2', '#0f9d9a', '#12c4c0', None)
        self.button(0, 430, 'LABA 4  Part2 Task3', '#0f9d9a', '#12c4c0', None)
        self.button(0, 460, 'LABA 4  Part2 Task4', '#0f9d9a', '#12c4c0', None)

        self.img2 = ImageTk.PhotoImage(Image.open('close.png'))
        self.close_button = Button(self.f1,
                                   image=self.img2,
                                   border=0, command=self.delete_bar,
                                   bg='#12c4c0',
                                   activebackground='#12c4c0')
        self.close_button.place(x=5, y=10)

    def button(self, x, y, text, bcolor, fcolor, cmd):
        """This feature creates all the buttons with advanced features"""
        def on_mouse_enter(e):
            button_parent['background'] = bcolor
            button_parent['foreground'] = '#262626'

        def on_mouse_exit(e):
            button_parent['background'] = fcolor
            button_parent['foreground'] = '#262626'
        button_parent = Button(self.f1, text=text, width=42, height=2,
                               fg='#262626', border=0, bg=fcolor,
                               activeforeground='#262626',  activebackground=bcolor, command=cmd)
        button_parent.bind('<Enter>', on_mouse_enter)
        button_parent.bind('<Leave>', on_mouse_exit)

        button_parent.place(x=x, y=y)

    def go_lab2_part2_2(self):
        """This function creates a lab2_2_3 class object"""
        self.lab2_part2_2 = task2_ui.Task2Part2t2(self.root)

    def go_lab2_part2_3(self):
        """This function creates a lab2_2_4 class object"""
        self.lab2_part2_3 = task3_ui.Task2Part2t3(self.root)

    def go_lab3_part1_1(self):
        """This function creates a lab3_1 class object"""
        self.lab3_part1_1 = laba3_1_ui.Task3Task1(self.root)

    def delete_bar(self):
        """This function destroys the frame"""
        self.f1.destroy()
