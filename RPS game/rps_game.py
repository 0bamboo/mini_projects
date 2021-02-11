from tkinter import *
import random as rd


window = Tk()
window.title('R x P x S')

example_entry = Entry(text = 'enter something', fg = 'yellow')
example_entry.grid(row = 0, column = 0, rowspan = 3)

window.mainloop()