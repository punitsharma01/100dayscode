from tkinter import *

window = Tk()

window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50) # can config the elements
label = Label(text="Welcome to Converter app", font=("Arial", 18))
# label.pack()
# label.place(x=100, y=200) # pack, place and grid are the ways to place element in layout
label.grid(row=0, column=0)

label["text"] = "New Text"
label.config(text="Another New Text!")


def button_clicked():
    print("button clicked")
    label_text = label['text']
    text_to_write = "Button Clicked!" if label_text == "New Text!" else "New Text!"
    label.config(text=text_to_write)


def login_button_click():
    text_to_write = entry.get()
    label.config(text=text_to_write)


button = Button(text="Click Me!", command=button_clicked)
button.grid(row=0, column=1)
login_button = Button(text="Login!", command=login_button_click)
login_button.grid(row=1, column=1)

entry = Entry(width=10)
input_value = entry.get()
entry.grid(row=2, column=1)

window.mainloop()
