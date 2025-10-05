from turtle import Turtle
import random

SCREEN_WID, SCREEN_HIG = 600, 600


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-int(SCREEN_WID/2) + 20, int(SCREEN_WID/2) - 40)
        random_y = random.randint(-int(SCREEN_WID/2) + 40, int(SCREEN_WID/2) - 40)

        self.goto(random_x, random_y)
