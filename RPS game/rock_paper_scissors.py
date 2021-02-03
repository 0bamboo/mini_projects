from tkinter import *
import random as  rd

from tkinter import *


window = Tk()
label = Label(text = "Hello from label", foreground = 'DarkTurquoise', background = 'LightSalmon', width = 50, height = 20)
label.pack()
new_button = Button(text = 'Heat me hahah')
new_button.pack()
entry = Entry(fg='yellow', bg = 'blue', width = '50')
entry.pack()
entry.get()
print(entry.get())
window.mainloop()
