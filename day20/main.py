import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=500)
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
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        is_game_on = False
        scoreboard.game_over()


screen.exitonclick()







screen.exitonclick()
