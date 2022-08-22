#Abrar Faiaz Imon
#Abrar.Imon14@myhunter.cuny.edu
#This program creates shades red to green

import turtle
turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")
tess.backward(100)

for i in range(0,255,10):
    tess.forward(25)
    tess.pensize(i)
    tess.color(255-i,i,0)
