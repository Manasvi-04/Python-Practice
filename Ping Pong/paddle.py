from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, postion_x, postion_y):
        super().__init__()
        self.x = postion_x
        self.y = postion_y
        self.create_paddle()


    def create_paddle(self):
            self.shape("square")
            self.shapesize(stretch_len=1, stretch_wid=5)
            self.color("white")
            self.penup()
            self.goto(self.x, self.y)


    def up(self):
        self.goto(self.xcor(), self.ycor()+40)

    def down(self):
        self.goto(self.xcor(), self.ycor()-40)

