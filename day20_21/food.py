from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        self.SCREEN_WID = 600
        self.SCREEN_HIG = 500
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-int(self.SCREEN_WID/2) + 20, int(self.SCREEN_WID/2) - 20)
        random_y = random.randint(-int(self.SCREEN_HIG/2) + 20, int(self.SCREEN_HIG/2) - 40)
        self.goto(random_x, random_y)

    def seperator_line(self):
        # Seperator line from scoreboard
        tim = Turtle("turtle")
        tim.color("white")
        tim.speed("fastest")
        tim.hideturtle()
        tim.penup()
        tim.goto(-self.SCREEN_WID / 2, self.SCREEN_HIG / 2 - 40)
        tim.pendown()
        tim.goto(self.SCREEN_WID / 2, self.SCREEN_HIG / 2 - 40)
        return None
