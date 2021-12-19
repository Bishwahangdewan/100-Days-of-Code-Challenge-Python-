from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=500, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
pos=-150

for color in colors:
    pos += 50
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=-230, y=pos)


screen.exitonclick()
