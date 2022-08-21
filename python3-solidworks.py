width = input('Width: ')
length = input('Lenght: ')
height = input('Height: ')

#Open files to input variables
f = open("boss.txt", "w+")
#Wright to .txt file
#Place user input in .txt
f.write('width = '+width + '\n')
f.write('length = '+length + '\n')
f.write('height = '+height + '\n')

f.close()

#open and read the file after the appending:
f = open("boss.txt", "r")
print(f.read())
