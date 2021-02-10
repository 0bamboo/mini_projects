from tkinter import *

window = Tk()

# window.rowconfigure(0, minsize = 600)
# window.columnconfigure(0, minsize = 600)

result_entry = Entry()
result_entry.grid(columnspan = 4, padx = 5, pady = 5, ipadx = 9, ipady = 9)

button_1 = Button(text = '1')
button_2 = Button(text = '2')
button_3 = Button(text = '3')
button_4 = Button(text = '4')
button_5 = Button(text = '5')
button_6 = Button(text = '6')
button_7 = Button(text = '7')
button_8 = Button(text = '8')
button_9 = Button(text = '9')
button_0 = Button(text = '0')
button_reset = Button(text = 'CE')
button_plus = Button(text = '+')
button_minus = Button(text = '-')
button_multi = Button(text = '*')
button_equal = Button(text = '=')

button_7.grid(row = 1, column = 0, padx = 2, pady = 2, ipadx = 10, ipady = 10)
button_8.grid(row = 1, column = 1, padx = 2, pady = 2, ipadx = 10, ipady = 10)
button_9.grid(row = 1, column = 2, padx = 2, pady = 2, ipadx = 10, ipady = 10)
button_reset.grid(row = 1, column = 3, padx = 2, pady = 2, ipadx = 7, ipady = 10)

button_4.grid(row = 2, column = 0, padx = 2, ipadx = 10, pady = 2, ipady = 10)
button_5.grid(row = 2, column = 1, padx = 2, ipadx = 10, pady = 2, ipady = 10)
button_6.grid(row = 2, column = 2, ipadx = 10, padx = 2, pady = 2, ipady = 10)
button_plus.grid(row = 2, column = 3, ipadx = 10, padx = 2, pady = 2, ipady = 10)

button_1.grid(row = 3, column = 0, ipadx = 10, padx = 2, pady = 2, ipady = 10)
button_2.grid(row = 3, column = 1, ipadx = 10, padx = 2, pady = 2, ipady = 10)
button_3.grid(row = 3, column = 2, ipadx = 10, padx = 2, pady = 2, ipady = 10)
button_minus.grid(row = 3, column = 3, padx = 2, pady = 2, ipadx = 10, ipady = 10)

button_equal.grid(row = 4, column = 0, columnspan = 3, pady = 2, padx = 2, ipadx = 10, ipady = 10)
button_multi.grid(row = 4, column = 3, padx = 2, pady = 2, ipadx = 10, ipady = 10)

window.mainloop()
