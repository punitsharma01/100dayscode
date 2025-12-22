from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website_value = website_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()
    with open("data.txt", mode="a") as file:
        details = f"{website_value} | {email_value} | {password_value}"
        file.write(details)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("K-Vault Password Manager")
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT = ("Arial", 12, "bold")
window.config(width=400, height=400)
window.config(padx=40, pady=40)

# canvas
canvas = Canvas(width=360, height=280, bg=YELLOW, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(180, 140, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", font=FONT)
website_label.grid(row=1, column=0)
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username", font=FONT)
email_label.grid(row=2, column=0)
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "myemail@example.com")

password_label = Label(text="Password", font=FONT)
password_label.grid(row=3, column=0)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate")
generate_password_button.config(bg=YELLOW, font=FONT)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save_details)
add_button.config(width=36, bg=GREEN, font=FONT)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
