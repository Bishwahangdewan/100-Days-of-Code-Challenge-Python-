import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

angle = [0, 90, 180, 270]
turtle.colormode(255)
tim.pensize(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_value = (r, g, b)
    return color_value


for i in range(200):
    tim.forward(20)
    tim.color(random_color())
    tim.setheading(random.choice(angle))

screen.exitonclick()
