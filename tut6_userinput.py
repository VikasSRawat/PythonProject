# from curses.ascii import isdigit

acceptable_range=range(0,10)
print(acceptable_range)
# Using a while to see if the element entered is a number in range from 0 to 10
def check():
    inrange=False
    choice='WRONG'
    while choice.isdigit()==False or inrange==False:
        choice=input('Enter a number between 1 and 10 : ')
        if choice.isdigit()==False:
            print('Wrong input')
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                inrange=True
            else:
                inrange=False
                print('Out of range number ')
    return int(choice)


# print(check()) #for the above function check 


l1=[0,1,2]
acceptable_range=[0,1,2]
def enter():
    choice=''
    s=''
    print(l1)
    prompt='Please enter a valid index'
    while choice.isdigit()==False:
        print('Enter the index position you want to replace it with : ')
        if choice.isdigit()==False:
            print(prompt)
        if int(choice) >3 or int(choice)<0:
            print(prompt)
    s=input('Enter the valid string : ')
    l1[choice]=s
def game():
    choice='y'
    while choice=='y' or choice=='Y':
        enter
        choice=0
        while choice.isalpha()==False:
            choice=input('Enter y/Y for yes \n Enter n/N for no : ')
            if choice.isalpha()==False :
                print('Please enter the correct symbols')
    print('Thank you for playing the game \n')

game