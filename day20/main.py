import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=500)
screen.title("Snake Game")
screen.bgcolor("black")

for i in range(0, 3):
    tim = Turtle(shape="square")
    tim.color("white")
    tim.goto(i * 20.0, 0.0)








screen.exitonclick()
