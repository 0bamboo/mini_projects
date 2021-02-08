from Tkinter import *
import random as rd


window = Tk()
window.title('ROCK PAPER SCISSOR')
# window.geometry('400x200')

window.rowconfigure(0, minsize = 200, weight = 1)
window.columnconfigure(0, minsize = 400, weight = 1)

frame_title = Frame(window)
frame_game = Frame(window)

label_1 = Label(frame_title, text = 'hello from frame title',)
label_2 = Label(frame_game, text = 'hello from frame game', relief = RAISED, bg = 'yellow')
label_3 = Label(frame_game, text = 'hello from frame game', )
label_4 = Label(frame_game, text = 'hello from frame game', )

label_1.pack(anchor = CENTER, padx = 3, pady = 3)
label_2.grid(row = 0, column = 0, padx = 3, pady = 3)
label_3.grid(row = 0, column = 1, padx = 3, pady = 3)
label_4.grid(row = 0, column = 2, padx = 3, pady = 3)

frame_title.grid(row = 0, column = 0, sticky = 'nsew')
frame_game.grid(row = 1, column = 0, sticky = 'nsew')

window.mainloop()