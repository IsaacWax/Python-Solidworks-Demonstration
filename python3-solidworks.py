import math
#Written by Isaac Wax as a simple demmo on how you can use Solidworks do equation driven modeling from a text file

#Open files to input variables
f = open('boss.txt', 'w+')

#User input
#Assign input values...
width = input('Width: ')
length = input('Lenght: ')
height = input('Height: ')

#Wright to .txt file
#Place user input in .txt
f.write('width = '+width + '\n')
f.write('width = '+length + '\n')
f.write('width = '+height + '\n')

#Close and save .txt
f.close()
