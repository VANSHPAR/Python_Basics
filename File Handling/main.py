#open the file in read mode
file=open("File Handling/file.txt","r")

#way to read file

#using loop
'''
for line in file:
    print(line)
    '''

'''
print(file.read()) '''

#using statement
'''
with open("File Handling/file.txt","r") as file :
    data=file.read()
    print(data)
    '''

#read only first x number of chars
'''
with open("File Handling/file.txt","r") as file :
    data=file.read(18)
    print(data)
    '''

#for writing the file
'''
file=open("File Handling/file2.txt","w")
file.write("Hello World\n")
file.write("writing in file.txt")
file.close()
'''
'''
file=open("File Handling/file2.txt","a")
file.write("\nHello World\n")
file.write("appending in file.txt")
file.close()
'''


#code forappend/write to file using with
'''
with open("File Handling/file3.txt","w") as file:
    file.write("hello everyone")
    '''

import os
os.remove("File Handling/file3.txt")




