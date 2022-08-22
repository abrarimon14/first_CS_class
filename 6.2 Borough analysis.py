#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program analyzes boroughs

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
borough = input('Enter borough name:')
out = input('Enter output name:')
print('Min:', pop[borough].min())
print('Max:', pop[borough].max())
print('Mean:', pop[borough].mean())
print('Median:', pop[borough].median())
print('Standard Deviation:', pop[borough].std())

pop['Fraction'] = pop[borough]/pop['Total']

pop.plot(x='Year',y='Fraction')
fig = plt.gcf()
fig.savefig(out)
