#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program creates shades of green

import turtle
turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")
tess.backward(100)
for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(0,i,0)

tess.penup()
tess.forward(300)
tess.pendown()

for i in range(255,-5,-10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(0,i,0)
