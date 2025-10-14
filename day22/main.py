from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

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

ball = Ball()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    ball.move()

    # detect collision with ball
    if ball.ycor() > 230 or ball.ycor() < - 230:
        ball.bounce_y()

    # detect collision with right paddle
    if ((ball.distance(r_paddle) < 50 and ball.xcor() > 320) or
            (ball.distance(l_paddle) < 50 and ball.xcor() < -320)):
        ball.bounce_x()

    # detect missing the ball right paddle
    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()

    screen.update()


screen.exitonclick()
