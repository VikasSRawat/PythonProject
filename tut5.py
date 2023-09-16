# map function returns an iterable result of the function and the iterable element passed to it i.e., this will make it so that the map function executes the function passed into it automatically without making a for loop for the iterable element
def square(num):
    return num*num


l1=list(range(1,11))

# print(map(square,l1)) This will return the address of the map itself

print(list(map(square,l1))) # Will return the answer in the form of a list

def splicer(name):
    if len(name)%2!=0:
        return name
    else :
        return name[0]

names=['vikas','even','john','god']
result=map(splicer,names)
# we can also iterate through the result directly 
# for i in result : 
#     print(i,end=', ')
# print(' ')
print(list(result))
# Note map itself is calling and executing the function hence no parenthesis is passed with the fucntion name
# map will iterate through all the elements of the given iterable items and perform the fucntion passed to it.


def check_even(num):
    return num%2==0

# map will iterate through all elements of l1 and hence it will pass it to that fucntion
print(list(map(check_even,l1)))

# to avoid traversing through all the elements of the list and pass only those elements which are actually required by the function , we will use filter

print(list(filter(check_even,l1))) # Hence only those numbers are passed to it which are even(required by the function)



# lamda functions are used to make functions shorter and hence it will make it easier

result= lambda num:num**2
print(result(69))

# WE CAN ALSO USE THESE LAMBDA FUNCTIONS INSIDE maps and filter functions


print(list(map(lambda num:num**2,l1)))
print(list(filter(lambda num:num%2==0,l1)))


name='random'
def func():
    # name='yoo'
    print(name)
    def greet():
        name='jojo'
        print(name)
    greet()

# python searches for its variable from the local scope and then its gloabl scope 


# Global changes the value of x outside the function scope
x=20
def outter_func():
    print(f'local value of x is {x}')
    def inner_func():
        global x
        x='new value'
        print(f'i just locally changed global x to {x}')
    inner_func()

outter_func()
print(x)

l1='abcdefghijklmnopqrstuvwxyz'

s='the quick brown fox jumps over the lazy dog'
s1='dog'

def check(s):
    for i in l1:
        if i in s:
            pass
        else :
            return False
    return True        


print(check(s))
print(check(s1)) 


