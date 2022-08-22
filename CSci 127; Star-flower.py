#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program creates a star-flower

import turtle
wn = turtle.Screen()
wn.bgcolor("cyan")

tess = turtle.Turtle()
tess.pencolor("red")
tess.shape("turtle")
tess.fillcolor("yellow")


for i in range(18):
    tess.forward(200)
    tess.left(140)
    tess.stamp()


