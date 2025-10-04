import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=500)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()

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


screen.exitonclick()







screen.exitonclick()
