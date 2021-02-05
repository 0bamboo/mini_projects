from tkinter import *
import random as  rd

from tkinter import *

# THE INITIALIZING OF THE WINDOW
window = Tk()
window.title('NOTHING TO SEE HERE')

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

# # THIS THE TYPES OF BORDER EFFECTS

# for relief_name, relief in border_effects.items():
#     # You use the releif option for setting the border type
#     frame = Frame(master = window, relief = relief, borderwidth = 5)
#     # Use the side var for setting the path of frames vertical or horizontal 
#     # Use the fill var for setting the path of responsivity use the option both with the option expand set to true 
#     # for setting the frame to be responsive in all directions
#     frame.pack(side = RIGHT, fill = BOTH, expand = True)
#     label =  Label(master = frame, text = relief_name)
#     label.pack()

# frame_pl = Frame(master = window, width = 150, height = 100)
# label_with_placemethod = Label(text = 'Hello from (11, 45)', bg = 'blue', fg = 'grey')

# # The method place is for setting the place of the label , but it's not responsive ....
# label_with_placemethod.place(x = 11, y = 45)
# frame_pl.pack()

# The method grid ()
# for i in range(4):
#     window.columnconfigure(i, weight = 10, minsize = 100)
#     window.rowconfigure(i, weight = 10, minsize = 80)
#     for j in range(4):
#         frame_grid = Frame(
#             master = window,
#             relief = RAISED,
#             borderwidth = 3
#         )
#         frame_grid.grid(row = i, column = j, padx = 2, pady = 2)
#         label = Label(master = frame_grid, text = f'row {i}, column {j}')
#         label.pack(padx = 15, pady = 15)

# window.columnconfigure(0, minsize = 100)
# window.rowconfigure([3, 3], minsize = 100)
# label_1 = Label(text = 'A', relief = SUNKEN)
# label_1.grid(row = 0, column = 0, padx = 3, pady = 4)
# label_2 = Label(text = 'B', relief = SUNKEN)
# label_2.grid(row = 1, column = 1, padx = 3, pady = 4)

# # ********* CREATE AN ADDRESS ENTRY FORM

# f_ad_form = Frame(relief = SUNKEN, borderwidth = 3)
# f_ad_form.pack()
# f_button = Frame(relief = FLAT)
# f_button.pack()
# # FOR THE LABEL AND ENTRY OF THE FIRST NAME 
# label_first_name = Label(master = f_ad_form,  text = 'First Name :')
# entry_first_name = Entry(master = f_ad_form, width = 50)

# label_first_name.grid(row = 0, column = 0, sticky = 'e')
# entry_first_name.grid(row = 0, column = 1)

# # FOR THE LABEL AND ENTRY OF THE LAST NAME 
# label_last_name = Label(master = f_ad_form, text = 'Last Name :')
# entry_last_name = Entry(master = f_ad_form, width = 50)

# label_last_name.grid(row = 1, column = 0, sticky = 'e')
# entry_last_name.grid(row = 1, column = 1)

# label_gmail = Label(master = f_ad_form, text = 'Gmail :')
# entry_gmail = Entry(master = f_ad_form, width = 50)

# label_gmail.grid(row = 2, column = 0)
# entry_gmail.grid(row = 2, column = 1)

# label_phone = Label(master = f_ad_form, text = 'Phone Number :')
# entry_phone = Entry(master = f_ad_form, width = 50)

# label_phone.grid(row = 3, column = 0, sticky = 'e')
# entry_phone.grid(row = 3, column = 1)

# button_clear = Button(master = f_button, text = 'Clear')
# button_clear.grid(row = 0, column = 2)

# button_submit = Button(master = f_button, text = 'Submit')
# button_submit.grid(row = 0, column = 4)
# entry_value = StringVar()
# entry = Entry(window, bg = 'white', fg = 'red', textvariable = entry_value)
# if not entry_value:
#     print('Opss')
# else:
#     print(entry_value)
# entry.pack()

# Handling key press {
# def handle_key_press(event):
#     print(event.char)

# window.bind('<Key>', handle_key_press)
# # }

# # Handling Button Click {
# def handle_click(event):
#     print('YOU HEAT ME WITH LEFT BUTTON OF MOUSE !! YAMETE KUDASSAI :(')

# def handle_click_right(event):
#     print('YOU HEAT ME WITH RIGHT BUTTON OF MOUSE !! YAMETTEEEEEE ')

# def handle_click_middle(event):
#     print('YOU HEAT ME WITH THE MIDDLE BUTTON OF THE MOUSE ...')

# button = Button(text = 'Heat me!')
# button.bind('<Button-1>', handle_click)
# button.bind('<Button-2>', handle_click_right)
# button.bind('<Button-3>', handle_click_middle)
# button.pack()
# # } 

# # Counter application {
# def increase():
#     value = int(lbl_value['text'])
#     lbl_value['text'] = f'{value + 1}'


# def decrease():
#     value = int(lbl_value['text'])
#     lbl_value['text'] = f'{value - 1}'


# def reset(): 
#     lbl_value['text'] = '0'


# window.rowconfigure(0, minsize = 50, weight = 1)
# window.columnconfigure([0, 1, 2], minsize = 50, weight = 1)

# btn_decrease = Button(master = window, text = '-', command = decrease, background = 'Black', fg = 'DarkTurquoise')
# btn_decrease.grid(row = 0, column = 0, sticky = 'nsew')

# lbl_value = Label(master = window, text = '0', background = 'Black', foreground = 'DarkTurquoise')
# lbl_value.grid(row = 0, column = 1, sticky = 'nsew')

# btn_increase = Button(master = window, text = '+', command = increase, background = 'Black', fg = 'DarkTurquoise')
# btn_increase.grid(row = 0, column = 2, sticky = 'nsew')

# btn_reset = Button(master = window, text = 'Reset', bg = 'red',command = reset)
# btn_reset.grid(row = 1, column = 1, sticky = 'nsew')

# # }

# Program that simulates rolling six-sided die {
def roll():
    lbl_roll['text'] = f'{rd.randrange(1, 7)}'

window.rowconfigure([0, 1], minsize = 50, weight = 1)
window.columnconfigure(0, minsize = 100, weight = 1)

btn_roll = Button(master = window, text = 'Roll', command = roll, relief = SUNKEN)
btn_roll.grid(row = 0, column = 0, sticky = 'nsew')

random_die = f'{rd.randrange(1, 7)}'
lbl_roll = Label(master = window, text = random_die, )
lbl_roll.grid(row = 1, column = 0)

window.mainloop()