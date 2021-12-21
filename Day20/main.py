# SNAKE GAME MAIN FILE
from turtle import Turtle, Screen
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    tim.goto(position)
    segments.append(tim)

gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()

        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(10)


screen.exitonclick()
