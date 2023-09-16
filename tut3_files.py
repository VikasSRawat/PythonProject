myfile=open('sample.txt') # acts like a file handle which is kind of a gateway or a path to access the file
str=myfile.read()# .read() reads the entire file as an entire string
print(str)

str=myfile.read()# after applying .read once , the cursor will reach the end of text in the file and hence it won't return anything if called again
print(str)


myfile.seek(0)# .seek() will change the cursor's position back to the specified character and hence it will read from there
str=myfile.read()
print(str)

print('\n\n')
myfile.seek(0)
str=myfile.readlines()# this will return the file content as a list of strings
print(str[0])


myfile.seek(10)
str=myfile.readline()# reads the current line of the file from where the pointer is situated at and then returns the pointer to its original position 
print(str)
print(str)

myfile.close()# closes the current file which we are working on


fhandle=open("C:\\Users\\vikas\\c programs\\record.txt") # we can fetch any file from the system using its address and \\(doube backslash)
print(fhandle.read())
fhandle.close()

with open('sample.txt') as fhandle:# This will open the file and close the file after the operation inside the indented blocks are performed
    contents=fhandle.read()

print(contents,'\n\n\n')


# Python has different modes from which we can open different files
# some of these modes are w-write , r-read, a-append,etc

with open('sample.txt',mode='r') as f:
    print(f.read())

# with open('sample.txt',mode='r') as f:
#     print(f.write('Hello this is the third line'))  this will give an error due to it being in read mode and we are trying to write into the file

with open('sample.txt',mode='a') as f:
    f.write('\nHello this is the next line')# This will append the line to the end of the file

with open('sample2.txt',mode='r') as f:
    print(f.read())

with open('sample2.txt',mode='w') as f:# This will erase whatever is there in the file mentioned i.e., overwrite the contents in it
    f.write('Hey this is a new file')

with open('sample2.txt',mode='r') as f:
    print(f.read())