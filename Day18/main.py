from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract("image.jpg", 30)

print(len(colors))

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(5)
screen = Screen()
screen.colormode(255)

# for _ in range(15):
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()
#     turtle.forward(10)

# for i in range(5):
#     for j in range(i+3):
#         turtle.forward(100)
#         turtle.left(360/(i+3))
#     turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# for _ in range(100):
#     turtle.forward(50)
#     angle = random.randint(1, 360)
#     turtle.right(angle)
#     turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# time = 10
# angle = 360/time
# for i in range(time):
#     turtle.circle(50)
#     turtle.right(angle)
#     turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

turtle.penup()
turtle.hideturtle()

for i in range(10):
    for j in range(10):
        color = (colors[random.randint(4, 29)].rgb.r, colors[random.randint(4, 29)].rgb.g, colors[random.randint(4, 29)].rgb.b)
        turtle.dot(10, color)
        if j == 9:
            if i % 2 == 1:
                turtle.right(90)
            else:
                turtle.left(90)
        else:
            turtle.forward(20)
    if i % 2 == 1:
        turtle.forward(20)
        turtle.right(90)
    else:
        turtle.forward(20)
        turtle.left(90)

screen.exitonclick()