#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program counts snow


import matplotlib.pyplot as plt
import numpy as np


picture = input('Enter file name:')
ca = plt.imread(picture)   
countSnow = 0
t = 0.8

#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)
