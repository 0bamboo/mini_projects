from tkinter import *
import random as rd
from PIL import ImageTk,Image


window = Tk()
window.title('R x P x S')
window.iconbitmap('../../notebook_laptop_computer_pc_icon_181477.ico')


def find_the_winner(player, rand_player):
    if player.upper() == 'ROCK' and rand_player == 'SCISSOR':
        label = Label(window, text = 'You win !!')
        label.grid()
    if player.upper() == 'SCISSOR' and rand_player == 'ROCK':
        label = Label(window, text = 'You lose !!')
        label.grid()
    if player.upper() == 'PAPER' and rand_player == 'ROCK':
        label = label(window, text = 'You win !!')
        label.grid()
    if player.upper() == 'ROCK' and rand_player == 'PAPER':
        label = Label(window, text = 'You lose !!')
        label.grid()
    if player.upper() == 'SCISSOR' and rand_player == 'PAPER':
        label = Label(window, text = 'You win !!')
        label.grid()
    if player.upper() == 'PAPER' and rand_player == 'SCISSOR':
        label = Label(window, text = 'You lose !!')
        label.grid()
    else:
        label = Label(window, text = 'You entered wrong option !')


def who_is_the_winner(player):
    rps = ['ROCK', 'PAPER', 'SCISSOR']
    rand_player = rps[rd.randint(0, 2)]
    find_the_winner(player, rand_player)
    example_entry.insert(f'{rand_player}')
    

# How to use images in tkinter
# my_img = ImageTk.PhotoImage(Image.open('../../backgrounds/anime-bleach-kenpachi-zaraki-c4.jpg'))
# image_label = Label(image = my_img)
# image_label.grid(row = 4, column = 0)

frame = LabelFrame(
    window,
    text = 'R P S :',
    bg = 'LightBlue'
    )

frame_2 = Frame(window)

first_label = Label(
    frame,
    text = 'Welcome to RPS GAME ',
    font = ('Courier New', 20),
    fg = '#000080',
    )

first_label.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 15, sticky = W+E)

example_entry = Entry(frame)
example_entry.grid(row = 1, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 5, ipady = 5)

player_entry = Entry(frame)
player_entry.grid(row = 3, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 5, ipady = 5)

start_label = Button(frame,text = 'Start', activebackground = 'yellow', command = lambda : who_is_the_winner(player_entry.get()))
start_label.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 10, ipady = 10)

frame.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
frame_2.grid(row = 1, column = 0)

window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)

window.mainloop() 