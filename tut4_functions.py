# result2=func(2,2)
# print(result2)
# The function has to be defined first before its called


def func(num1,num2,name):
    print(f'the name is {name}')
    return num1+num2

result1=func(49,11.5,'vikas')
print(result1)

# We can also have default values for parameters same as c,c++,java,etc.
# python does not support method overloading due to its dynamic nature
def func(n1,n2='vikas'):
    print(n2)
    return n1*9

print(func(2))
print(func(34,'john'))


def even_list(l1):
    l2=[]
    for i in l1:
        if i%2==0:
            l2.append(i)
        else : #overhere else is optional
            pass
    return l2


l1=list(range(1,50))
l=even_list(l1)
print(l1)


employees=[('a',200),('d',800),('c',400)]

def best_employee(emp):
    best=''
    workhours=0
    for e,w in emp:
        if(w>workhours):
            workhours=w
            best=e
    return (best,workhours)

result=best_employee(employees)
print(result)



# *args allows us to pass any amount of arguements while calling the function without expanding the arguement list
# args is just the arbitrary variable which is in the form of a tuple 
def myfunc(*args):
    print(args)
    return sum(args)*0.05

result=myfunc(1,2,3,4,5,6)
print(result)

# ** allows us to build key-value or key-word arguements i.e., it will return us a dictionary
def myfunc(**kwarg):
    if 'fruits' in kwarg:
        print('the fruit is : {}'.format(kwarg['fruits']))
    else:
        print('NO fruit is present here')
    print(kwarg)


myfunc(fruits = 'apple',name='god')


