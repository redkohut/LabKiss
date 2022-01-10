import menu_button
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from Group import Group
from Student import Student


isFirst = True


class Task2Part2t3:
    """
    -----------------------------------------------------
    This class represents the lab2_2_3 with a graphical
    interface using the tkinter module
    -----------------------------------------------------
    """
    ti_01 = None
    ti_02 = None
    tv_01 = None

    def __init__(self, root):
        """Constructor"""
        self.input_index = None
        self.label_record = None
        self.input_eng = None
        self.input_math = None
        self.input_gym = None
        self.input_surname = None
        self.label_math = None
        self.label_eng = None
        self.label_gym = None
        self.label_surname = None
        self.label_name = None
        self.input_add_frame = None
        self.label_ti01_top5 = None
        self.label_ti02_top5 = None
        self.input_name = None
        self.label_tv01 = None
        self.label_ti02 = None
        self.label_ti01 = None
        self.bar_button = None
        self.tab_tv_01 = None
        self.tab_ti_01 = None
        self.tab_ti_02 = None
        self.list_ti_01 = None
        self.list_ti_02 = None
        self.list_tv_01 = None
        self.root = root
        self.__task = 'The class GROUP contains a sequence of instances of the class STUDENT. \n' \
                      'The class STUDENT contains the student`s name, surname, record book \n' \
                      'number and grades. Determine the required attributes-data and attributes-methods\n' \
                      ' in classes GROUP and STUDENT. Find the average score of each student. \n' \
                      'Output to the standard output stream the five students with the highest \n' \
                      'average score. Assume that there can be no more than 20 students in a group, \n ' \
                      'as well as students with the same name and surname.'
        self.list_students = Label(self.root, text=self.__task, fg='#000000', bg='#12c4c0', font=('Comic Sans MS', 15))

        self.f1 = Frame(self.root, width=900, height=600, bg='#262626')
        self.label1 = Label(self.root, text='Laba 2 Part2_3', fg='#12c4c0', bg='#262626', font=('Comic Sans MS', 20))
        self.label2 = Label(self.root, text=self.__task, fg='#000000', bg='#12c4c0', font=('Comic Sans MS', 15))

        self.notebook = ttk.Notebook(self.root)

        self.label1.place(x=55, y=2)
        self.label2.place(x=55, y=40)

        self.button_open_tabs = Button(text='START', font=('Comic Sans MS', 15),
                                       width=22,
                                       height=2,
                                       fg='white',
                                       border=0,
                                       bg='#12c4c0',
                                       activeforeground='#0f9d9a',
                                       activebackground='#12c4c0',
                                       command=self.start_app)
        self.button_open_tabs.place(x=300, y=260)

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

    def open_bar(self):
        """The function that opens the menu_button"""
        self.bar_button = menu_button.MenuButton(self.root)

    def start_app(self):
        """The main function which starts the app and rules processes it"""
        self.label2.destroy()
        self.button_open_tabs.destroy()

        self.tab_ti_01 = Frame(self.notebook)
        self.tab_ti_02 = Frame(self.notebook)
        self.tab_tv_01 = Frame(self.notebook)
        # create tabs
        self.notebook.add(self.tab_ti_02, text='TI-02')
        self.notebook.add(self.tab_ti_01, text='TI-01')
        self.notebook.add(self.tab_tv_01, text='TB-01')
        self.notebook.place(x=30, y=50)
        # set lists of students
        self.ti_02 = None
        self.ti_01 = None
        self.tv_01 = None
        self.set_student_ti02()
        self.set_student_ti01()
        self.set_student_tv01()

        self.label_ti01 = Label(self.tab_ti_01,
                                text=str(self.ti_01),
                                height=22, width=104,
                                fg='#000000',
                                bg='#12c4c0',
                                font=('Comic Sans MS', 10))
        self.label_ti02 = Label(self.tab_ti_02,
                                text=str(self.ti_02),
                                height=22, width=104,
                                fg='#000000',
                                bg='#12c4c0',
                                font=('Comic Sans MS', 10))
        self.label_tv01 = Label(self.tab_tv_01,
                                text=str(self.tv_01),
                                height=22, width=104,
                                fg='#000000',
                                bg='#12c4c0',
                                font=('Comic Sans MS', 10))
        # pack
        self.label_ti01.pack()
        self.label_ti02.pack()
        self.label_tv01.pack()
        # Buttons_create
        Button(self.root,
               text='Add student',
               font=('Comic Sans MS', 15),
               width=15,
               height=2,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=self.add_student).place(x=100, y=480)
        Button(self.root,
               text='Delete',
               font=('Comic Sans MS', 15),
               width=15,
               height=2,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=self.delete_student).place(x=300, y=480)
        Button(self.root,
               text='TOP 5',
               font=('Comic Sans MS', 15),
               width=15,
               height=2,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=self.top_five).place(x=500, y=480)

    def top_five(self):
        """The function which return for user the label with top 5 students"""
        global isFirst
        scene = self.notebook.index('current')

        if isFirst:
            if scene == 0:
                list = self.ti_02.top_five_students()
                self.label_ti02.destroy()
                self.label_ti02_top5 = Label(self.tab_ti_02,
                                             text=list,
                                             height=22,
                                             width=104,
                                             fg='#000000',
                                             bg='#12c4c0',
                                             font=('Comic Sans MS', 10))
                self.label_ti02_top5.pack()
                isFirst = False
            elif scene == 1:
                list = self.ti_01.top_five_students()
                self.label_ti01.destroy()
                self.label_ti01_top5 = Label(self.tab_ti_01,
                                             text=list,
                                             height=22,
                                             width=104,
                                             fg='#000000',
                                             bg='#12c4c0',
                                             font=('Comic Sans MS', 10))
                self.label_ti01_top5.pack()
                isFirst = False
            elif scene == 2:
                list = self.tv_01.top_five_students()
                self.label_tv01.destroy()
                self.label_tv01_top5 = Label(self.tab_tv_01,
                                             text=list,
                                             height=22,
                                             width=104,
                                             fg='#000000',
                                             bg='#12c4c0',
                                             font=('Comic Sans MS', 10))
                self.label_tv01_top5.pack()
                isFirst = False

    def delete_student(self):
        """This function deletes the student from group"""
        global isFirst
        isFirst = True
        self.input_add_frame = Frame(self.root, width=843, height=540, bg='#323232')
        self.label_name = Label(self.input_add_frame,
                                text='Enter name', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.label_surname = Label(self.input_add_frame,
                                   text='Enter surname', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.label_gym = Label(self.input_add_frame,
                               text='Gym', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.label_eng = Label(self.input_add_frame,
                               text='English', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.label_math = Label(self.input_add_frame,
                                text='Math', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.input_add_frame.place(x=30.3, y=36)
        self.label_name.place(x=52, y=20)
        self.label_surname.place(x=52, y=140)
        self.label_eng.place(x=52, y=260)
        self.label_math.place(x=260, y=260)
        self.label_gym.place(x=480, y=260)

        self.input_name = Entry(self.input_add_frame, width=40, border=0, fg='#d16000', font=('Comic Sans MS', 16))
        self.input_surname = Entry(self.input_add_frame, width=40, border=0, fg='#d16000', font=('Comic Sans MS', 16))
        self.input_gym = Entry(self.input_add_frame, width=7, border=0, fg='#d16000', font=('Comic Sans MS', 16))
        self.input_math = Entry(self.input_add_frame, width=7, border=0, fg='#d16000', font=('Comic Sans MS', 16))
        self.input_eng = Entry(self.input_add_frame, width=7, border=0, fg='#d16000', font=('Comic Sans MS', 16))

        self.input_name.place(x=45, y=60)
        self.input_surname.place(x=45, y=180)
        self.input_eng.place(x=45, y=300)
        self.input_math.place(x=250, y=300)
        self.input_gym.place(x=470, y=300)

        Button(self.input_add_frame, text='OK', font=('Comic Sans MS', 15),
               width=15,
               height=1,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=self.back_to_lists_from_del).place(x=345, y=480)

    def back_to_lists_from_del(self):
        """This function make access to visiting previously window"""
        name = self.input_name.get()
        surname = self.input_surname.get()
        math = int(self.input_math.get())
        gym = int(self.input_gym.get())
        eng = int(self.input_eng.get())

        try:
            student = Student(name, surname, {'мат': math, 'англ': eng, 'фп': gym})
            self.ti_02.delete(student)
        except Exception as e:
            print(e)

        self.label_ti02.destroy()
        self.label_ti02 = Label(self.tab_ti_02, text=str(self.ti_02), height=22, width=104, fg='#000000',
                                bg='#12c4c0', font=('Comic Sans MS', 10))
        self.label_ti02.pack()
        self.input_add_frame.destroy()

    def add_student(self):
        """This function adds the student to group"""
        global isFirst
        isFirst = True
        self.input_add_frame = Frame(self.root, width=843, height=540, bg='#323232')
        self.label_name = Label(self.input_add_frame,
                                text='Enter name', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.label_surname = Label(self.input_add_frame,
                                   text='Enter surname', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.label_record = Label(self.input_add_frame,
                                  text='Enter record', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.label_gym = Label(self.input_add_frame,
                               text='Gym', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.label_eng = Label(self.input_add_frame,
                               text='English', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.label_math = Label(self.input_add_frame,
                                text='Math', fg='white', bg='#323232', font=('Comic Sans MS', 20))
        self.input_add_frame.place(x=30.3, y=36)
        self.label_name.place(x=52, y=20)
        self.label_surname.place(x=52, y=140)
        self.label_record.place(x=52, y=260)
        self.label_eng.place(x=52, y=360)
        self.label_math.place(x=260, y=360)
        self.label_gym.place(x=480, y=360)

        self.input_name = Entry(self.input_add_frame, width=40, border=0, fg='#d16000', font=('Comic Sans MS', 16))
        self.input_surname = Entry(self.input_add_frame, width=40, border=0, fg='#d16000', font=('Comic Sans MS', 16))
        self.input_index = Entry(self.input_add_frame, width=40, border=0, fg='#d16000', font=('Comic Sans MS', 16))
        self.input_gym = Entry(self.input_add_frame, width=7, border=0, fg='#d16000', font=('Comic Sans MS', 16))
        self.input_math = Entry(self.input_add_frame, width=7, border=0, fg='#d16000', font=('Comic Sans MS', 16))
        self.input_eng = Entry(self.input_add_frame, width=7, border=0, fg='#d16000', font=('Comic Sans MS', 16))

        self.input_name.place(x=45, y=60)
        self.input_surname.place(x=45, y=180)
        self.input_index.place(x=45, y=300)
        self.input_eng.place(x=45, y=420)
        self.input_math.place(x=250, y=420)
        self.input_gym.place(x=470, y=420)

        Button(self.input_add_frame, text='OK', font=('Comic Sans MS', 15),
               width=15,
               height=1,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=self.back_to_lists_from_add).place(x=345, y=480)

    def set_student_tv01(self):
        """This function initializes the group TV-01"""
        try:
            student1 = Student('Орест', 'Тойвович', {'мат': 100, 'англ': 85, 'фп': 90})
            student2 = Student('Ксюша', 'Бездоганна', {'мат': 99, 'англ': 99, 'фп': 99})
            student3 = Student('Санчоус', 'Спільний', {'мат': 100, 'англ': 90, 'фп': 80})
            student4 = Student('Остап', 'Ковальський', {'мат': 100, 'англ': 100, 'фп': 80})
            student5 = Student('Ілля', 'Рудий', {'мат': 85, 'англ': 90, 'фп': 100})
            student6 = Student('Євгенія', 'Бороденко', {'мат': 100, 'англ': 85, 'фп': 100})
            student7 = Student('Анна', 'Марієнко', {'мат': 90, 'англ': 100, 'фп': 90})
            student8 = Student('Данил', 'Креніда', {'мат': 70, 'англ': 90, 'фп': 90})
            student9 = Student('Серж', 'Свійвович', {'мат': 100, 'англ': 70, 'фп': 70})
            student10 = Student('Сніжана', 'Кук', {'мат': 100, 'англ': 100, 'фп': 100})
            student11 = Student('Михайло', 'Дагойда', {'мат': 100, 'англ': 100, 'фп': 100})
            student12 = Student('Аміна', 'Шимко', {'мат': 100, 'англ': 60, 'фп': 70})
            self.tv_01 = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9,
                               student10, student11, student12)

        except Exception as e:
            print(e)

    def set_student_ti01(self):
        """This function initializes the group TI-01"""
        try:
            student1 = Student('Саня', 'Ткаченко', {'мат': 100, 'англ': 85, 'фп': 90})
            student2 = Student('Даня', 'Петраченко', {'мат': 99, 'англ': 99, 'фп': 99})
            student3 = Student('Максим', 'Гарманенко', {'мат': 100, 'англ': 90, 'фп': 80})
            student4 = Student('Олекса', 'Гарбаж', {'мат': 100, 'англ': 100, 'фп': 80})
            student5 = Student('Степан', 'Зінченко', {'мат': 85, 'англ': 90, 'фп': 100})
            student6 = Student('Саня', 'Санович', {'мат': 100, 'англ': 85, 'фп': 100})
            student7 = Student('Тіна', 'Костаренко', {'мат': 90, 'англ': 100, 'фп': 90})
            student8 = Student('Катерина', 'Свербигова', {'мат': 70, 'англ': 90, 'фп': 90})
            student9 = Student('Сергій', 'Рвихвіст', {'мат': 100, 'англ': 70, 'фп': 70})
            student10 = Student('Стьопа', 'Костел', {'мат': 100, 'англ': 100, 'фп': 100})
            student11 = Student('Михайло', 'Лагідний', {'мат': 100, 'англ': 100, 'фп': 100})
            student12 = Student('Ілля', 'Саймоненко', {'мат': 100, 'англ': 60, 'фп': 70})

            self.ti_01 = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9,
                               student10, student11, student12)
        except Exception as e:
            print(e)

    def set_student_ti02(self):
        """This function initializes the group TI-02"""
        try:
            student1 = Student('Іван', 'Власюк', {'мат': 100, 'англ': 85, 'фп': 90})
            student2 = Student('Ліза', 'Гончарова', {'мат': 99, 'англ': 99, 'фп': 99})
            student3 = Student('Максим', 'Груздов', {'мат': 100, 'англ': 90, 'фп': 80})
            student4 = Student('Олексій', 'Дудкін', {'мат': 100, 'англ': 100, 'фп': 80})
            student5 = Student('Олексій', 'Занченко', {'мат': 85, 'англ': 90, 'фп': 100})
            student6 = Student('Євгеній', 'Захарчук', {'мат': 100, 'англ': 85, 'фп': 100})
            student7 = Student('Анна', 'Котова', {'мат': 90, 'англ': 100, 'фп': 90})
            student8 = Student('Дарія', 'Кравченко', {'мат': 70, 'англ': 90, 'фп': 90})
            student9 = Student('Сергій', 'Кубрак', {'мат': 100, 'англ': 70, 'фп': 70})
            student10 = Student('Тетяна', 'Кушнірук', {'мат': 100, 'англ': 100, 'фп': 100})
            student11 = Student('Михайло', 'Лагойда', {'мат': 100, 'англ': 100, 'фп': 100})
            student12 = Student('Святослав', 'Луговий', {'мат': 100, 'англ': 60, 'фп': 70})

            self.ti_02 = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9,
                               student10, student11, student12)
        except Exception as e:
            print(e)

    def back_to_lists_from_add(self):
        name = self.input_name.get()
        surname = self.input_surname.get()
        math = int(self.input_math.get())
        gym = int(self.input_gym.get())
        eng = int(self.input_eng.get())

        try:
            student = Student(name, surname, {'мат': math, 'англ': eng, 'фп': gym})
            self.ti_02.add(student)
        except Exception as e:
            print(e)

        self.label_ti02.destroy()
        self.label_ti02 = Label(self.tab_ti_02, text=str(self.ti_02), height=22, width=104, fg='#000000',
                                bg='#12c4c0', font=('Comic Sans MS', 10))
        self.label_ti02.pack()
        self.input_add_frame.destroy()

