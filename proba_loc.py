from tkinter import *

def set_color():
    but1.config(bg='green')
    lab.config(bg='green')
    lab_info.config(text='Color changed')

window = Tk()
window.title('Git work')
window.geometry('360x240')

but1 = Button(window, text='Open', font='Arial 12', command=set_color)
but1.place(x=150, y=100)
lab = Label(window, text='New widget')
lab.place(x=10, y=10)
lab_info = Label(window, text='Without changes')
lab_info.place(x=10, y=150)

window.mainloop()
