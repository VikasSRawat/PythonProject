# if else in python requires indentations and does not require any parenthesis to hold the query of the if else

from codecs import escape_encode
import imp
from unicodedata import name


a='vikas'
b='vikas'
c='Vikas'
if a==b:
    print('true')
else:
    print("false")


if a==c:
    print('True')
else:
    print('false')



var1='a'


age=69

if(age<18):
    print('underage')
elif(age<45):  # instead of else if  , it is elif in python
    print('middle aged')
else:
    print('ancient being')


#################################################################for loops in python############################################################


l1=[1,2,3,4,5,6,7]

for i in l1:
    print('hello ',i)

l1=[1,'vikas',23.5]  
for i in l1:
    print(i)


# Here i is the iterator of the list and i itself is the item or element in the list

t1=[('a','b'),('c','d'),('e','f')]

for i in t1:
    print(i)

# using individual items as an iterator 
for [a,b] in t1:
    print(a)
    print(b)


d1={'key1': 'vikas', 'key2':'singh','key3':'rawat'}
for key in d1:
    print(key)# printing the keys in a dictionary

for values in d1.values():
    print(values)# printing the values in a dictionary

for items in d1.items():
    print(items)# printing the items in a dictionary


##################################################################while loops in python#########################################################


i=0
while (i<10):
    print(f'The current value of i is {i}')
    i=i+1

# They are similar to for loops 


# break: Used for exiting the current closest loop
# continue: Used for going to top of the closes loop 
# pass: Does nothing at all 

i=0
while(i<10):
    if(i==8):
        break
    print(i,end=' ')
    i=i+1


l1=[1,2,3,34,4]
for i in l1:
    pass# normally loops should contain at least one line or statement(not a comment) hence pass can be used for empty for loops

print('')
s='vikas'
for i in s: 
    if i=='a':
        continue
    print(i,end=' ')

print('')
for i in range(10):# range is a predefined function where it will generate numbers from 0(by default) to n-1 
    print(i,end=' ')
print('')
# WE CAN ALSO GENERATE NUMBERS FROM A SPECIFIED STARTING POINT TO A SPECIFIC ENDING INDEX WITH A BREAK IN THE SERIES
for num in range(2,10,3):
    print(num,end=' ')

print('')
# We can also generate list and tupples from the range function
l1=list(range(1,20,2))
print(l1)

t1=tuple(range(21,40,2))
print(t1)


# Zipping lists together

l1=[1,2,3,45,6,8]
l2=['a','b','c','d','e']
l3=[0.1,0.2,0.3,0.4]

# print(zip(l1,l2,l3)) prints the zip code
for items in zip(l1,l2,l3):
    print(items)# prints tuples of all the individual items 

l1=list(zip(l1,l2)) # making a list of the zipped lists
print(l1)

t1=tuple(zip(l1,l2)) # Some wierd bullshit
print(t1)

# in keyword can be used to check if an item is present inside another data structures

var='vikas is a god'
print('vikas' in var)
print('dog 'in var)
print('vikas  'in var)# every single character matters in python 

l1=list(range(100,200,10))
print(max(l1))
print(min(l1))

# from random import shuffle
from random import *
l1=[1,2,3,4,5]
shuffle(l1)# shuffles the list randomly inorder 
print(l1)

print(randint(1,100))# generates a random integer between 1 and 100


var1=input('Enter a random number : ') # By default the input value will be taken as a string
print("The inputted number is a string : ",var1)
a=int(var1)
print(a,type(a))# we can change the type of input value using change_type() , ex: int(),float(),str()


# we can directly change the typeof of the input value while taking input value : change_type(input('prompt'))
var2=int(input('Enter the integer type : '))
print(var2,type(var2))



