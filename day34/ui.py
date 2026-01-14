from tkinter import *
THEME_COLOR = "#375362"
WIDTH, HEIGHT = 400, 600
class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=WIDTH, height=HEIGHT, padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0",
                                 bg=THEME_COLOR,
                                 fg="white",
                                 font=("Arial", 20)
                                 )
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 100,
                           text="Some text goes here",
                           font=("Arial", 20, "italic"),
                           fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.cross_image = PhotoImage(file="./images/false.png")
        false_button = Button(image=self.cross_image, highlightthickness=0, padx=20, pady=20)
        false_button.grid(row=2, column=0)
        self.tick_image = PhotoImage(file="./images/true.png")
        true_button = Button(image=self.tick_image, highlightthickness=0, padx=20, pady=20)
        true_button.grid(row=2, column=1)



        self.window.mainloop()
