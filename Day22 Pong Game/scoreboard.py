from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=250)
        self.update()

    def add_point_right(self):
        self.r_score += 1
        self.update()

    def add_point_left(self):
        self.l_score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Left Score: {self.l_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"Right Score: {self.r_score}", False, align = ALIGNMENT, font = FONT)

