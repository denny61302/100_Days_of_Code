from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
hit_the_wall = False
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect wall collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect paddle collisions
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect outside the wall
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_point_left()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_point_right()

    if scoreboard.r_score > 5 or scoreboard.l_score > 5:
        scoreboard.game_over()
        game_is_on = False






screen.exitonclick()