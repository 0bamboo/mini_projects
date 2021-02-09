from tkinter import *
import random as rd


window = Tk()
window.title('R x P x S')
# window.geometry('400x200')

window.rowconfigure(0, minsize = 200, weight = 1)
window.columnconfigure(0, minsize = 400, weight = 1)

frame_title = Frame(window)
frame_game = Frame(window)

label_1 = Label(frame_title, text = 'hello from frame title',)
label_2 = Label(frame_game, text = 'hello from east', relief = RAISED, bg = 'yellow')
label_3 = Label(frame_game, text = 'hello from center', )
label_4 = Label(frame_game, text = 'hello from west', )

label_1.pack(anchor = CENTER, padx = 3, pady = 3)
label_2.pack(anchor = 'se')
label_3.pack(anchor = CENTER)
label_4.pack(anchor = 'sw')

frame_title.grid(row = 0, column = 0, sticky = 'nsew')
frame_game.grid(row = 1, column = 0,)

window.mainloop()