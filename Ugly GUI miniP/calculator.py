from tkinter import *

window = Tk()

# window.rowconfigure(0, minsize = 600)
# window.columnconfigure(0, minsize = 600)

# Define functions

def insert_number(number):
    """ This function for insert the number in the entry label """

    result_entry.insert(END, number)


def clear():
    """ This function for clearing entry label """

    result_entry.delete(0, END)


def set_the_operation(operation):
    """ This functino for set which operation to use for calculating """

    global result
    global oper
    entry_str = result_entry.get()
    if entry_str:
        result = int(result_entry.get())
    oper = operation
    result_entry.delete(0, END)


def get_result():
    """ This function for print the result of the operation in the entry label """

    if result_entry.get() and oper:
        second_number = int(result_entry.get())
        result_entry.delete(0, END)
        if oper == '+':
            result_entry.insert(END, result + second_number)
        elif oper == '*':
            result_entry.insert(END, result * second_number)
        elif oper == '-':
            result_entry.insert(END, result - second_number)
        elif oper == '/':
            result_entry.insert(END, result / second_number)


# The label where to see the result of opertions
result_entry = Entry(width = 33, font = ('Comic sans serif', 15))
result_entry.grid(columnspan = 4, padx = 10, pady = 10, ipadx = 15, ipady = 8)

# The buttons of calculator
button_1 = Button(master = window, text = '1', padx = 30, pady = 10, command = lambda : insert_number(1))
button_2 = Button(master = window, text = '2', padx = 30, pady = 10, command = lambda : insert_number(2))
button_3 = Button(master = window, text = '3', padx = 30, pady = 10, command = lambda : insert_number(3))
button_4 = Button(master = window, text = '4', padx = 30, pady = 10, command = lambda : insert_number(4))
button_5 = Button(master = window, text = '5', padx = 30, pady = 10, command = lambda : insert_number(5))
button_6 = Button(master = window, text = '6', padx = 30, pady = 10, command = lambda : insert_number(6))
button_7 = Button(master = window, text = '7', padx = 30, pady = 10, command = lambda : insert_number(7))
button_8 = Button(master = window, text = '8', padx = 30, pady = 10, command = lambda : insert_number(8))
button_9 = Button(master = window, text = '9', padx = 30, pady = 10, command = lambda : insert_number(9))
button_0 = Button(master = window, text = '0', padx = 30, pady = 10, command = lambda : insert_number(0))
button_reset = Button(master = window, fg = 'blue', text = 'CE', padx = 25, pady = 10, command = clear)
button_plus = Button(master = window, fg = 'blue', text = '+', padx = 30, pady = 10, command = lambda : set_the_operation('+'))
button_minus = Button(master = window, fg = 'blue', text = '-', padx = 30, pady = 10, command = lambda : set_the_operation('-'))
button_multi = Button(master = window, fg = 'blue', text = '*', padx = 30, pady = 10, command = lambda : set_the_operation('*'))
button_equal = Button(master = window, fg = 'blue', text = '=', padx = 30, pady = 10, width = 12, command = get_result)

# The position of buttons
button_7.grid(row = 1, column = 0, padx = 2)
button_8.grid(row = 1, column = 1, padx = 2)
button_9.grid(row = 1, column = 2, padx = 2)
button_reset.grid(row = 1, column = 3)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_plus.grid(row = 2, column = 3)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_minus.grid(row = 3, column = 3)

button_equal.grid(row = 4, column = 0, columnspan = 2)
button_multi.grid(row = 4, column = 3)
button_0.grid(row = 4, column = 2)

# To launch the program 
window.mainloop()