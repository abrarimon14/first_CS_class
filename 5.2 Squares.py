#Abrar Faiaz Imon
#Abrar.Imon14@myhunter.cuny.edu
#This program will crease a spiral of squares

import turtle

tess = turtle.Turtle()
length = 25


for i in range(100):
    tess.right(5)
    length = 1.02*length
    for j in range(4):
        tess.forward(length)
        tess.right(90)
    
