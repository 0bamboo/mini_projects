from tkinter import *
import random as rd
from PIL import ImageTk,Image


window = Tk()
window.title('R x P x S')

def who_is_the_winner(player):
    pass

# How to use images in tkinter
# my_img = ImageTk.PhotoImage(Image.open('../../backgrounds/anime-bleach-kenpachi-zaraki-c4.jpg'))
# image_label = Label(image = my_img)
# image_label.grid(row = 4, column = 0)

first_label = Label(
    text = 'Welcome to RPS GAME ',
    font = ('Arial', 15)
    )
first_label.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 15)

example_entry = Entry(text = 'enter something', fg = 'yellow')
example_entry.grid(row = 1, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 5, ipady = 5)

player_entry = Entry()
player_entry.grid(row = 3, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 5, ipady = 5)

start_label = Button(text = 'Start', activebackground = 'yellow', command = lambda : who_is_the_winner(player_entry.get()))
start_label.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 10, ipady = 10)

window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)

window.mainloop()