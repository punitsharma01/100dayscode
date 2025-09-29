import time
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=500)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

segments = []
for i in range(0, 3):
    tim = Turtle(shape="square")
    tim.color("white")
    tim.penup()
    tim.goto(i * 20.0, 0.0)
    segments.append(tim)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)









screen.exitonclick()
