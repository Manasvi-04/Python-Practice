from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.ht()
        self.l_score=0
        self.r_score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-80, 250)
        self.write(f"Score:{self.l_score}", align="center", font=("courier", 20, "normal"))
        self.goto(80, 250)
        self.write(f"Score:{self.r_score}", align="center", font=("courier", 20, "normal"))

    def new_score_l(self):
        self.l_score += 1
        self.update_score()

    def new_score_r(self):
        self.r_score += 1
        self.update_score()