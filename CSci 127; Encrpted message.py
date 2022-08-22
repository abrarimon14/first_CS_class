#Abrar Faiaz Imon
#abrar.imon14@myhunter.cuny.edu
#This program creates an encrypted message

mess = input('Enter a word:')
EncryptedMessage = ""
for i in mess:
    offset = ord(i) - ord('A') + 13
    wrap = offset % 26
    newChar = chr(ord('A') + wrap)
    EncryptedMessage = EncryptedMessage + newChar

print('The encrypted message is:', EncryptedMessage)



