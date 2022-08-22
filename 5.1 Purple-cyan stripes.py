#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program creates purple and cyan stripes

import numpy as np
import matplotlib.pyplot as plt

size = int(input('Enter the size:'))
output = input('Enter output file:')
purplecyan = np.ones((size,size,3))

purplecyan[::2,:,1:2] = 0
purplecyan[1::2,:,0:1] = 0

plt.imsave(output, purplecyan)

