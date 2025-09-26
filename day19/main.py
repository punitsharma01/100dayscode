from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def turn_left():
    tim.left(45)


def turn_right():
    tim.right(45)


def clear_screen_on_key():
    screen.clear()
    tim.home()


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="c", fun=clear_screen_on_key)


screen.exitonclick()
