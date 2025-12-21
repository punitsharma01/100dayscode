from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("K-Vault Password Manager")
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
window.config(width=400, height=400)
window.config(padx=40, pady=40)

# canvas
canvas = Canvas(width=360, height=280, bg=YELLOW, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(180, 140, image=logo_image)

canvas.grid(row=1, column=1)


window.mainloop()
