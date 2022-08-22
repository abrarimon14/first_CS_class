#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This prrogram makes a turtle spiral

num = int(input('Enter number of stamps the turtle will print:'))

import turtle
tess = turtle.Turtle()
tess.shape('arrow')
tess.color('cyan')
tess.penup()
steps = 10
for i in range(num):
    tess.stamp()
    if i % 2 == 0:
        steps = steps + 3
    tess.forward(steps)
    tess.right(24)
