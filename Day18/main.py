import random
import turtle
from turtle import Turtle, Screen

color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171),
              (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105)]

tim = Turtle()
turtle.colormode(255)
screen = Screen()

for j in range(0, 10):
    for i in range(0, 10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.penup()
    tim.backward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.pendown()
    tim.setheading(0)


screen.exitonclick()
