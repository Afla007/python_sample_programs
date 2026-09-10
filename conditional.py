
if condition:
    code to be executed
elif condition:
    code to be executed
else:
    code to be executed
#============

num=int(input("Enter a number: "))
if num>=0:
    print("Positive number")
else:
    print("Negative number")
#============

vowelchecker=input("enter a character: ")
if vowelchecker in "aeiouAEIOU":
    print("Entered char is a vowel")
else:
    print("Entered char is a consonant")
#============

num=int(input("Enter a number: "))
if num%2==0:    
    print("Number is even")
else:
    print("Number is odd")
#==============

age=int(input("Enter your age: "))
if age<=13:
    print("Child")
elif age<18:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior Citizen")
   #=============

num=int(input("Enter a number: "))
if num>=0:
    if num%2==0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
else:
    print("Negative number")
#=============
    #check whether given no is 3 digit or not
   
num=int(input("Enter a number: "))

if num>=100 and num<=999:
    print("Its a 3 digit number")
else:
    print("Not a 3 digit number")
#=================
    #control statements:-for repeated checking,
    for and while loop,thet are called entry controller loops

    syntax:- for variable in sequence : 
    code to be executed

    #using range function(syntax):-
    for variable in range(start,stop,step):
        code to be executed
 
    #start:- default value is zero
    #stop:-number -1
    #step:-default value is 1 for +ve numbers, we have to give value for -ve numbers
     
     #syntax for while loop:-
     initialization while condition:
        code to be executed 
        updation
       
       #================
        
word=input("Enter a word: ")
for letter in word:
    print(letter)
    #==========

for item in [1,2,3,4,5]:
    print(item)    
#==========

for element in range(11):
    print(element)
 #=================
 
for element in range(5,15):
    print(element)
#=========

for element in range(10,26,5):
    print(element)
#====================

for item in range(17,3,-3):
    print(item)
#==========
multiple=int(input("Enter a number: "))
for item in range(1,11):
    print(item*multiple)
#=============
multiple=int(input("Enter a number: "))
for item in range(1,11):
   # print(multiple,"*",item,"=",item*multiple)
    print(f"{multiple} * {item} = {item*multiple}")
#========

value=1
iterations=int(input("Enter the number of iterations: "))
while value<=iterations:
    print(value)
    value+=1
 #===========
    

    
for item in range(11):
    
    if(item==5):
        print(item)
        break

       
year=int(input("Enter year: "))
if(year%4==0):
    print("Its a leap year")
else:
    print("Its not a leap year")


for i in range(9):
    if(i==2):
       pass
    print(i)
    
