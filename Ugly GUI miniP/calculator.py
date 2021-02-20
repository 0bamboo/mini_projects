from tkinter import *


class Calculator():

    def __init__(self):

        self.window = Tk()

        # The label where to see the result of opertions
        self.result_entry = Entry(width = 33, font = ('Courier', 18))
        # The buttons of calculator
        self.button_1 = Button(master = self.window, text = '1', command = lambda : self.insert_number(1))
        self.button_2 = Button(master = self.window, text = '2', command = lambda : self.insert_number(2))
        self.button_3 = Button(master = self.window, text = '3', command = lambda : self.insert_number(3))
        self.button_minus = Button(master = self.window, fg = 'blue', text = '-', command = lambda : self.set_the_operation('-'))

        self.button_4 = Button(master = self.window, text = '4', command = lambda : self.insert_number(4))
        self.button_5 = Button(master = self.window, text = '5', command = lambda : self.insert_number(5))
        self.button_6 = Button(master = self.window, text = '6', command = lambda : self.insert_number(6))
        self.button_plus = Button(master = self.window, fg = 'blue', text = '+', command = lambda : self.set_the_operation('+'))
        
        self.button_7 = Button(master = self.window, text = '7', command = lambda : self.insert_number(7))
        self.button_8 = Button(master = self.window, text = '8', command = lambda : self.insert_number(8))
        self.button_9 = Button(master = self.window, text = '9', command = lambda : self.insert_number(9))
        self.button_reset = Button(master = self.window, fg = 'blue', text = 'CE', command = self.clear)
        
        self.button_0 = Button(master = self.window, text = '0', command = lambda : self.insert_number(0))
        self.button_multi = Button(master = self.window, fg = 'blue', text = '*', command = lambda : self.set_the_operation('*'))
        self.button_div = Button(master = self.window, text = '/', command = lambda : self.set_the_operation('/'))
        self.button_mod = Button(master = self.window, text = '%', command = lambda : self.set_the_operation('%'))
        
        self.button_equal = Button(master = self.window, fg = 'blue', text = '=', command = self.get_result)


    def insert_number(self, number):
        """ This function for insert the number in the entry label """

        self.result_entry.insert(END, number)


    def clear(self):
        """ This function for clearing entry label """

        self.result_entry.delete(0, END)


    def set_the_operation(self, operation):
        """ This functino for set which operation to use for calculating """

        global result
        global oper
        entry_str = self.result_entry.get()
        if entry_str:
            result = int(self.result_entry.get())
        oper = operation
        self.result_entry.delete(0, END)


    def get_result(self):
        """ This function for print the result of the operation in the entry label """

        if self.result_entry.get() and oper:
            second_number = int(self.result_entry.get())
            self.result_entry.delete(0, END)
            if oper == '+':
                self.result_entry.insert(END, result + second_number)
            elif oper == '*':
                self.result_entry.insert(END, result * second_number)
            elif oper == '-':
                self.result_entry.insert(END, result - second_number)
            elif oper == '/':
                self.result_entry.insert(END, result / second_number)
            elif oper == '%':
                self.result_entry.insert(END, result % second_number)
    

    def build_widgets(self):
        """ This function sets all the widget and all its data """

        self.result_entry.grid(columnspan = 4, ipadx = 15, ipady = 15, sticky = E+N+W+S)
        # The position of buttons
        self.button_7.grid(row = 1, column = 0, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_8.grid(row = 1, column = 1, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_9.grid(row = 1, column = 2, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_reset.grid(row = 1, column = 3, ipadx = 10, ipady = 10, sticky=E+W+N+S)

        self.button_4.grid(row = 2, column = 0, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_5.grid(row = 2, column = 1, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_6.grid(row = 2, column = 2, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_plus.grid(row = 2, column = 3, ipadx = 10, ipady = 10, sticky=E+W+N+S)

        self.button_1.grid(row = 3, column = 0, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_2.grid(row = 3, column = 1, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_3.grid(row = 3, column = 2, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_minus.grid(row = 3, column = 3, ipadx = 10, ipady = 10, sticky=E+W+N+S)

        self.button_0.grid(row = 4, column = 0, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.button_mod.grid(row = 4, column = 1, ipadx = 10, ipady = 10, sticky = E+S+W+N)
        self.button_div.grid(row = 4, column = 2, ipadx = 10, ipady = 10, sticky = E+S+N+W)
        self.button_multi.grid(row = 4, column = 3, ipadx = 10, ipady = 10, sticky=E+W+N+S)

        
        self.button_equal.grid(row = 5, column = 0, columnspan = 4, ipadx = 10, ipady = 10, sticky=E+W+N+S)
        self.window.rowconfigure([0,1,2,3,4,5], weight = 1)
        self.window.columnconfigure([0,1,2,3], weight = 1)


    def launch_app(self):
        """ For starting the calculator app """

        self.build_widgets()
        self.window.mainloop()



if __name__ == "__main__":
    start = Calculator()
    start.launch_app()