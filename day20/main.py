import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SCREEN_WID, SCREEN_HIG = 600, 500
screen = Screen()
screen.setup(width=SCREEN_WID, height=SCREEN_HIG)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.turn_up, key="Up")
screen.onkey(fun=snake.turn_down, key="Down")
screen.onkey(fun=snake.turn_right, key="Right")
screen.onkey(fun=snake.turn_left, key="Left")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()

    # Detect collision with wall
    if (snake.head.xcor() > SCREEN_WID/2 - 20 or
        snake.head.xcor() < -SCREEN_WID/2 or
        snake.head.ycor() > SCREEN_HIG/2 - 30 or
        snake.head.ycor() < -SCREEN_HIG/2):
        is_game_on = False
        scoreboard.game_over()


screen.exitonclick()







screen.exitonclick()
