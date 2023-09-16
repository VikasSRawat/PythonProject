from tkinter import PAGES


class myclass():# Creating a class using the keyword class
    pass

obj1= myclass()# creating an instance of that class
print(type(obj1))


class dog():
    species="mammal" # This is static for all the instances of this class ans
    def __init__(self,breed,name,spots) -> None:   #__init__(self,arg1,arg2,etc) is itself a special methos AKA constructor where breed over here is the arguement
        self.breed=breed    # self is similar to 'this' keyword i.e., self keyword is used to access the class attributes .
        self.spots=spots
        self.name=name
    # defining a normal method inside the class    
    def bark(self,number):# note self is always passed inside the method even if no arguements are passed during the method call
        print("my name is {} and the number is {}".format(self.name,number))
        
        
mydog= dog("Street","shibu",False)
# if there is a confusion about which attribute is for which arguement then we can specify the attribute for each arguement
# mydog=dos(breed="street",name="shibu",spots=False)
print(mydog.name)
print(mydog.breed)
print(mydog.spots)
print(mydog.species)
print(type(mydog))

newdog=dog("retriever","malt",False)
print(newdog.name)
print(newdog.breed)
print(newdog.spots)
print(newdog.species)

newdog.bark(69)
# newdog.bark()



class circle():
    pi=3.14 # static attribute-common for all instances
    def __init__(self,radius=1) -> None:
        self.radius=radius
    def circumference(self):
        print('The radius is ',2*self.pi*self.radius)
    def area(self):# we can also directly return the values from the method itself
        return self.pi*self.radius*self.radius
    

cobj=circle(7)

cobj.circumference()
print('The are of the circle is ',cobj.area())

newobj=circle(9)
newobj.circumference()
print('The area of the circle is ',newobj.area())


class animal():
    def __init__(self):
        print("Yo animal created")
    def run():
        print('I can run')
    def shit():
        print('I can shit')
        
class cat(animal):# cat is being derived from animal
    def __init__(self):
        animal.__init__(self)# calling the parent class constructor
        print('A cat created')
    def meow():
        print("I am meowing")
        

kitten=cat()
cat.meow()
cat.run() # calling parent class method 



class book():
    def __init__(self,name,author,pages) -> None:
        self.name=name
        self.author=author
        self.pages=pages
    def __str__(self) -> str:# creating userdefined functions for utility functions like print,length ,etc i.e., it will return usedefined values and prompts whern print or len is called
        return f"{self.name} by {self.author}"
    def __len__(self):
        return self.pages
    
    
b=book("Arthala","vivek oberai",345)
print(b)
print(len(b))
    
    