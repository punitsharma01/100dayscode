from turtle import Turtle
SCREEN_WID, SCREEN_HIG = 800, 500
STARTING_POSITION = (0, -(SCREEN_HIG/2) + 20)
MOVE_DISTANCE = 10
FINISH_LINE_Y = SCREEN_HIG/2 - 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self) -> bool:
        return True if self.ycor() > FINISH_LINE_Y else False

    def go_to_start(self):
        self.goto(STARTING_POSITION)