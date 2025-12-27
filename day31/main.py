from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

# ----------------------- UI Setup ----------------#
window = Tk()
window.title("Flash Card Learning")
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_SMALL = ("Arial", 24, "italic")
FONT_LARGE = ("Arial", 40, "bold")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=800, height=526, bg=YELLOW, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(412, 274, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)
canvas.create_text(412, 150, text="English", font=FONT_SMALL)
canvas.create_text(412, 360, text="Hello", font=FONT_LARGE)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0)
cross_button.grid(row=1, column=0)
right_image = PhotoImage(file="./images/right.png")
tick_button = Button(image=right_image, highlightthickness=0)
tick_button.grid(row=1, column=1)

window.mainloop()
