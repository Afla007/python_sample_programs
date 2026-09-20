#exception:-unexpected event that we can solve, eg:error password , we can solve that by "forgot password"



'''
print("statement 1")
print("statement 2")
print("statement 3")
try:
    value1=10
    value2=0
    value3=value1/value2  #zero division error
except ZeroDivisionError:
    print("denominator can't be zero")
print("statement 4")
print("statement 5")
'''
'''
#try except else
numerator=int(input("Enter the numerator: "))
denominator=int(input("Enter the denominator: "))
try:
    quotient=numerator/denominator
except ZeroDivisionError:
    print("denominator can't be zero")
else:
    print("quotient")     
    '''

#type error
'''
try:
    num1=15
    num2="25"
    add=num1+num2
    print(add)
except TypeError:
    print("String can't be added with integer value")
'''
#index error:- index out of range
'''
numbers=[1,2,3,4,5,6,7,8,9,10]
try:
    print(numbers[10])
except IndexError:
    print("index out of range")
'''

#key error-dictionary
'''
book_details={
    "book_id":2,
    "book_name":"atomic habits"
}
try:
    print(book_details["book author"])
except KeyError:
    print("key not found")
'''
#file not found:- happens when srching for a file that doesnt exist
'''
try:
    with open("test_file.txt","r") as f:
        print(f,read())
except FileNotFoundError:
    print("file not found in directory")
'''

#import error
'''
try:
    from math import square
except ImportError as e:
    print(e)
    '''

#attribute error
'''
try:
    user_value="welcome"
    print(user_value.add())
except AttributeError as e:
    print(e)
'''
#value error:- when no proper value is given
'''
try:
    data=int("Afla")
except ValueError as e:
    print(e)
'''
#name error:-
'''
try:
    print(student)
#except NameError as e:
   # print(e)
finally:      # works even if there is an except,it doesnt mind the except 
    print("executed normally")
'''
#multiple exception: if there is more than one problem in try ,they resolve the 1st problm
'''
try:
    data=int("Afla")
    user_value="welcome"
    print(user_value.add())
except ValueError as e:
    print(e)
except AttributeError as e:
    print(e)
'''

#multiple exception using another method

try:
    data=int("Afla")
    user_value="welcome"
    print(user_value.add())
except (ValueError,AttributeError) as e:   # use tuple for multiple classes 
    print(e)
