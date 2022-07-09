import turtle
from turtle import Turtle,Screen
from random import choice

max=Turtle()
screen = Screen()
turtle.colormode(255)

color_list= [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
             (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
             (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
             (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
             (65, 66, 56)]
max.ht()
max.penup()
max.setpos(-250,-250)
max.width(20)
n = -250
for _ in range(11):
    n += 50
    for _ in range(11):
        max.pendown()
        max.dot(20, choice(color_list))
        max.penup()
        max.forward(50)
    max.penup()
    max.setpos(-250, n)




screen.exitonclick()