from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [str(num) for num in range(0, 10)]
    symbols = ['!', '#', '@', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 3))]

    password_in_list = password_letters + password_numbers + password_symbols
    shuffle(password_in_list)
    password = "".join(password_in_list)
    # print(password)
    # populating password in the field
    password_entry.insert(0, password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    website_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) < 1 or len(password) < 2:
        messagebox.showinfo(
            title="Oops !!",
            message=f"Field Value(s) are Invalid, Try Again!!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title="Entered Details",
            message=f"Website: {website} \n"
                    f"Password: {password} \n"
                    f"Are you sure you want to save?"
        )
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    # reading old data
                    data = json.load(data_file)
                    # updating old data + new data
                    data.update(website_data)
            except FileNotFoundError:
                # print("file not found!")
                data = {}
                data.update(website_data)
            finally:
                with open("data.json", mode="w") as data_file:
                    # saving new data to file
                    json.dump(data, data_file, indent=4)

                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                    website_entry.focus()


# ------------------------- Search Function --------------------------- #
def search_details():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data = {key.lower(): value for key, value in data.items()}
            if website.lower() in data:
                email = data[website.lower()]["email"]
                password = data[website.lower()]["password"]
                messagebox.showinfo(
                    title=website,
                    message=f"Email: {email} \n"
                            f"Password: {password}"
                )
            else:
                messagebox.showinfo(
                    title="Error!",
                    message=f"Details for {website} Not found!"
                )
    except FileNotFoundError:
        messagebox.showinfo(
            title="Oops!",
            message=f"No Data Found!"
        )


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
website_entry = Entry(width=42)
website_entry.grid(row=1, column=1)
website_entry.focus()
search_button = Button(text="Search", command=search_details)
search_button.config(bg=GREEN, font=FONT)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username", font=FONT)
email_label.grid(row=2, column=0)
email_entry = Entry(width=42)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "myemail@example.com")

password_label = Label(text="Password", font=FONT)
password_label.grid(row=3, column=0)
password_entry = Entry(width=42)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.config(bg=YELLOW, font=FONT)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save_details)
add_button.config(width=36, bg=GREEN, font=FONT)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
