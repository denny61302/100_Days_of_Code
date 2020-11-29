from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=250)
        self.update()

    def add_point(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align = ALIGNMENT, font = FONT)
