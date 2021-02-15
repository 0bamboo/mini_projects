from tkinter import *
import random as rd
import time as t
# from PIL import ImageTk,Image


# Create a class for the rps_game
class Result_Popup_Window():

    def __init__(self, master_window, text, start):
        self.start = start
        self.text = text
        self.master_window = master_window
        self.child = Toplevel(master_window)
        self.label = Label(self.child, text = self.text, font = ('Comic sans serif', 17))
        self.label.grid(row = 0, column = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)
        # self.start.configure(state = 'readonly')
        self.exit_button = Button(self.child, text = 'Exit', command = self.exit_child_window)
        self.exit_button.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 10, ipady = 10)

    def exit_child_window(self):
        self.start.configure(state = 'normal')
        self.child.destroy()


# class CustomButton(Canvas):
#     def __init__(self, parent, width, height, color, command=None):
#         Canvas.__init__(self, parent, borderwidth=1, 
#             relief="raised", highlightthickness=0)
#         self.command = command

#         padding = 4
#         id = self.create_oval((padding,padding,
#             width+padding, height+padding), outline=color, fill=color)
#         (x0,y0,x1,y1)  = self.bbox("all")
#         width = (x1-x0) + padding
#         height = (y1-y0) + padding
#         self.configure(width=width, height=height)
#         self.bind("<ButtonPress-1>", self._on_press)
#         self.bind("<ButtonRelease-1>", self._on_release)

#     def _on_press(self, event):
#         self.configure(relief="sunken")

#     def _on_release(self, event):
#         self.configure(relief="raised")
#         if self.command is not None:
#             self.command()


class Rps_App():

    def __init__(self,):
        self.window = Tk()
        self.window.title('R x P x S')
        self.window.resizable(0, 0)
        self.window.configure(bg = '#2a3132')

        self.frame = LabelFrame(
            self.window,
            text = 'R P S :',
            bg = '#00FA9A'
            )
        self.frame_2 = Frame(self.window)

        self.rps = ['ROCK', 'PAPER', 'SCISSOR']

        self.first_label = Label(
            self.frame,
            text = 'Welcome to RPS GAME ',
            font = ('Courier New', 20),
            fg = '#00FA9A',
            bg = '#2a3132'
            )


        self.example_entry = Entry(self.frame, width = 15)
        self.example_entry.configure(state = 'readonly')


        clicked = StringVar()
        clicked.set('Choose your option :')

        self.player_entry = OptionMenu(self.frame, clicked, 'Rock', 'Paper', 'Scissor',)
        # self.player_entry.configure(bg = '#2a3132')
        
        self.start_label = Button(self.frame,text = 'Start', width = 7, bg = '#2a3132', fg = '#00FA9A', activebackground = '#2a3132', activeforeground = '#00FA9A', command = lambda : self.who_is_the_winner(clicked.get()))
        self.exit_button = Button(self.frame_2, activebackground = '#2a3132', activeforeground = '#00FA9A', text = 'Exit', width = 7, comman = self.exitApp)
        self.exit_button.grid(row = 0, column = 1, ipadx = 5, ipady = 5)
        self.exit_button.configure(bg = '#2a3132', fg = '#00FA9A')

        # button = CustomButton(self.frame_2, 100, 25, 'red')
        # button.grid(row = 0, column = 0)

        # self.window.grid_rowconfigure(0, weight = 1)
        # self.window.grid_columnconfigure(0, weight = 1)
    

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
        Result_Popup_Window(self.window, text, self.start_label)
    

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
        self.player_entry.grid(row = 3, column = 0, columnspan = 3, ipadx = 1, ipady = 1)
        self.start_label.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 10, ipady = 10)
        self.frame.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
        self.frame_2.grid(row = 1, column = 0)
        self.window.mainloop()
    

    def exitApp(self):
        self.window.destroy()



app = Rps_App()
app.runApp()


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