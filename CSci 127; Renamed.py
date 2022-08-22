#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program creates star-flower

import turtle
wn = turtle.Screen()
wn.bgcolor("cyan")

turtle.pencolor("red")
turtle.shape("turtle")
turtle.fillcolor("yellow")

turtle.stamp()

for i in range(17):
    turtle.forward(200)
    turtle.left(140)
    turtle.stamp()
turtle.forward(200)
turtle.hideturtle()
