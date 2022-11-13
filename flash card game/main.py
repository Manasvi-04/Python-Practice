BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
from pandas import DataFrame
import random

current_card = {}
data_dic = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_ori = pandas.read_csv("data/french_words.csv")
    data_dic = data_ori.to_dict(orient="records")
else:
    data_dic = data.to_dict(orient="records")


# -------------------------- ADDING TO WORDS LEARNED ---------------------------#
def words_learned():
    random_word()
    data_dic.remove(current_card)
    dl = DataFrame(data_dic)
    dl.to_csv("data/words_to_learn.csv", index=False)



# -------------------------- RANDOM WORD ---------------------------#

def flip_card(current_card):
    canvas.itemconfig(old_image, image=new_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

# -------------------------- RANDOM WORD ---------------------------#

def random_word():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    canvas.itemconfig(old_image, image=card_1)
    current_card = random.choice(data_dic)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card, current_card)


# -------------------------- UI ----------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card, current_card)

canvas = Canvas(width=800, height=526 , bg=BACKGROUND_COLOR, highlightthickness=0)
new_image = PhotoImage(file="images/card_back.png")
card_1 = PhotoImage(file="images/card_front.png")
old_image = canvas.create_image(400, 263, image=card_1)
language = canvas.create_text(400, 150, text="word", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

tick = PhotoImage(file="images/right.png")
right_button = Button(image=tick, highlightthickness=0, command=random_word)
right_button.grid(column=1, row=1)

cross = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross, highlightthickness=0, command=random_word)
wrong_button.grid(column=0, row=1)

random_word()
window.mainloop()