from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.listen()

ball = Ball()
score = ScoreBoard()

line = Turtle()
line.ht()
line.width = 20
line.color("white")
line.penup()
line.goto(0, -400)
line.left(90)
for _ in range(0, 800):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

r_paddle = Paddle(370, 0)
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")


l_paddle = Paddle(-370, 0)
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

n=0.07
game_is_on = True
while game_is_on:
    time.sleep(n)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.boucne()

    if (ball.xcor() < -350 and ball.distance(l_paddle) < 50) or (ball.xcor() > 350 and ball.distance(r_paddle) < 50):
        ball.boucne2()
        n *= 0.9

    if ball.xcor() > 380:
        ball.restart()
        n = 0.07
        score.new_score_l()

    if ball.xcor() < -380:
        ball.restart()
        n = 0.07
        score.new_score_r()




screen.exitonclick()