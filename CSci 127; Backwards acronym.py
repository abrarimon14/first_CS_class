#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program makes a backward aronym

mess = input("Enter a phrase:")
print("You phrase in capital letters:", mess.upper())
words = mess.upper().split( )

for i in range(len(words)-1,-1,-1):
    print(words[i][0], end="")



