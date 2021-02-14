from tkinter import *
import random as rd
import time as t
# from PIL import ImageTk,Image


# Create a class for the rps_game
class Result_Popup_Window():

    def __init__(self, master_window):
        self.master_window = master_window
        self.child = Toplevel(master_window)




class Rps_App():

    def __init__(self):
        self.window = Tk()
        self.window.title('R x P x S')

        self.frame = LabelFrame(
            self.window,
            text = 'R P S :',
            bg = 'LightBlue'
            )
        self.frame_2 = Frame(self.window)

        self.rps = ['ROCK', 'PAPER', 'SCISSOR']

        self.first_label = Label(
            self.frame,
            text = 'Welcome to RPS GAME ',
            font = ('Courier New', 20),
            fg = '#000080',
            )


        self.example_entry = Entry(self.frame)
        self.example_entry.configure(state = 'readonly')


        clicked = StringVar()
        clicked.set('Choose your option :')

        self.player_entry = OptionMenu(self.frame, clicked, 'Rock', 'Paper', 'Scissor')

        self.start_label = Button(self.frame,text = 'Start', activebackground = 'yellow', command = lambda : self.who_is_the_winner(clicked.get()))


        self.window.grid_rowconfigure(0, weight = 1)
        self.window.grid_columnconfigure(0, weight = 1)
    

    def find_the_winner(self, player, rand_player):
        """ This function returns the result of the game """

        text = ''
        if (player.upper() == 'ROCK' and rand_player == 'SCISSOR') or\
        (player.upper() == 'PAPER' and rand_player == 'ROCK') or\
        (player.upper() == 'SCISSOR' and rand_player == 'PAPER'):
            text = 'You win !!'
        elif (player.upper() == 'SCISSOR' and rand_player == 'ROCK') or\
        (player.upper() == 'ROCK' and rand_player == 'PAPER') or\
        (player.upper() == 'PAPER' and rand_player == 'SCISSOR'):
            text = 'You lose !!'
        elif (player.upper() == 'PAPER' and rand_player == 'PAPER') or\
        (player.upper() == 'ROCK' and rand_player == 'ROCK') or\
        (player.upper() == 'SCISSOR' and rand_player == 'SCISSOR'):
            text = 'Draw'
        else:
            text = 'You entered a wrong option.'
        label = Label(self.window, text = text)
        label.grid()
    

    def who_is_the_winner(self, player):
        """ This funciton sets the random value of the other player and call the function that finds the winner """

        rand_player = self.rps[rd.randint(0, 2)]
        self.find_the_winner(player, rand_player)
        self.example_entry.configure(state = 'normal')
        self.example_entry.delete(0, END)
        self.example_entry.insert(0, rand_player)
        self.example_entry.configure(state = 'readonly')


    def runApp(self):
        """ This function starts the app """

        self.first_label.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 15, sticky = W+E)
        self.example_entry.grid(row = 1, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 5, ipady = 5)
        self.player_entry.grid(row = 3, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 5, ipady = 5)
        self.start_label.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 10, ipady = 10)
        self.frame.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
        self.frame_2.grid(row = 1, column = 0)
        self.window.mainloop() 



app = Rps_App()
app.runApp()


# window = Tk()
# window.title('R x P x S')
# global count 
# count = 0
# window.iconbitmap('../../notebook_laptop_computer_pc_icon_181477.ico')


# def find_the_winner(player, rand_player):
#     text = ''
#     global count
#     if (player.upper() == 'ROCK' and rand_player == 'SCISSOR') or\
#     (player.upper() == 'PAPER' and rand_player == 'ROCK') or\
#     (player.upper() == 'SCISSOR' and rand_player == 'PAPER'):
#         text = 'You win !!'
#     elif (player.upper() == 'SCISSOR' and rand_player == 'ROCK') or\
#     (player.upper() == 'ROCK' and rand_player == 'PAPER') or\
#     (player.upper() == 'PAPER' and rand_player == 'SCISSOR'):
#         text = 'You lose !!'
#     elif (player.upper() == 'PAPER' and rand_player == 'PAPER') or\
#     (player.upper() == 'ROCK' and rand_player == 'ROCK') or\
#     (player.upper() == 'SCISSOR' and rand_player == 'SCISSOR'):
#         text = 'Draw'
#     else:
#         text = 'You entered a wrong option.'
#     label = Label(window, text = text)
#     label.grid()



# def who_is_the_winner(self, player):
#     rps = ['ROCK', 'PAPER', 'SCISSOR']
#     rand_player = self.rps[rd.randint(0, 2)]
#     find_the_winner(player, rand_player)
#     example_entry.configure(state = 'normal')
#     example_entry.delete(0, END)
#     example_entry.insert(0, rand_player)
#     example_entry.configure(state = 'readonly')
    

# How to use images in tkinter
# my_img = ImageTk.PhotoImage(Image.open('../../backgrounds/anime-bleach-kenpachi-zaraki-c4.jpg'))
# image_label = Label(image = my_img)
# image_label.grid(row = 4, column = 0)

# frame = LabelFrame(
#     window,
#     text = 'R P S :',
#     bg = 'LightBlue'
#     )

# frame_2 = Frame(window)

# first_label = Label(
#     frame,
#     text = 'Welcome to RPS GAME ',
#     font = ('Courier New', 20),
#     fg = '#000080',
#     )

# first_label.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 15, sticky = W+E)

# example_entry = Entry(frame)
# example_entry.configure(state = 'readonly')

# example_entry.grid(row = 1, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 5, ipady = 5)

# clicked = StringVar()
# clicked.set('Choose your option :')

# player_entry = OptionMenu(frame, clicked, 'Rock', 'Paper', 'Scissor')
# player_entry.grid(row = 3, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 5, ipady = 5)

# start_label = Button(frame,text = 'Start', activebackground = 'yellow', command = lambda : who_is_the_winner(clicked.get()))
# start_label.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 10, ipady = 10)

# frame.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
# frame_2.grid(row = 1, column = 0)

# window.grid_rowconfigure(0, weight = 1)
# window.grid_columnconfigure(0, weight = 1)

# window.mainloop() 

# import tkinter as tk
# from tkinter.messagebox import showinfo

# --- classes ---

# class PopupWindow():

#     def __init__(self, master):
#         #self.master = master
#         window = tk.Toplevel(master)

#         label = tk.Label(window, text="Hello World!")
#         label.pack(fill='x', padx=50, pady=5)

#         button_close = tk.Button(window, text="Close", command=window.destroy)
#         button_close.pack(fill='x')


# class App():

#     def __init__(self):
#         self.root = tk.Tk()

#         button_bonus = tk.Button(self.root, text="Window", command=self.popup_window)
#         button_bonus.pack(fill='x')

#         button_showinfo = tk.Button(self.root, text="ShowInfo", command=self.popup_showinfo)
#         button_showinfo.pack(fill='x')

#         button_close = tk.Button(self.root, text="Close", command=self.root.destroy)
#         button_close.pack(fill='x')

#     def run(self):
#         self.root.mainloop()

#     def popup_window(self):
#         PopupWindow(self.root)

#     def popup_showinfo(self):
#         showinfo("ShowInfo", "Hello World!")

# # --- main ---

# app = App()
# app.run()