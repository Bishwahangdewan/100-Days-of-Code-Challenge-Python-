import turtle
import random
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
heading = 0

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_value = (r, g, b)
    return color_value

for i in range(50):
    heading += 10
    tim.circle(40)
    tim.color(random_color())
    tim.setheading(heading)

screen.exitonclick()
