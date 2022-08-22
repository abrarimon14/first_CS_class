#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program stamps turtles of a specified color.

num = input('Please enter a 6-digit Hexadecimal number:')
import turtle
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("#"+num)


for i in range(5):
    tess.stamp()
    tess.penup()
    tess.forward(50)
    tess.pendown()
