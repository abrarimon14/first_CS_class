#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program shows volcanic elevations

import matplotlib.pyplot as plt
import pandas as pd

file = input('Enter file name:')
data = pd.read_csv(file)



groupeddata = data.groupby('Dominant Rock Type')
print(groupeddata['Elevation (Meters)'].mean())

Italy = data.groupby('Country').get_group('Italy')
Italyelevation = Italy['Elevation (Meters)']
print('The tallest Volcano in Italy is', Italyelevation.max(), 'meters high')
