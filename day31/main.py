import random
from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_SMALL = ("Arial", 24, "italic")
FONT_LARGE = ("Arial", 40, "bold")

# ----------------------- Reading data  ----------------#
dataframe = pandas.read_csv("./data/french_words.csv")
french_words = dataframe.to_dict(orient="records")


def next_word():
    random_dict = random.choice(french_words)
    french = random_dict["French"]
    english = random_dict["English"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=f"{french}")


# ----------------------- UI Setup ----------------#
window = Tk()
window.title("Flash Card Learning")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=800, height=526, bg=YELLOW, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(412, 274, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(412, 150, text="", font=FONT_SMALL)
card_word = canvas.create_text(412, 320, text="", font=FONT_LARGE)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_word)
cross_button.grid(row=1, column=0)
right_image = PhotoImage(file="./images/right.png")
tick_button = Button(image=right_image, highlightthickness=0, command=next_word)
tick_button.grid(row=1, column=1)
next_word()

window.mainloop()
