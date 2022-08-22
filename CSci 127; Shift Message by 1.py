#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program shifts message by 1

mess = input("enter a message here")
for i in mess:
    print(i, ord(i)+1, chr(ord(i)+1))
