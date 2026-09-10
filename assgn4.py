print("----ONLINE BANKING MANAGEMENT SYSTEM----")

def create_account(name,age,city):
    '''create  a new bank account'''

    print("---Account Details---")
    print(f"Customer Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

name=input("Enter your name: ")
age=int(input("Enter your age: "))
city=input("Enter your city: ")

create_account(name,age,city)

def customer_details(**details):
    '''stores customer details,eq:**kwargs'''
    print(details)
customer_details(name=name,age=age,city=city)



def deposit_amount(balance,amount):
    '''deposit amount'''
    total=balance+amount
    return total

balance=5000
amount=2000

balance=deposit_amount(balance,amount)
print("Updated balance: ",balance)

def withdraw_amount(balance,amount):
    '''withdraw amount'''
    total=balance-amount
    return total

amount=3000

balance=withdraw_amount(balance,amount)
print("Balance after withdrawal: ",balance)


def check_balance(balance):
    '''checks balance '''
    print(f"Current balance: {balance}")
check_balance(balance)


def transaction_history(*transactions):
    '''checks transaction history'''
    print(f"The transaction amounts: {transactions} ")
transaction_history(5000,2000,3000,1000)


def loan_eligibility(age,balance):
    '''checks loan eligibility'''
    if age>=18 and balance>=5000:
        return "Eligible for loan"
    else:
        return "Not eligible for loan"
        
print(loan_eligibility(age,balance))

def update_balance(amount):
    '''updates global bank balance'''
    global balance
    balance = balance + amount
    
update_balance(1000)
print("Balance after global update:", balance)


interest = lambda amount:amount*0.05
print("Interest on amount: ",interest(balance))

transactions = [5000, 2000, 3000, 1000]

print("No. of transactions: ",len(transactions))
print("Total transactions: ",sum(transactions))
print("Max transaction: ",max(transactions))
print("Min transaction: ",min(transactions))
print("Rounded interest: ",round(interest(balance), 2))