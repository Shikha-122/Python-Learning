#Example 1 : Create/ writing a file

#Approach 1
file= open('C:\\Users\\prai3\\Desktop\\myfile.txt', 'w')
file.write('Welcome to python \n File Handing')
file.close()

#Approach 2 : using with

with open('C:\\Users\\prai3\\Desktop\\myfile.txt', 'w') as file:
    file.write('Welcome to python \n Lets learn File Handing')
    file.close()

#Example 2: Appending the file

file= open('C:\\Users\\prai3\\Desktop\\myfile.txt', 'a')
file.write(' \n This line is appended...')
file.close()

# Example 3: Reading data from text file

#read() - read entire data
#readline() --read single line
#readLines() --read all the lines in to list format

file= open('C:\\Users\\prai3\\Desktop\\myfile.txt', 'r')
# content= file.read()
# content= file.readline()
content= file.readlines()
print(content)
file.close()

#Example 4: Rename the file
import os
os.rename('C:\\Users\\prai3\\Desktop\\myfile1.txt', 'C:\\Users\\prai3\\Desktop\\pythonmyfile.txt')
print('File renamed...')

#Example 5 : Delete the file

import os

file='C:\\Users\\prai3\\Desktop\\pythonmyfile.txt'

if os.path.exists(file):
    os.remove(file)
else:
    print('File does not exist')

# Example 6 : Creating a directory

import os
os.mkdir('C:\\Users\\prai3\\Desktop\\mydir')
print('Directory created')

#Example 7 Check the directory exist or not

import os
mydir= 'C:\\Users\\prai3\\Desktop\\mydir'

if os.path.exists(mydir):
    print('Directory exists...')

else:
    print('Directory doesnot exist...')

#Example 8: Rename the directory
import os

os.rename('C:\\Users\\prai3\\Desktop\\mydir1','C:\\Users\\prai3\\Desktop\\mydir')
print('Directory renamed...')

#Example 9: remove the directory

import os
os.rmdir('C:\\Users\\prai3\\Desktop\\mydir') # if folder/directory is empty
print('Directory removed')

#Example 10: Remove the directory with files
#  if the folder /directory contains files
import os
import shutil
shutil.rmtree('C:\\Users\\prai3\\Desktop\\mydir')

#Example 11: get the current working directory

import os

print(os.getcwd()) #returns current working directory

