from tkinter import *

from numpy import column_stack

root = Tk()
root.title("Calculadora")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    try:
        if last_button == 'equal':
            e.delete(0, END)  # deleta o que já na caixinha de entrada
            e.insert(0, str(number))
        else:
            current = e.get()
            e.delete(0, END)  # deleta o que já na caixinha de entrada
            e.insert(0, current+str(number))
            last_button = 'number'
    except:
        current = e.get()
        e.delete(0, END)  # deleta o que já na caixinha de entrada
        e.insert(0, current+str(number))

def button_clear():
    e.delete(0, END)

def add():
    first_number = e.get()
    global f_num
    global op
    op = 'sum'
    f_num = int(first_number)
    e.delete(0,END)

def mult():
    first_number = e.get()
    global f_num
    global op
    op = 'mult'
    f_num = int(first_number)
    e.delete(0,END)

def div():
    first_number = e.get()
    global f_num
    global op
    op = 'div'
    f_num = int(first_number)
    e.delete(0,END)

def sub():
    first_number = e.get()
    global f_num
    global op
    op = 'sub'
    f_num = int(first_number)
    e.delete(0,END)

def equal():
    global last_button
    last_button = 'equal'
    second_number = int(e.get())
    e.delete(0,END)
    if op == 'sum':
        e.insert(0,f_num + second_number)
    elif op =='mult':
        e.insert(0,f_num*second_number)
    elif op =='div':
        e.insert(0,f_num/second_number)
    else:
        e.insert(0,f_num-second_number)

# criando os botões


button_1 = Button(root, text='1', padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20,
                  command=lambda: button_click(0))
button_add = Button(root, text='+', padx=38, pady=20,
                    command=add)
button_sub = Button(root, text='-', padx=41, pady=20,
                    command=sub)
button_div = Button(root, text='/', padx=41, pady=20,
                    command=div)
button_mult = Button(root, text='*', padx=41, pady=20,
                     command=mult)
button_equal = Button(root, text='=', padx=38, pady=20,
                      command=equal)
button_clean = Button(root, text='c', padx=145, pady=5,
                      command=button_clear)

# colocando os botões na tela
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_add.grid(row=5, column=1)
button_sub.grid(row=5, column=2)
button_div.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_equal.grid(row=6, column=2)
button_clean.grid(row=1, column=0, columnspan=3)

root.mainloop()
