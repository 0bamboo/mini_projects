from tkinter import *
import random as rd
import time as t


# Create a class for the rps_game
class Rps_App():

    def __init__(self,):
        # Setting the components of the main window 
        self.window = Tk()
        self.window.title('R x P x S')
        self.window.geometry('400x400')
        self.window.resizable(0, 0)
        self.window.configure(bg = '#2a3132')

        self.frame = LabelFrame(
            self.window,
            text = 'R P S :',
            bg = '#00FA9A',
            width = 600,
            height = 600
            )
        self.frame_2 = Frame(self.window)

        self.rps = ['ROCK', 'PAPER', 'SCISSOR']

        self.first_label = Label(
            self.frame,
            text = ' ROCK,PAPER,SCISSOR ',
            font = ('Courier New', 20),
            fg = '#00FA9A',
            bg = '#2a3132'
            )

        self.label_cmp = Label(self.frame, text = 'Computer choice :', font = ('Courier New', 10), bg = '#2a3132', fg = 'white', width = 17)
        self.example_entry = Entry(self.frame, width = 15, font = ('Courier New', 12))
        self.example_entry.configure({'background':'#2a3132', 'foreground':'#00FA9A'})

        clicked = StringVar()
        clicked.set('Rock')
        self.player_label = Label(self.frame, text = 'Player choice :', font = ('Courier New', 10), bg = '#2a3132', fg = 'white', width = 17)
        self.player_entry = OptionMenu(self.frame, clicked, 'Rock', 'Paper', 'Scissor')
        self.player_entry.configure(width = 15)
        self.player_entry.configure({'background':'#2a3132', 'foreground':'#00FA9A', 'activebackground':'#2a3132', 'activeforeground':'#00FA9A', 'font':('Courier New', 12)})
        
        self.start_label = Button(self.frame,text = 'Start', width = 7, font = ('Courier New', 10), bg = '#2a3132', fg = '#00FA9A', activebackground = '#2a3132', activeforeground = '#00FA9A', command = lambda : self.who_is_the_winner(clicked.get()))
        self.exit_button = Button(self.frame_2, activebackground = '#2a3132', font = ('Courier New', 10), activeforeground = '#00FA9A', text = 'Exit', width = 7, comman = self.exitApp)
        self.exit_button.configure(bg = '#2a3132', fg = '#00FA9A')

        self.window.grid_rowconfigure(0, weight = 1)
        self.window.grid_columnconfigure(0, weight = 1)
    

    def find_the_winner(self, player, rand_player):
        """ This function returns the result of the game """

        text = ''
        if (player.upper() == 'ROCK' and rand_player == 'SCISSOR') or\
        (player.upper() == 'PAPER' and rand_player == 'ROCK') or\
        (player.upper() == 'SCISSOR' and rand_player == 'PAPER'):
            text = 'You won !!'
        elif (player.upper() == 'SCISSOR' and rand_player == 'ROCK') or\
        (player.upper() == 'ROCK' and rand_player == 'PAPER') or\
        (player.upper() == 'PAPER' and rand_player == 'SCISSOR'):
            text = 'You lost !!'
        elif (player.upper() == 'PAPER' and rand_player == 'PAPER') or\
        (player.upper() == 'ROCK' and rand_player == 'ROCK') or\
        (player.upper() == 'SCISSOR' and rand_player == 'SCISSOR'):
            text = 'Draw'
        else:
            text = 'You entered a wrong option.'
        Result_Popup_Window(self.window, text, self.start_label, self.example_entry)
    

    def who_is_the_winner(self, player):
        """ This funciton sets the random value of the other player and call the function that finds the winner """

        rand_player = self.rps[rd.randint(0, 2)]
        self.find_the_winner(player, rand_player)
        self.example_entry.configure(state = 'normal')
        self.example_entry.delete(0, END)
        self.example_entry.insert(0, rand_player)

    def runApp(self):
        """ This function starts the app """

        self.label_cmp.grid(row = 1, column = 0)
        self.first_label.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 15, sticky = W+E)
        self.example_entry.grid(row = 2, column = 0, columnspan = 3, pady = 5, ipadx = 5, ipady = 5)
        self.player_label.grid(row = 4, column = 0)
        self.player_entry.grid(row = 5, column = 0, columnspan = 3, pady = 5, ipadx = 5, ipady = 5)
        self.start_label.grid(row = 3, column = 0, columnspan = 3, padx = 20, pady = 15, ipadx = 10, ipady = 10)
        self.frame.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
        self.frame_2.grid(row = 1, column = 0)
        self.exit_button.grid(row = 0, column = 1, ipadx = 5, ipady = 5)
        self.window.mainloop()
    

    def exitApp(self):
        """ Exit the application """

        self.window.destroy()


# This class is for the result window
class Result_Popup_Window():

    def __init__(self, master_window, text, start, entry):
        # Setting all the components of the second window
        self.start = start
        self.text = text
        self.entry = entry
        self.master_window = master_window
        self.child = Toplevel(master_window)
        self.child.geometry('200x100')
        self.child.resizable(0, 0)
        self.child.configure(bg = '#00FA9A')
        self.label = Label(self.child, text = self.text, font = ('Courier New', 23), bg = '#00FA9A', fg = '#2a3132')
        self.label.grid(row = 0, column = 0, ipady = 5, ipadx = 5, sticky = E+W)
        self.exit_button = Button(self.child, text = 'Exit', command = self.exit_child_window, fg = '#00FA9A', bg = '#2a3132', activeforeground = '#00FA9A', activebackground = '#2a3132')
        self.exit_button.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 10, ipady = 10)

    def exit_child_window(self):
        """ Delete the entry label of computer choice and, Exit the second window """

        self.entry.delete(0, END)
        self.start.configure(state = 'normal')
        self.child.destroy()


if __name__ == '__main__':
    app = Rps_App()
    app.runApp()