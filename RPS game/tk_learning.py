from tkinter import *
import random as  rd

from tkinter import *

# THE INITIALIZING OF THE WINDOW
window = Tk()

# A SIMPLE FRAME 
# frame_a = Frame()
# frame_b = Frame()

# # THIS HOW TO CREATE LABEL
# label_a = Label(master = frame_a, text = 'Im in frame_a')
# label_a.pack()

# label_b = Label(master = frame_b, text = 'Im in frame_b')
# label_b.pack()

# frame_b.pack()
# frame_a.pack()

border_effects = {
    'flat' : FLAT,
    'sunken' : SUNKEN,
    'raised' : RAISED,
    'groove' : GROOVE,
    'ridge' : RIDGE,
}


# THIS THE TYPES OF BORDER EFFECTS

for relief_name, relief in border_effects.items():
    # You use the releif option for setting the border type
    frame = Frame(master = window, relief = relief, borderwidth = 5)
    # Use the side var for setting the path of frames vertical or horizontal 
    # Use the fill var for setting the path of responsivity use the option both with the option expand set to true 
    # for setting the frame to be responsive in all directions
    frame.pack(side = RIGHT, fill = BOTH, expand = True)
    label =  Label(master = frame, text = relief_name)
    label.pack()

frame_pl = Frame(master = window, width = 150, height = 100)
label_with_placemethod = Label(text = 'Hello from (11, 45)', bg = 'blue', fg = 'grey')

# The method place is for setting the place of the label , but it's not responsive ....
label_with_placemethod.place(x = 11, y = 45)
frame_pl.pack()

window.mainloop()