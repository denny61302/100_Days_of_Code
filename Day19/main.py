from turtle import Turtle, Screen
import random

colors = ["red", "yellow", "green", "blue", "black", "purple"]

turtles = []
for _ in range(6):
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")

if user_bet:
    is_race_on = True

index = 0
for turtle in turtles:
    turtle.penup()
    turtle.color(colors[index])
    turtle.goto(x=-230, y=-170 + index * 50)
    index += 1


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print("You win")
            else:
                print(f"You lose, the winner is {winner_color} turtle")
        turtle.forward(random.randint(0, 10))

# def forward():
#     turtle.forward(10)
#
#
# def backward():
#     turtle.backward(10)
#
#
# def clock():
#     turtle.right(5)
#
#
# def counter_clock():
#     turtle.left(5)
#
#
# def reset():
#     turtle.reset()
#
#
# screen.listen()
# screen.onkey(key="w", fun=forward)
# screen.onkey(key="s", fun=backward)
# screen.onkey(key="a", fun=counter_clock)
# screen.onkey(key="d", fun=clock)
# screen.onkey(key="c", fun=reset)

screen.exitonclick()