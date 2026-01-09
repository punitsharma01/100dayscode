import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_SMALL = ("Arial", 24, "italic")
FONT_LARGE = ("Arial", 40, "bold")

# ----------------------- Reading data  ----------------#
current_word = {}
words_to_learn = {}

try:
    dataframe = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data_file = pandas.read_csv("./data/french_words.csv")
    words_to_learn = original_data_file.to_dict(orient="records")
else:
    words_to_learn = dataframe.to_dict(orient="records")


def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_to_learn)
    french = current_word["French"]
    english = current_word["English"]
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{french}", fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill='#fff')
    canvas.itemconfig(card_word, text=current_word["English"],  fill='#fff')


def is_known():
    words_to_learn.remove(current_word)
    to_learn = pandas.DataFrame(words_to_learn)
    to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_word()

# ----------------------- UI Setup ----------------#
window = Tk()
window.title("Flash Card Learning")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526, bg=YELLOW, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(412, 274, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(412, 150, text="", font=FONT_SMALL)
card_word = canvas.create_text(412, 320, text="", font=FONT_LARGE)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_word)
cross_button.grid(row=1, column=0)
right_image = PhotoImage(file="./images/right.png")
tick_button = Button(image=right_image, highlightthickness=0, command=is_known)
tick_button.grid(row=1, column=1)
next_word()

window.mainloop()
