from tkinter import *
from PIL import ImageTk, Image

w = Tk()
w.geometry('900x500')
w.configure(bg='#262626')
w.resizable(False, False)
w.title('Toggle Menu')

# l1 = Label(w, text='LabKiss', fg='white', bg='#262626')
# l1.config(font=('Comic Sans MS', 90))
# l1.pack(expand=True)

def default_home():
    f2 = Frame(w, width=900, height=455, bg='#262626')
    f2.place(x=0, y=45)
    l2 = Label(w, text='LabKiss', fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 90))
    l2.place(x=290, y=105)
    #l2.pack(expand=True)
#
# def laba2_part2_2():
#     f1.destroy()
#     f2 = Frame(w, width=900, height=455, bg='#262626')
#     f2.place(x=0, y=45)
#     l2 = Label(w, text='LabKiss', fg='white', bg='#262626')
#     l2.config(font=('Comic Sans MS', 90))
#     l2.place(x=290, y=105)
#     #l2.pack(expand=True)

def toggle_win():
    f1 = Frame(w, width=300, height=500, bg='#12c4c0')
    f1.place(x=0, y=0)


    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=42,
                           height=2,
                           fg='#262626',
                           border=0,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor,
                           command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 40, 'LABA 2  Part2 Task2', '#0f9d9a', '#12c4c0', None)
    bttn(0, 70, 'LABA 2  Part2 Task3', '#0f9d9a', '#12c4c0', None)
    bttn(0, 100, 'LABA 2  Part2 Tass4', '#0f9d9a', '#12c4c0', None)
    bttn(0, 130, 'LABA 3  Part1 Task1', '#0f9d9a', '#12c4c0', None)
    bttn(0, 160, 'LABA 3  Part1 Task2', '#0f9d9a', '#12c4c0', None)
    bttn(0, 190, 'LABA 3  Part2 Task1', '#0f9d9a', '#12c4c0', None)
    bttn(0, 220, 'LABA 3  Part2 Task2', '#0f9d9a', '#12c4c0', None)
    bttn(0, 250, 'LABA 3  Part2 Task3', '#0f9d9a', '#12c4c0', None)
    bttn(0, 280, 'LABA 3  Part2 Task4', '#0f9d9a', '#12c4c0', None)
    bttn(0, 310, 'LABA 4  Part1 Task1', '#0f9d9a', '#12c4c0', None)
    bttn(0, 340, 'LABA 4  Part1 Task2', '#0f9d9a', '#12c4c0', None)
    bttn(0, 370, 'LABA 4  Part2 Task1', '#0f9d9a', '#12c4c0', None)
    bttn(0, 400, 'LABA 4  Part2 Task2', '#0f9d9a', '#12c4c0', None)
    bttn(0, 430, 'LABA 4  Part2 Task3', '#0f9d9a', '#12c4c0', None)
    bttn(0, 460, 'LABA 4  Part2 Task4', '#0f9d9a', '#12c4c0', None)


    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5, y=10)


default_home()

img1 = ImageTk.PhotoImage(Image.open("open.png"))
Button(w, image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=5, y=10)

w.mainloop()
