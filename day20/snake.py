from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(i * 20.0, 0.0)
            self.segments.append(tim)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def turn_left(self):
        self.segments[0].setheading(180)

    def turn_right(self):
        self.segments[0].setheading(0)

    def turn_up(self):
        self.segments[0].setheading(90)

    def turn_down(self):
        self.segments[0].setheading(270)
