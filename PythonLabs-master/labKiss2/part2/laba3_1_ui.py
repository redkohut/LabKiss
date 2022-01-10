from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import menu_button
import text
from tickets import *
from fpdf import FPDF
from pdf_mail import sendpdf
from event import Event
from datetime import datetime
from tkinter import messagebox

working_email = 'pppython.oop@gmail.com'
password = 'kapustaqwe123zxc'
client_email = 'zhenia.yf@gmail.com'
is_restart = False


class PDF(FPDF):
    """
    This class represent the way to send pdf file to our clients
    But the client must be registered
    """
    __sender_email = 'pppython.oop@gmail.com'
    __password = 'kapustaqwe123zxc'
    __client_email = 'zhenia.yf@gmail.com'
    events = []
    all_ticket = []

    def __init__(self, layout='P', unit='mm', format='A4', tickets=None):
        super().__init__(orientation=layout, unit=unit, format=format)
        self.__type = tickets
        self.add_page()
        self.photo()

    def photo(self):
        """This function creates photo tickets"""
        tickets = self.__type
        print(tickets)
        if not isinstance(tickets, int):
            raise TypeError('The type of tickets must be integer')
        if tickets == 1:
            self.image('regular.png', 10, 8, 25)
            self.set_font('times', 'B', 20)
            self.cell(0, 10, 'Regular Ticket', border=False, ln=1, align='C')
            self.ln(20)
        elif tickets == 2:
            self.image('advance.png', 10, 8, 25)
            self.set_font('times', 'B', 20)
            self.cell(0, 10, 'Advance Ticket', border=False, ln=1, align='C')
            self.ln(20)
        elif tickets == 3:
            self.image('late.png', 10, 8, 25)
            self.set_font('times', 'B', 20)
            self.cell(0, 10, 'Late Ticket', border=False, ln=1, align='C')
            self.ln(20)
        elif tickets == 4:
            self.image('student.png', 10, 8, 25)
            self.set_font('times', 'B', 20)
            self.cell(0, 10, 'Student Ticket', border=False, ln=1, align='C')
            self.ln(20)
        else:
            raise ValueError('The value of tickets should be in the range (1, 4)')


