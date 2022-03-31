import tkinter as tk
from tkinter import ttk


# root window
from tkinter import *

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Airwire GUI')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider current value
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())

# label for the slider
slider_label = ttk.Label(
    root,
    text='Volume:'
)

slider_label.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
)

slider.grid(
    column=1,
    row=0,
    sticky='we'
)

# current value label
current_value_label = ttk.Label(
    root,
    text='Current Value:'
)

current_value_label.grid(
    row=1,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label = ttk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=2,
    columnspan=2,
    sticky='n'
)

# Mute button
# create button, link it to clickMuteButton()
muteButton = Button(root, text='Mute', fg = 'Red')

# place button at (130,100)
muteButton.place(x=130, y=100)

# Confirm button
# create button, link it to clickConfirmButton()
muteButton = Button(root, text='Confirm', fg = 'Green')

# place button at (130,150)
muteButton.place(x=125, y=150)



root.mainloop()
