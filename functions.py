''' fuction syntax:-
def function_name():
    code to be executed

#user defined function without parameters
def welcome():
    print("Welcome Afla")
welcome()

#with parameters
def greeting(username,userage):
    print(f"Welcome {username},you are {userage} years old")
greeting("Afla",21)

def addition(num1,num2):
    return num1+num2 # return is a keyword so no need for paranthesis
num1=int(input("Enter the First number: "))
num2=int(input("Enter the second number: "))

print(addition(num1,num2))# output il veranamengi  print kodkknm

#positional argument
def book_ticket(moviename,customername,seats,ticketprice):
    total_price=seats*ticketprice
    return f"{customername} booked {seats} tickets for {moviename}. Total amount: {total_price} "
    
print(book_ticket("bahubali","Alex",2,200))# only give arguments for the mentioned parameters@@@@@@@

#keyword argument
def customer_details(customername,customerage,city):
    print(f"customer name is {customername} and customer age is {customerage} and is from {city}")
#customer_details("Alex",22,"palayam")
customer_details(customerage=22,customername="Alex",city="Trivandrum") #here position or order of the parameters doesnt matter

# default arguments

def booking_status(customername="Alex",status="confirmed",screen="screen1"):
    print(f"Booking status of {customername} is {status} and the screen allocated is {screen} ")
booking_status()

booking_status("Alan")
booking_status("Tom","pending")
booking_status("abhi","pending","screen2")

#multiple arguments

def calculate_bill(*ticketprices):  # *args= more than 1 parameter value kodkkan,like single parameter but multiple values
    print(f"ticketprices : {ticketprices}")
calculate_bill(111,222,333,123,321) # **kwargs HOMEWORK

#built in function

print(len("Afla"))
print(sum([1,2,3,4,5]))
print(min([1,2,3,4,5]))
print(max([1,2,3,4,5]))
print(sorted([3,7,2,5,6]))
print(sorted([3,7,2,5,6],reverse=True))

#HW
def ticket_booking(**movie):
    print(movie)
ticket_booking(movie="Avatar",seats=2,ticketprice=250,city="palayam")

def ticket_booking(movie,**details):
    print(movie)
    print(details)
ticket_booking("Avatar",seats=2,ticketprice=250,city="palayam")


#Legb rule - local,enclose,global

def student_details():
    name="Afla"   #local variable
    print("Student name: ",name)
student_details()

#global variable - function nthe velil aanengilum access chyyan pattum

college_name="Mangalam College"
def display():
    print("College name: ",college_name)
display()
print("College name: ",college_name)    

#enclosing variable -has a outer and inner fnctn and variable is defined in the outer fnction and asked in the inner fnctn

def department():
    dptmnt_name="cse"
    def student():
        print("Department name: ",dptmnt_name)
    student()   # function call vilikkumbo nere thazhe indentation nokki chyyanm
department()


tax=50#global variable - variable outside fnctn
def shopping():
    discount=100 #enclosing variable - variable in outer fnctn
    def bill():
        amount=2500   # ithokke local variable aakum cause ithellm bill enna function nthe agath aan
        total_amount=amount-discount+tax
        print("Total amount: ",total_amount)
    bill()
shopping()


 #Recursive function - calls itself in the fnctn
def factorial(number):
    if number==1: # base case
        return 1
    else:      # recursive case
            return number*factorial(number-1)
num=int(input("Enter a number: "))
print(factorial(num))

 #working-
 6*factorial(5)
 6*5*factorial(4)
 6*5*4*factorial(3)
 6*5*4*3*factorial(2)
 6*5*4*3*2*1

 #lambda function-anonymous function :- lambda keyword use akki chyym
 #syntax:-lambda arguments:expression

def add(num1,num2):
    return num1+num2 
print(add(2,3))

add=lambda a,b:a+b
print(add(2,4))

square=lambda num:num*num
print(square(3))
'''


cube=lambda num:num**3
print(cube(3))

celsius_to_f=lambda c:(c*9/5)+32
print(celsius_to_f(100))

multiply=lambda a,b:a*b
print(multiply(8,8))

is_odd=lambda num:num%2!=0
print(is_odd(7))

smallest=lambda a,b,c:min(a,b,c)
print(smallest(8,7,2))

area=lambda l,b:l*b
print(area(110,128))


practise legb rule that is in the notes