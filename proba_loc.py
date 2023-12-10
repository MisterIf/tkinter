from tkinter import *

def set_color():
    but1.config(bg='green')

window = Tk()
window.title('Git work')
window.geometry('360x240')

but1 = Button(window, text='Open', font='Arial 12', command=set_color)
but1.place(x=150, y=100)

window.mainloop()
