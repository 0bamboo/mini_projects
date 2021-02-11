from tkinter import *

window = Tk()

# window.rowconfigure(0, minsize = 600)
# window.columnconfigure(0, minsize = 600)

# The label where to see the result of opertions
result_entry = Entry()
result_entry.grid(columnspan = 4, padx = 5, pady = 5)

# The buttons of calculator
button_1 = Button(master = window, text = '1')
button_2 = Button(master = window, text = '2')
button_3 = Button(master = window, text = '3')
button_4 = Button(master = window, text = '4')
button_5 = Button(master = window, text = '5')
button_6 = Button(master = window, text = '6')
button_7 = Button(master = window, text = '7')
button_8 = Button(master = window, text = '8')
button_9 = Button(master = window, text = '9')
button_0 = Button(master = window, text = '0')
button_reset = Button(master = window, text = 'CE')
button_plus = Button(master = window, text = '+')
button_minus = Button(master = window, text = '-')
button_multi = Button(master = window, text = '*', width = 8)
button_equal = Button(master = window, text = '=', width = 8)

# The position of buttons

button_7.grid(row = 1, column = 0, padx = 2, pady = 2, ipadx = 10, ipady = 10)
button_8.grid(row = 1, column = 1, padx = 2, pady = 2, ipadx = 10, ipady = 10)
button_9.grid(row = 1, column = 2, padx = 2, pady = 2, ipadx = 10, ipady = 10)
button_reset.grid(row = 1, column = 3, padx = 2, pady = 2, ipadx = 6, ipady = 10)

button_4.grid(row = 2, column = 0, padx = 2, ipadx = 10, pady = 2, ipady = 10)
button_5.grid(row = 2, column = 1, padx = 2, ipadx = 10, pady = 2, ipady = 10)
button_6.grid(row = 2, column = 2, ipadx = 10, padx = 2, pady = 2, ipady = 10)
button_plus.grid(row = 2, column = 3, ipadx = 10, padx = 2, pady = 2, ipady = 10)

button_1.grid(row = 3, column = 0, ipadx = 10, padx = 2, pady = 2, ipady = 10)
button_2.grid(row = 3, column = 1, ipadx = 10, padx = 2, pady = 2, ipady = 10)
button_3.grid(row = 3, column = 2, ipadx = 10, padx = 2, pady = 2, ipady = 10)
button_minus.grid(row = 3, column = 3, padx = 2, pady = 2, ipadx = 10, ipady = 10)

button_equal.grid(row = 4, column = 0, columnspan = 2, pady = 2, padx = 2, ipadx = 9, ipady = 10)
button_multi.grid(row = 4, column = 2, columnspan = 2, padx = 2, pady = 2, ipadx = 8.5, ipady = 10)

# To launch the program 
window.mainloop()
