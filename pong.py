# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 14:36:09 2021

@author: mitch
"""
import turtle
  
# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
  
# Left paddle
l_pad = turtle.Turtle()
l_pad.speed(0)
l_pad.shape("square")
l_pad.color("black")
l_pad.shapesize(stretch_wid=6, stretch_len=2)
l_pad.penup()
l_pad.goto(-400, 0)
  
# Right paddle
r_pad = turtle.Turtle()
r_pad.speed(0)
r_pad.shape("square")
r_pad.color("black")
r_pad.shapesize(stretch_wid=6, stretch_len=2)
r_pad.penup()
r_pad.goto(400, 0)
  
# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5
  
# Initialize the score
left_player = 0
right_player = 0
  
# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Player 1: 0    Player 2: 0",
             align="center", font=("Courier", 24, "normal"))
  
# Functions to move paddle vertically
def paddleaup():
    y = l_pad.ycor()
    y += 20
    l_pad.sety(y)
  
def paddleadown():
    y = l_pad.ycor()
    y -= 20
    l_pad.sety(y)
  
def paddlebup():
    y = r_pad.ycor()
    y += 20
    r_pad.sety(y)
   
def paddlebdown():
    y = r_pad.ycor()
    y -= 20
    r_pad.sety(y)
  
# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
  
while True:
    sc.update()
  
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
  
    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
  
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
  
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "normal"))
  
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Player 1: {}    Player 2: {}".format(
                                 left_player, right_player), align="center",
                                 font=("Courier", 24, "normal"))
  
    # Paddle ball collision
    if (hit_ball.xcor() > 360 and
                        hit_ball.xcor() < 370 and
                        hit_ball.ycor() < r_pad.ycor()+40 and
                        hit_ball.ycor() > r_pad.ycor()-40):
        hit_ball.setx(360)
        hit_ball.dx*=-1
         
    if (hit_ball.xcor() < -360 and 
                       hit_ball.xcor() > -370 and 
                       hit_ball.ycor() < l_pad.ycor()+40 and 
                       hit_ball.ycor() > l_pad.ycor()-40):
        hit_ball.setx(-360)
        hit_ball.dx*=-1