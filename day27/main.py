import tkinter

window = tkinter.Tk()

window.title("First GUI program")
window.minsize(width=500, height=300)
label = tkinter.Label(text="Welcome to Website", font=("Arial", 22))
label.pack()



window.mainloop()