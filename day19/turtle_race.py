import math
from turtle import Turtle, Screen
import random

screen = Screen()

screen_width = 600
screen_height = 400

screen.setup(width=screen_width, height=screen_height, )
user_choice = screen.textinput("Make your bet", prompt="Enter your color to bet on: ")

color_list = ["red", "green", "blue", "yellow", "brown", "magenta", "pink"]

all_turtle_objects = []
for item in color_list:
    tim = Turtle(shape="turtle")
    tim.color(item)
    all_turtle_objects.append(tim)


y_pos, margin = screen_height / len(all_turtle_objects), 40
for i in range(-math.ceil(len(all_turtle_objects)/2), int(len(all_turtle_objects)/2)):
    all_turtle_objects[i].penup()
    all_turtle_objects[i].goto(x=-int(screen_width/2 - margin/2), y=(i * y_pos + margin))

race_on = True
if user_choice not in color_list:
    print("Your chosen bet is not available currently! Try Another !")
    race_on = False

while race_on:
    for t in all_turtle_objects:
        random_steps = random.randint(0, 10)
        t.forward(random_steps)
        if t.xcor() > screen_width/2 - margin:
            race_on = False
            winning_color = t.pencolor()
            if winning_color == user_choice:
                print(f"You WON!! The winner of the race is: {winning_color}")
            else:
                print(f"You Lost! The winner of the race is: {winning_color}")

screen.exitonclick()
