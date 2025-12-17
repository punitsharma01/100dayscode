from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(width=600, height=400)
window.config(padx=40, pady=24, bg=YELLOW)
# canvas
canvas = Canvas(width=360, height=280, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(180, 140, image=tomato_img)
canvas.create_text(180, 170, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg="green", bg=YELLOW)
timer_label.config(font=(FONT_NAME, 24, "bold"))
timer_label.grid(row=0, column=1)
start_button = Button(text="Start", fg="green")
start_button.config(font=(FONT_NAME, 24, "bold"))
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", fg="green")
reset_button.config(font=(FONT_NAME, 24, "bold"))
reset_button.grid(row=2, column=2)

check_label = Label(text="✓", fg="green", bg=YELLOW)
check_label.config(font=(FONT_NAME, 24, "bold"))
check_label.grid(row=3, column=1)


window.mainloop()
