from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-120, 190)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(120, 190)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def add_l_score(self):
        self.l_score += 1
        self.score_update()

    def add_r_score(self):
        self.r_score += 1
        self.score_update()
