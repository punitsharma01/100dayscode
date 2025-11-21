import time
from turtle import Screen
from player import *
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
SCREEN_WID, SCREEN_HIG = 800, 600

screen = Screen()
screen.setup(width=SCREEN_WID, height=SCREEN_HIG)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

screen.exitonclick()
