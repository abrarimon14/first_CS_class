#Abrar Faiaz Imon
#Abrar.imon14@myhunter.cuny.edu
#This program creates a t-logo

import matplotlib.pyplot as plt
import numpy as np
logoimg = np.ones((30,30,3))

logoimg[:,10:20,0] = 0
logoimg[:,10:20,2] = 0

logoimg[0:10,:,0] = 0
logoimg[0:10,:,2] = 0

plt.imsave('logo.png', logoimg)
plt.imshow(logoimg)
plt.show()
