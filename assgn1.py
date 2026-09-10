customer_name=input("Enter your name: ")
food_item_name=input("Enter Food item: ")
quantity=int(input("Enter the quantity: "))
price_per_item=float(input("Enter the price per item: "))
delivery_distance_in_km=float(input("Enter the delivery distance: "))

print("The customer name is: ",customer_name)
print("The ordered food item is: ",food_item_name)
print("The ordered quantity is:  ",quantity)
print("The price per item is: ",price_per_item)
print("The delivery distance in km is: ",delivery_distance_in_km)

print(type(customer_name))
print(type(food_item_name))
print(type(quantity))
print(type(price_per_item))
print(type(delivery_distance_in_km))

print(id(customer_name))
print(id(food_item_name))
print(id(quantity))
print(id(price_per_item))
print(id(delivery_distance_in_km))

total_food_cost=price_per_item*quantity
delivery_charge=30.0
final_bill=total_food_cost+delivery_charge
price=total_food_cost
print("Total food cost: ",total_food_cost)
print("Delivery cahrge: ",delivery_charge)
print("Final bill amount: ",final_bill)

print(isinstance(quantity,int))
print(isinstance(price,float))
print(isinstance(final_bill,float))


'''variables= storage space or containers for storing data.
data types= kind of data stored . eg:int,float,str
memory management using id()= returns the unique identity of an object ,i.e its memory address.
Type conversions:
1.Explicit Type conversion:- we have to manually convert the data type.
2.Implicit Type conversion:- python automatically converts the data type. 
'''
