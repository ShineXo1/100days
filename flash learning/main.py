#!/usr/bin/python
  # -*- coding: utf8 -*-
import random
from tkinter import *

import pandas
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# data = pandas.read_csv('data/500 fi-en.csv')
# to_learn = data.to_dict(orient='records')
try:
    with open('data/words_to_learn.csv', 'r', encoding='UTF-8') as f:
        df = pd.read_csv(f)
except FileNotFoundError:
    with open('data/500 fi-ru1.csv', 'r', encoding='UTF-8') as f:
        original_data = pd.read_csv(f)
        to_learn = original_data.to_dict(orient='records')
else:
    to_learn = df.to_dict(orient='records')



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='suomi', fill='black')
    canvas.itemconfig(card_word, text=(current_card["FI"]), fill='black')
    canvas.itemconfig(card_front_img, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='Русский', fill='white')
    canvas.itemconfig(card_word, text=(current_card['RU']), fill='white')
    canvas.itemconfig(card_front_img, image=back_image)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()
    

window = Tk()
window.title('Super Suomea Opiskelija')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
# creating buttons
v_image = PhotoImage(file='images/right.png')
v_button = Button(image=v_image, highlightthickness=0, command=is_known)
v_button.grid(row=1, column=1)
# creating button images
x_image = PhotoImage(file='images/wrong.png')
x_button = Button(image=x_image, highlightthickness=0, command=flip_card)
x_button.grid(row=1, column=0)
#creating front and back images
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
card_front_img = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

window.mainloop()
