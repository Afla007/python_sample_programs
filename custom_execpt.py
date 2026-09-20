'''
class Custom_Exception(Exception):  # first you create a class which will inherit the exception only then can you do the try and except 
    pass # do nothing
def check_nummber(num):
    if num<0:
        raise Custom_Exception("not allow negative numbers")
    return num
try:
    result=check_nummber(2)
except Custom_Exception as e:
    print(e)
else:
    print(result)
'''
'''
class NameTooShortError(Exception):
    pass
name=input("Enter the name: ")
try:
    if len(name)<8:
        raise NameTooShortError("minimum 8 characters required")
except NameTooShortError as e:
    print(e)
'''
class InsufficientBalanceError(Exception):
    pass
available=5000
amount=int(input("Enter the amount to withdraw: "))
try:
    
    if amount>available:
        raise InsufficientBalanceError("Insufficient Balance")
except InsufficientBalanceError as e:
    print(e)
else: 
    print("Transaction Successful")