class Task3Task1:
    """
    This class represents a simple GUI app for
    buying a tickets for IT events
    """

    def __init__(self, root):
        self.but5 = None
        self.but4 = None
        self.ticket_imag4 = None
        self.but3 = None
        self.ticket_imag3 = None
        self.but2 = None
        self.ticket_imag2 = None
        self.but1 = None
        self.ticket_imag1 = None
        self.ff1 = None
        self.user_buttons = None
        self.img2 = None
        self.color_frame = None
        self.event_image7 = None
        self.event_image6 = None
        self.event_image5 = None
        self.event_image4 = None
        self.event_image3 = None
        self.event_image2 = None
        self.event_image1 = None
        self.event6 = None
        self.event7 = None
        self.event5 = None
        self.event3 = None
        self.event4 = None
        self.event2 = None
        self.event1 = None
        self.design_frame2 = None
        self.design_frame1 = None
        self.main_label = None
        self.second_frame = None
        self.scrollbar = None
        self.canvas = None
        self.main_frame = None
        self.bar_button = None
        self.root = root
        self.__task = 'Write a program for selling tickets to IT-events. Each ticket has\n'\
                      'a unique number and a price. There are four types of tickets: regular\n'\
                      'ticket, advance ticket (purchased 60 or more days before the event),\n'\
                      'late ticket (purchased fewer than 10 days before the event) and student ticket.\n'\
                      'Additional information:\n'\
                      '-advance ticket - discount 40% of the regular ticket price;\n'\
                      '-student ticket - discount 50% of the regular ticket price;\n'\
                      '-late ticket - additional 10% to the reguler ticket price.\n'\
                      'All tickets must have the following properties:\n'\
                      '-the ability to construct a ticket by number;\n'\
                      '-the ability to ask for a ticket’s price;\n'\
                      '-the ability to print a ticket as a String.'
        self.list_students = Label(self.root, text=self.__task, fg='#000000', bg='#12c4c0', font=('Comic Sans MS', 15))

        self.f1 = Frame(self.root, width=900, height=600, bg='#262626')
        self.label1 = Label(self.root, text='Laba 3 Part1_1', fg='#12c4c0', bg='#262626', font=('Comic Sans MS', 20))
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
        self.button_open_tabs.place(x=300, y=460)

        self.f1.place(x=0, y=0)

        self.problem_label = None
        self.problem_is_active = False
        self.file_text = None

        self.img1 = ImageTk.PhotoImage(Image.open('open.png'))
        self.open_buttons = Button(self.root, image=self.img1,
                                   command=self.open_bar,
                                   border=0,
                                   bg='#262626',
                                   activebackground='#262626')
        self.open_buttons.place(x=5, y=10)

    def open_bar(self):
        self.main_frame.destroy()
        self.bar_button = menu_button.MenuButton(self.root)

    def start_app(self):
        self.label2.destroy()
        self.button_open_tabs.destroy()

        self.main_frame = Frame(self.root, width=900, height=600, bg='#262626')
        self.main_frame.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self.main_frame, bg='#323232')
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        # configure the Canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        # create another frame inside the Canvas
        self.second_frame = Frame(self.canvas, bg='#323232')
        self.canvas.create_window((0, 0), window=self.second_frame, anchor='nw')
        # main label
        self.main_label = Label(self.second_frame, text='All ITEvents in the World',
                                fg='white', bg='#323232', font=('Comic Sans MS Bold', 35))
        self.main_label.place(x=170, y=40)
        # Frames
        self.design_frame1 = Frame(self.second_frame, bg='#262626', width=600, height=10)
        self.design_frame1.place(x=170, y=40)
        self.design_frame2 = Frame(self.second_frame, bg='#262626', width=600, height=10)
        self.design_frame2.place(x=170, y=105)
        #########################################
        #   need to create all events objects   #
        #########################################
        self.event1 = Event('BRECKERS GAME JAM', 1, datetime.strptime('2022-03-28', '%Y-%m-%d').date(), 1000.0, 500)
        self.event2 = Event('HACKwithMATE HACKATHON', 2, datetime.strptime('2022-12-04',
                                                                           '%Y-%m-%d').date(), 1000.0, 400)
        self.event3 = Event('AI CONFERENCE 2022', 3, datetime.strptime('2022-02-11', '%Y-%m-%d').date(), 1200.0, 600)
        self.event4 = Event('PAN-INDIA ONLINE HACKATHON', 4,
                            datetime.strptime('2022-04-26', '%Y-%m-%d').date(), 400.0, 50)
        self.event5 = Event('GLOBAL GAME JAM', 5, datetime.strptime('2022-01-16', '%Y-%m-%d').date(), 750.0, 100)
        self.event6 = Event('TREX HACKATHON', 6, datetime.strptime('2022-04-04', '%Y-%m-%d').date(), 400.0, 500)
        self.event7 = Event('DECODE THE OCEAN 2022', 7, datetime.strptime('2022-07-15', '%Y-%m-%d').date(), 850.0, 60)
        # Buttons_create
        self.event_image1 = ImageTk.PhotoImage(Image.open('event1.png'))
        Button(self.second_frame, image=self.event_image1,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=lambda: self.tickets_controller(self.event1)).grid(row=10, column=0, pady=200, padx=200)
        Label(self.second_frame, text=text.event1,
              fg='#12c4c0', bg='#323232', font=('Comic Sans MS', 16)).place(x=180, y=510)
        self.event_image2 = ImageTk.PhotoImage(Image.open('event2.png'))
        Button(self.second_frame, image=self.event_image2,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=lambda: self.tickets_controller(self.event2)).grid(row=100, column=0, pady=150, padx=50)
        Label(self.second_frame, text=text.event2,
              fg='#12c4c0', bg='#323232', font=('Comic Sans MS', 16)).place(x=180, y=1210)
        self.event_image3 = ImageTk.PhotoImage(Image.open('event3.png'))
        Button(self.second_frame, image=self.event_image3,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=lambda: self.tickets_controller(self.event3)).grid(row=200, column=0, pady=150, padx=50)
        Label(self.second_frame, text=text.event3,
              fg='#12c4c0', bg='#323232', font=('Comic Sans MS', 16)).place(x=180, y=1810)
        self.event_image4 = ImageTk.PhotoImage(Image.open('event4.png'))
        Button(self.second_frame, image=self.event_image4,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=lambda: self.tickets_controller(self.event4)).grid(row=300, column=0, pady=150, padx=50)
        Label(self.second_frame, text=text.event4,
              fg='#12c4c0', bg='#323232', font=('Comic Sans MS', 16)).place(x=180, y=2410)
        self.event_image5 = ImageTk.PhotoImage(Image.open('event5.png'))
        Button(self.second_frame, image=self.event_image5,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=lambda: self.tickets_controller(self.event5)).grid(row=400, column=0, pady=150, padx=50)
        Label(self.second_frame, text=text.event5,
              fg='#12c4c0', bg='#323232', font=('Comic Sans MS', 16)).place(x=180, y=3050)
        self.event_image6 = ImageTk.PhotoImage(Image.open('event6.png'))
        Button(self.second_frame, image=self.event_image6,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=lambda: self.tickets_controller(self.event6)).grid(row=500, column=0, pady=150, padx=50)
        Label(self.second_frame, text=text.event6,
              fg='#12c4c0', bg='#323232', font=('Comic Sans MS', 16)).place(x=180, y=3710)
        self.event_image7 = ImageTk.PhotoImage(Image.open('event7.png'))
        Button(self.second_frame, image=self.event_image7,
               fg='white',
               border=0,
               bg='#12c4c0',
               activeforeground='#0f9d9a',
               activebackground='#12c4c0',
               command=lambda: self.tickets_controller(self.event7)).grid(row=600, column=0, pady=150, padx=50)
        Label(self.second_frame, text=text.event7,
              fg='#12c4c0', bg='#323232', font=('Comic Sans MS', 16)).place(x=180, y=4210)

        self.img1 = ImageTk.PhotoImage(Image.open('open.png'))
        self.color_frame = Frame(self.main_frame, width=50, height=900, bg='#262626')
        self.color_frame.place(x=0, y=0)
        self.open_buttons = Button(self.main_frame, image=self.img1,
                                   command=self.open_bar,
                                   border=0,
                                   bg='#262626',
                                   activebackground='#262626')
        self.open_buttons.place(x=5, y=10)
        self.img2 = ImageTk.PhotoImage(Image.open('user.png'))
        self.user_buttons = Button(self.main_frame, image=self.img2, border=0)
        self.user_buttons.place(x=845, y=10)

    def tickets_controller(self, event):
        ################################################
        #   Next step - add all types of tickets:      #
        #   Regular(Ticket), Late, Student, Advance    #
        ################################################
        self.main_label.destroy()
        self.ff1 = Frame(self.root, width=900, height=600, bg='#262626')
        self.ff1.place(x=0, y=0)

        self.ticket_imag1 = ImageTk.PhotoImage(Image.open('regular.png'))
        self.but1 = Button(self.ff1, image=self.ticket_imag1,
                           fg='white',
                           border=0,
                           activeforeground='#0f9d9a',
                           activebackground='#12c4c0',
                           command=lambda: self.order_ticket('regular', event))
        self.but1.place(x=50, y=50)
        price1 = str(event.price)
        Label(self.ff1, text=price1 + '$', fg='#12c4c0', bg='#323232',
              font=('Comic Sans MS', 16)).place(x=70, y=180)
        self.ticket_imag2 = ImageTk.PhotoImage(Image.open('advance.png'))
        self.but2 = Button(self.ff1, image=self.ticket_imag2,
                           fg='white',
                           border=0,
                           activeforeground='#0f9d9a',
                           activebackground='#12c4c0',
                           command=lambda: self.order_ticket('advance', event))
        self.but2.place(x=410, y=50)
        price2 = str(event.price * 0.4)
        Label(self.ff1, text=price2 + '$', fg='#12c4c0', bg='#323232',
              font=('Comic Sans MS', 16)).place(x=450, y=180)

        self.ticket_imag3 = ImageTk.PhotoImage(Image.open('late.png'))
        self.but3 = Button(self.ff1, image=self.ticket_imag3,
                           fg='white',
                           border=0,
                           activeforeground='#0f9d9a',
                           activebackground='#12c4c0',
                           command=lambda: self.order_ticket('late', event))
        self.but3.place(x=50, y=300)
        price3 = str(event.price * 1.1)
        Label(self.ff1, text=price3 + '$', fg='#12c4c0', bg='#323232',
              font=('Comic Sans MS', 16)).place(x=70, y=440)
        self.ticket_imag4 = ImageTk.PhotoImage(Image.open('student.png'))
        self.but4 = Button(self.ff1, image=self.ticket_imag4,
                           fg='white',
                           border=0,
                           activeforeground='#0f9d9a',
                           activebackground='#12c4c0',
                           command=lambda: self.order_ticket('student', event))
        self.but4.place(x=410, y=300)
        price4 = str(event.price * 0.5)
        Label(self.ff1, text=(price4 + '$'), fg='#12c4c0', bg='#323232',
              font=('Comic Sans MS', 16)).place(x=450, y=440)
        # back to task
        self.but5 = Button(self.ff1,
                           text='BACK',
                           font=('Comic Sans MS', 14),
                           width=14,
                           height=2,
                           fg='white',
                           border=0,
                           bg='#12c4c0',
                           activeforeground='#0f9d9a',
                           activebackground='#12c4c0',
                           command=self.back_app)
        self.but5.place(x=410, y=500)
        # and create all ITEvents

    def create_events(self):
        pass

    def back_app(self):
        self.ff1.destroy()

    @staticmethod
    def order_ticket(type_of_tickets, event):
        pdf = None
        ticket = None
        description = None
        if not isinstance(type_of_tickets, str):
            raise TypeError('The [type_of_tickets] must be a string')
        if type_of_tickets == 'regular':
            today = dat.today()
            difference = (event.date - today).days
            print(difference)
            if not 10 <= difference <= 60:
                messagebox.showinfo('Buying failed', 'You cannot buy this ticket, please, try another ticket')
                return
            else:
                messagebox.showinfo('Buying succeeded', 'Our admin is connecting to u')
            #############################
            #   CREATE REGULAR TICKET   #
            #############################

            ticket = Ticket(event.name, event.date, event.price)
            pdf = PDF('P', 'mm', 'Letter', 1)
            ticket.buy_ticket()
            print(ticket)
        elif type_of_tickets == 'advance':
            #############################
            #   CREATE ADVANCE TICKET   #
            #############################
            today = dat.today()
            difference = (event.date - today).days
            print(difference)
            if difference <= 60:
                messagebox.showinfo('Buying failed', 'You cannot buy this ticket, please, try another ticket')
                return
            else:
                messagebox.showinfo('Buying succeeded', 'Our admin is connecting to u')
            ticket = AdvanceTicket(event.name, event.date, event.price)
            pdf = PDF('P', 'mm', 'Letter', 2)
            ticket.buy_ticket()
            print(ticket)
        elif type_of_tickets == 'late':
            #############################
            #     CREATE LATE TICKET    #
            #############################
            today = dat.today()
            difference = (event.date - today).days
            print(difference)
            if 10 <= difference:
                messagebox.showinfo('Buying failed', 'You cannot buy this ticket, please, try another ticket')
                return
            else:
                messagebox.showinfo('Buying succeeded', 'Our admin is connecting to u')
            ticket = LateTicket(event.name, event.date, event.price)
            pdf = PDF('P', 'mm', 'Letter', 3)
            ticket.buy_ticket()
            print(ticket)
        elif type_of_tickets == 'student':
            #############################
            #   CREATE STUDENT TICKET   #
            #############################
            messagebox.showinfo('Buying succeeded', 'Our admin is connecting to u')
            ticket = StudentTicket(event.name, event.date, event.price)
            pdf = PDF('P', 'mm', 'Letter', 4)
            ticket.buy_ticket()
            print(ticket)

        # get total page numbers
        pdf.alias_nb_pages()
        # Set auto page break
        pdf.set_auto_page_break(auto=True, margin=15)
        # Add Page
        pdf.add_page()
        # specify font
        pdf.set_font('times', 'B', 20)
        pdf.output('ticket.pdf')
        description = str(ticket)
        send = Send(description)


class Send:
    __sender_email = 'pppython.oop@gmail.com'
    __password = 'kapustaqwe123zxc'
    __client_email = 'zhenia.yf@gmail.com'

    def __init__(self, description):
        self.send = sendpdf(Send.__sender_email,
                            Send.__client_email,
                            Send.__password,
                            'Buying a ticket',
                            description,
                            'ticket',
                            'C:/Users/zheni/Education/KPI/2 курс/1 семестр/Python/Labkiss/PythonLabs-master/'
                            'labKiss2/part2')
        self.send.email_send()
