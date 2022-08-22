#Abrar Faiaz Imon
#Abrar.Imon14@myhunter.cuny.edu
#This program changes an image to cyan

import matplotlib.pyplot as plt
import numpy as np

img = plt.imread(input("Enter name of the input file:"))
cyanized = input("Enter name of the output file:")
img2 = img.copy()
img2[:,:,0] = 0

plt.imsave(cyanized, img2)






