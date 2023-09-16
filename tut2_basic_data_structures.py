
#########################################################################List###################################################################


# lists are like array but are heterogenous in nature 
my_list=[1,2,3,'vikas','god',23.433]
print(my_list)

my_list[2]=69# They are also mutbale in nature and can access any individual list items using the indexing from both sides negative and positive
print(my_list)

my_list.append('lol')#appends an element to the end of list . cannot specify any other position
print(my_list)

var=my_list.pop()#pops the last element by default
print(var)
print(my_list)

var=my_list.pop(0)#pops the last element specified by the index passed
print(var)
print(my_list)


char_list=['a','v','m','g','f']
print(char_list)
new_list=char_list.sort()
print(new_list)#This will print none as sort is an inplace algorithm hence it will directly change char_list directly
print(char_list)# This will be sorted as it has been sorted above already
#similarly for reverse it will follow the same principle

random_list=[1,23,'vikas','h',34/5]
# random_list.sort() This will cause an error due to the fact the items in the list are of different datatypes
random_list.reverse()# This will work normally
print(random_list)

####################################################################dictionary##################################################################


# Dictionaries in python are like lists but with key-value pairs 
# hence we can call a specific value with their unique key directly 
# Dictionaries are also mutable i.e., the values of keys are mutable and are also heterogenous in nature
my_dict={'apple':40.23,'oranges': 124.2,'banana':34.2,404:'hello'}
print(my_dict)
print(my_dict['oranges'])
print(my_dict[404])

my_dict['banana']=69.9
print(my_dict)


# We can also have nested dictinaries and lists inside a dictionary

new_dict={1: 'hello',2:['vikas','singh',69],3:{'insidek1': 'value'}}

print(new_dict)

# Accessing individual elements inside the nested list and dictionaries
var=new_dict[2][1].upper()
print(var)
new_dict[2][1]=var
print(new_dict)
var=new_dict[3]['insidek1']
print(var)

new_dict[3]['insidek2']='new value'# inserting new value into the nested dictionary
print(new_dict)
print(new_dict.keys())#returns all the individual keys in the form of tupple
print(new_dict.values())#returns all the values in the form of tupple
print(new_dict.items())#returns the index-value pairs in the form of tupples

del new_dict[1]# Removes the key-value pair of key 1
print(new_dict)
# .pop() is a method that will pop the key-value pair specified key


#########################################################################Tuples#################################################################



#Tuples are also similar to lists but are immutable in nature 

t=(1,2,4)
print(t)
# t[0]='vikas'
t=('vikas',334,34.893)
print(t)
t=('a','a','b','c')
print(t.count('a'))
print(t.index('a'))#returns the index of the first occurence of the character 'a'



########################################################################Sets####################################################################


#set is a unique data structures which only stores unique values i.e., they have no duplicate values
# They are enclosed in curly braces
my_set=set()
my_set.add(1)
my_set.add(2)
my_set.add(2)
my_set.add('Vikas')
print(my_set)


l1=[1,2,'vikas','syth',89.5]
my_set=set(l1)
print(my_set)




#############################################################boolean############################################################################


print(type(True))
print(type(False))

print(1>3)
print('Boolean of this equation is',1==1)

print(1>2>3)
print(1<2<3) # chaining comparison operators
print(1>2<3)# All the comparions should be true in chaining comparion operators, it is similar to 'and' operator

print(not(1==1)) #  'not' operator is equal to ! i.e., it will return the opposite of the actual boolean



name='vikas singh rawat'
l3=[]
for letter in name : 
    l3.append(letter)
print(l3)

# we can easily shorten this to this

l4=[letter for letter in name]
print(l4)


l1=list(range(1,11))
l3=[num**2 for num in l1 if num%2==0] # insert the square of those numbers which are even
print(l3)

l3=[num*2 if num%2==0 else 'odd' for num in l1]# insert the number's double if it is even else insert the string 'odd'
print(l3)