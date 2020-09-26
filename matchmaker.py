import random
import time
from tkinter import Tk, Button, DISABLED


def show_symble(x, y):
    global first
    global previouseX, previouseY
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        previouseX = x
        previouseY = y
        first = False
    elif previouseX != x or previouseY != y:
        if buttons[previouseX, previouseY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previouseX, previouseY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[previouseX, previouseY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
        first = True


root = Tk()
root.title('Matchmaker')
root.resizable(width=False, height=False)

buttons = {}
first = True
previouseX = 0
previouseY = 0


button_symbols = {}

symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708', u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
           u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712', u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728']

random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x,
                        y=y: show_symble(x, y), width=3, height=3)
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()


root.mainloop()
