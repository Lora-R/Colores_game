import random
from tkinter import *
import time
from threading import *
from tkinter import messagebox

counter = 0
colours = {'Red': 'Rojo', 'Blue': 'Azul', 'Green': 'Verde', 'Pink': 'Rosa', 'Black': 'Negro',
           'Yellow': 'Amarillo', 'Orange': 'Naranja', 'White': 'Blanco', 'Purple': 'Purpura', 'Brown': 'Marron'}

points = 0
color_written = ""
values_list = []

def popup_points_end():
    global pop
    # pop window to show how many points u have for this game
    pop = Toplevel(tk)
    pop.title("Message")
    pop.config(bg="lavender")
    w = 190
    h = 80
    screen_w = pop.winfo_screenwidth()
    screen_h = pop.winfo_screenheight()
    x = (screen_w / 2) - (w / 2)
    y = (screen_h / 2) - (h / 2)

    pop.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
    label_total_points = Label(pop, text=f"Total Points: {points}", font=("Colibri", 16))
    label_total_points.grid(column=1, row=1, pady=20, padx=20)
    time.sleep(5)
    tk.quit()

def timer():
    # u have 50 sec to play the game
    sec = 50
    time_text = Label(tk, text=f"Time: {str(sec)}", font=("Colibri", 15))
    time_text.grid(column=0, row=8, pady=10, padx=150)
    while sec:
        sec -= 1
        time_text.config(text=f"Time: {str(sec)}")
        time.sleep(1)
    popup_points_end()

def start_game():
    # checking if the game have started and starting the time
    if counter == 0:
        t1 = Thread(target=timer)
        t1.start()

    # making a list from the keys of 'colours' dict
    keys = colours.keys()
    keys_list = list(keys)

    # shuffling the keys list
    random.shuffle(keys_list)
    # new dict
    d2 = {}
    for key in keys_list:
        d2[key] = colours[key]

    # list from the new dict /changing the words and colors/
    values = d2.values()
    values_list = list(values)
    keys = d2.keys()
    keys_list = list(keys)

    background = keys_list[1]
    # visualization of the different word and color
    label_color.config(fg=str(background), text=str(keys_list[0]))
    enter_data(values_list)

def enter_data(values_list):
    global counter
    counter += 1
    # entry data, box to fill ur answer
    entry = Entry(tk, justify="center")
    # by clicking 'Enter' u switch the word/color/ and check if ur answer is correct
    tk.bind('<Return>',
            lambda event, e=entry, v=values_list: color_check(e, v))

    entry.grid(column=0, row=5, pady=20, padx=100)
    # holding the cursor into the empty entry box all the time
    entry.focus_set()

def color_check(entry, values_list):
    global points
    global counter

    color_written = entry.get()
    # print(values_list[1])
    # comparing ur answer with the correct one
    if color_written.lower() == str(values_list[1]).lower():
        # if ur answer is correct u receive 1 point
        points += 1
        # and visualization of the points u have
        l_points = Label(tk, text=f"Points: {points}")
        l_points.grid(column=0, row=6, pady=10, padx=150)

    entry.delete(0, END)
    start_game()


# main visualization
tk = Tk()
tk.title("Color game")

w = 500
h = 500
screen_w = tk.winfo_screenwidth()
screen_h = tk.winfo_screenheight()
x = (screen_w / 2) - (w / 2)
y = (screen_h / 2) - (h / 2)
tk.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

# explination of the game, what are the rules and how to play
lbl = Label(tk, text="Type in the colour \n"
                     "of the word you see in spanish, \n"
                     "not the word text!", font=("Colibri", 16))
lbl.grid(column=0, row=1, pady=15, padx=100)

# label for the words, which color u need to write is spanish
label_color = Label(tk, font=('Colibri', 60))
label_color.grid(column=0, row=3, pady=15, padx=100)

# calling the function to start the game
start_game()

# loop to keep the window visible
tk.mainloop()
