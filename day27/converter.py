from tkinter import *

window = Tk()

window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)
label = Label(text="Converter app", font=("Arial", 18))
label.grid(row=0, column=1)

mile_entry = Entry(width=10)
input_value = mile_entry.get()
mile_entry.grid(row=2, column=0)
mile_label = Label(text="Miles", font=("Arial", 10))
mile_label.grid(row=3, column=0)

km_label = Label(text="0", font=("Arial", 18))
km_label.grid(row=2, column=2)
km_label_text = Label(text="Kilometers", font=("Arial", 10))
km_label_text.grid(row=3, column=2)


def calculate_kms():
    miles = mile_entry.get()
    kilometers = int(miles) * 1.609
    km_label.config(text=round(kilometers, 2))


button = Button(text="Calculate", command=calculate_kms)
button.grid(row=4, column=1)

window.mainloop()
