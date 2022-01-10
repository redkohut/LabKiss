from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from task2_part2_UI import MainScene


window1 = Tk()
window1.geometry('350x500')
window1.title('Login in system')
window1.resizable(False, False)

gmail = 'zhenia.yf@gmail.com'

j = 0
r = 0
for i in range(100):
    c = str(6060 + r)
    Frame(window1, width=250, height=500, bg='#d1'+c).place(x=j, y=0)
    j = j + 10
    r = r + 1

Frame(window1, width=250, height=400, bg='white').place(x=50, y=50)

# label1
label1 = Label(window1, text='Username', bg='white', fg='#d16060', font=('arial bold', 13))
label1.place(x=80, y=200)

input1 = Entry(window1, width=20, border=0, fg='#d16000', font=('arial', 11))
input1.place(x=80, y=230)

# label1
label2 = Label(window1, text='Password', bg='white', fg='#d16060', font=('arial bold', 13))
label2.place(x=80, y=280)

input2 = Entry(window1, width=20, border=0, fg='#d16000', font=('arial', 11))
input2.place(x=80, y=310)

Frame(window1, width=180, height=2, bg='#d16068').place(x=80, y=250)
Frame(window1, width=180, height=2, bg='#d16068').place(x=80, y=330)

image1 = Image.open('log.png')
image2 = ImageTk.PhotoImage(image1)

Label1 = Label(image=image2, border=0, justify=CENTER)
Label1.place(x=115, y=50)


def cmd():
    if input1.get() == 'zhenia.yf@gmail.com' and input2.get() == 'qwe123zxc':
        messagebox.showinfo('Login successful', 'Welcome in home')
        window1.destroy()
        main_scene = MainScene(900, 500)
        main_scene.run()
    else:
        messagebox.showinfo('Login failed', 'Please try again')


Button(window1, width=18, height=2, fg='white', bg='#994422',
       border=0, command=cmd, text='Login', font=('arial bold', 10)).place(x=100, y=375)

window1.mainloop()
