                       '''operators
1.Arithmetic operators
2.Assignment operators
3.Logical 
4.Comparison
5.Bitwise
6.Membership
7.Identity
                      
print("Arithmethic operator")
price_per_phone=20000
quantity=5
total_price=price_per_phone*quantity
average_price=total_price/quantity
gst_added=200
final_price=total_price+gst_added
discount_amount=1000
final_price=final_price-discount_amount
no_of_persons=3
remaining_price=final_price%no_of_persons
floor_division=final_price//7 #to remove decimal part

print("price per phone: ",price_per_phone)
print("Quantity : ",quantity)
print("Total price of phone",total_price)
print("Average price : ",average_price)
print("Added gst of phone; ",gst_added)
print("Discount amount of phone : ",discount_amount)
print("Final price of phone ",final_price)
print("Floor division is: ",floor_division)
print("remaining price: ",remaining_price)
'''
#Assignment operator
'''
score=100
score+=50
score-=20
score*=5
print("you have scored: ",score)
'''
'''
#Logical operator 
AND = Both the conditions must be true.
OR = any of the conditions must be true
NOT = opposite condition must be true


username="king77"
password="queen717"
entered_username=input("Enter the username: ")
entered_password=input("Enter the password: ")

#and
if username==entered_username and password==entered_password:
    print("Locked in Successfully")
else:
    print("Invalid Login")  

    #or  
day=input("Enter a day: ")
if day=="Saturday" or day=="Sunday":
    print("Holiday")
else:
    print("Working day")   

      #not 
logged_in=False
if not logged_in:
    print("login uccessfull, welcome user")
else:
    print("Please Login")
@@@@@@@@

    #membership operator checks whether an element is present or not
movies=["kill bill","spider man","harry potter"]
movie=input("Enter a movie: ")
if movie in movies:
    print("Movie available")
else:
    print("Movie is not available")
  
employees=["Devika","Afla","Thasni"]
employee_name=input("Enter the employee name: ")
if employee_name not in employees:
    print("Access denied")
else:
    print("Access granted")  
'''
'''
    #identity operator :- checks whether the memory loc is same or not
    #keywords:-is , is not
value1=35
value2=35
print(value1 is value2)  
print(value1==value2)

list1=[35,33,54,71]
list2=[35,33,54,71]
print(list1 is list2)
print(list1==list2) '''   

#bitwise
a=5
b=3
print(a&b)
#0 1 0 1
#0 0 1 1
#0 0 0 1 
print(a|b)
#0 1 0 1
#0 0 1 1
#0 1 1 1
print(a^b)
#0 1 0 1
#0 0 1 1
#0 1 1 0
#not is - or minus of that number plus one
print(~a)#minus of a+1 is -6 ((-5)+1=-6)~- symbol called tilda
#left shifft is to left and right shift is for to the right
print(5<<1)#firts nuber *2^1(Eg:5*2^1)here is multiplication
print(5>>1)#right shift (eg:5/2^1 right shift is dividing)
print(5>>2)

