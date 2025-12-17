from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    timer_label.config(text="TIMER", bg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if REPS % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", bg=GREEN)
    elif REPS == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", bg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", bg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        if REPS % 2 == 1:
            checks = math.ceil(REPS/2) * "✓"
            check_mark.config(text=checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(width=600, height=400)
window.config(padx=40, pady=24, bg=YELLOW)
# canvas
canvas = Canvas(width=360, height=280, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(180, 140, image=tomato_img)
timer_text = canvas.create_text(180, 170, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg="green", bg=YELLOW)
timer_label.config(font=(FONT_NAME, 24, "bold"))
timer_label.grid(row=0, column=1)
start_button = Button(text="Start", fg="green", command=start_timer)
start_button.config(font=(FONT_NAME, 24, "bold"))
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", fg="green",  command=reset_timer)
reset_button.config(font=(FONT_NAME, 24, "bold"))
reset_button.grid(row=2, column=2)

check_mark = Label(fg="green", bg=YELLOW)
check_mark.config(font=(FONT_NAME, 24, "bold"))
check_mark.grid(row=3, column=1)

window.mainloop()
