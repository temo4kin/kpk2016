"""
from tkinter import *

class But_print:
    def __init__(self):
        self.but = Button(root,
                          width=30,height=5,
                          text="Печать",
                          bg="white",fg="blue")
        self.but.bind("<Button-1>",self.printer)
        self.but.pack()
    def printer(self,event):
        print ("Как всегда очередной 'Hello World!'")

root = Tk()
obj = But_print()
root.mainloop()
"""

import tkinter

def button1_command():
    print('Button 1 default command.')

def print_hello(event):
    #print(event.char)
    #print(event.keycode)
    print(event.num)
    print(event.x, event.y)
    #print(event.x_root, event.y_root)
    me = event.widget
    # что можно сделать с me?
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('You pressed button 2!')
    else:
        raise ValueError()


def init_main_window():
    """Инициализация главного окна. Создание всех необходимых виджетов и их упаковка"""

    global root, button1, button2, label, text, scale

    root = tkinter.Tk()

    button1 = tkinter.Button(root, text="Button 1", command=button1_command)
    button1.bind("<Button>", print_hello)
    button1.pack()

    button2 = tkinter.Button(root, text="Button 2")
    button2.bind("<Button>", print_hello)
    button2.pack()

    variable = tkinter.IntVar()
    label = tkinter.Label(root, textvariable=variable)
    scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL, length=300,
                          from_=0,to=100,tickinterval=10,resolution=1, variable=variable)
    text = tkinter.Entry(root, textvariable=variable)

    for obj in button1, button2, label, scale, text:
        obj.pack()

if __name__ == "__main__":
    init_main_window()

root.mainloop()
