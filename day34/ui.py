from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WIDTH, HEIGHT = 400, 600
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

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
                            width=280,
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
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)
