from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SCREEN_WID, SCREEN_HIG = 800, 500
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1) # 2x length means 2 * 20 = 40
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(- int(SCREEN_HIG/2) + 50, int(SCREEN_HIG/2) - 50)
            new_car.goto(SCREEN_WID/2 - 30, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT/2
