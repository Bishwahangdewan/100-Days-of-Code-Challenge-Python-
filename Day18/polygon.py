from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()

for sides in range(3, 11):
    deg = 360 / sides

    for each in range(0, sides):
        timmy.right(deg)
        timmy.forward(50)

screen.exitonclick()
