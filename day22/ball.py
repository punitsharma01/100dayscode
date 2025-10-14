from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x, new_y = self.xcor() + self.x_move, self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # multiply -1 to move ball in reverse once collision
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

