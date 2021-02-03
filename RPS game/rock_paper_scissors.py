from tkinter import *
import random as  rd

from tkinter import *

# THE INITIALIZING OF THE WINDOW
window = Tk()

# A SIMPLE FRAME 
frame_a = Frame()
frame_b = Frame()

# THIS HOW TO CREATE LABEL
label_a = Label(master = frame_a, text = 'Im in frame_a')
label_a.pack()

label_b = Label(master = frame_b, text = 'Im in frame_b')
label_b.pack()

border_effects = {
    'flat' : FLAT,
    'sunken' : SUNKEN,
    'raised' : RAISED,
    'groove' : GROOVE,
    'ridge' : RIDGE,
}

frame_b.pack()
frame_a.pack()

# THIS THE TYPES OF BORDER EFFECTS 
for relief_name, relief in border_effects.items():
    frame = Frame(master = window, relief = relief, borderwidth = 5)
    frame.pack(side = LEFT)
    label =  Label(master = frame, text = relief_name)
    label.pack()

window.mainloop()