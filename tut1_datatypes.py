# Python datatypes are dynamic in nature i.e., different types of data can be stored inside one variable
from inspect import getmodule


a=35
print(a)
print(type(a))
a="vikas"
print(a)
print(type(a))
a=34.3
print(a)
print(type(a))

s="Hello world this is a god"
print(s[3:])#Prints from the index 3 till the end of the string
print(s[:3])#Prints from the start till (index specified)-1
print(s[-4:])#Prints from the negative index 4 till the end of the string
print(s[:-4])#prints from the start till the index before -4 i.e., -3

print(s[-5: 2])#prints till the -5 index
print(s[::3])#prints all the letters with interval of 3
print(s[::-1])#reverses the string


#  We cannot directly edit individual characters in strings in python as characters don't exist in python 
# ex:
name= 'mad'
# name[0]='d' THIS WILL CAUSE AN ERROR
print(name)
# instead we can do this 
newname='d'
newname=newname+name[1:]# concatenating newname which is initially d with the rest of the letters in name
print(newname)


num1=2
num2=9
print(num1+num2)#This will directly add the numbers as they both are integers
# we can also concatenate 2 strings contaning numbers
num1='2'
num2='9'
print(num1+num2)
letter='abc'
# print(letter+69) This will give an error as we cannot concatenate 2 different datatypes

var='Hello World'
print(var.upper())# .upper() returns the same string in all caps without affecting the real string
print(var.upper)# this will print that it is an inbuilt method of strings
print(var.lower())

var='This is an incredible task'
print(var.split())#This will split the string into a list on by dividing the string on each space(by default)
#But by mentioning a character python will split the string whenver that character is encountered
print(var.split('i'))

#.format will fill in the curly braces with the arguements specified
print('Hello my name is {} {} {}'.format('Singh','Vikas','Rawat'))#Note : the number of arguments should be equal to the number of curly braces or else an error occurs
# The order of which the curly braces will be filled in will be the same as the one specified in the arguement list
print('Hello my name is {v} {s} {r}'.format(s='Singh',v='Vikas',r='Rawat'))# although we can also specify the order using positional arguement such as v,s,r or even index numbers
print('Hello my name is {r} {r} {r}'.format(s='Singh',v='Vikas',r='Rawat'))# we can also repeat a value for all curly braces by specifying that values's index or positional arguement
# print('Hello my name is {} {} {}'.format(s='Singh',v='Vikas',r='Rawat')) This will cause an error as positional arguemnets are defined in the .format but not specified in the string plus we can not specify the index numbers if positional arguements are already defined

result=100/699
print(result)
print('result = {r:1.4f}'.format(r=result))# This will round off all the values after the 3rd digit after the decimal point
result=234.343254343
print('result = {r:12.4f}'.format(r=result))# This will just add extra white spaces before the result

name='vikas singh rawat'
print(f'hello my name is {name}')# This is known as formatted strings without the .format but if we remove f then instead of the value inside name, instead it will directly insert {name} as a string

age=21
print(f'Hello this is {name} and my age is {age}')#injecting multiple 
