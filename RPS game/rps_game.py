from tkinter import *
import random as rd


window = Tk()
window.rowconfigure(0, minsize = 500)
window.columnconfigure(0, minsize = 500)
label = Label(text = 'start your game')
label.grid()
window.mainloop()