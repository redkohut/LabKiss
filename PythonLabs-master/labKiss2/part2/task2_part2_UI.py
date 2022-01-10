from tkinter import *
from PIL import ImageTk, Image
from menu_button import MenuButton


class MainScene:
    """
    This class represents the main menu with a graphical
    interface using the tkinter module
    """

    def __init__(self, width, height, title='LabKiss', resizable=(False, False)):
        self.bar_button = None
        self.root = Tk()
        self.root.wm_iconbitmap('icon.ico')
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+200')
        self.root.resizable(resizable[0], resizable[1])
        self.root.configure(bg='#262626')
        # Label1
        self.label1 = Label(self.root, text='Labkiss', fg='white', bg='#262626', font=('Comic Sans MS', 90))
        self.label1.place(x=200, y=40)
        # Label2
        self.label2 = Label(self.root, text='by zhenia TI-02', fg='white', bg='#262626', font=('Comic Sans MS', 50))
        self.label2.place(x=200, y=200)
        # create button
        self.img1 = ImageTk.PhotoImage(Image.open("open.png"))
        self.open_buttons = Button(self.root, image=self.img1,
                                   command=self.open_bar,
                                   border=0, bg='#262626',
                                   activebackground='#262626')
        self.open_buttons.place(x=5, y=10)

    def run(self):
        """Starting"""
        self.root.mainloop()

    def open_bar(self):
        """Create bar of all buttons(labs)"""
        self.bar_button = MenuButton(self.root)


if __name__ == '__main__':
    test = MainScene(900, 600)
    test.run()
