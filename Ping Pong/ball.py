from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()


    def create_ball(self):
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color("white")
        self.x = 10
        self.y = 10

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def boucne(self):
        self.y *= -1

    def boucne2(self):
        self.x *= -1

    def restart(self):
        self.goto(0, 0)
        self.x *= -1
        self.y *= -1




