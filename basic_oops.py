#object= real world entity or logical entity, it has state ,behaviour and identity.
#eg:pen:- identity: its name,state : colour,brand , behaviour: what it can do, lke writing ,drwaing etc
#class: group of similar objects or user defined data types.
# 4 basic concepts/pillars of oops :
#1.inheritance:
#2.polymorphism
#3.abstraction
#4.encapsulation

#custom method  
'''
class Student:  # Use pascal for class name
    def display(self):   # self parameter is a must in function inside the class
        print("I'm a Student")
student_object=Student()  # object creation
student_object.display()
'''


#constructor: special method in python,mainly used for initializing an object
#it will be automatically called when an object is created

class Employee:
    def __init__(self): # init is the constructor
        print("Default construct is called")
employee_object=Employee()

#next class object initialization
