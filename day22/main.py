from turtle import Screen, Turtle
from paddle import Paddle

SCREEN_WID, SCREEN_HIG = 800, 500
screen = Screen()
screen.setup(width=SCREEN_WID, height=SCREEN_HIG)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((- 350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "s")
screen.onkey(l_paddle.go_down, "x")

is_game_on = True
while is_game_on:
    screen.update()


screen.exitonclick()
