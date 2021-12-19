from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()


def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def move_clockwise():
    head = tim.heading()
    tim.setheading(head - 10)

def move_counter():
    head = tim.heading()
    tim.setheading(head + 10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter)
screen.exitonclick()
