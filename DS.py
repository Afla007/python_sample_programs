#non primitive DS
#primitive DS

#string-immutable data
#list-[]-ordered collection,mutable, allows duplicate, can be accessed using indexing
#tuple-()- ordered collection,immutable, allows duplicate, can be accessed using indexing
#set-{}-unordered collection, mutable,doesnt allow duplicates,cant be accessed using indexing
#dictionary-{key:value}- ordered collection, value can be changed, allows duplicates(key unique aayirikknm), can be accessed using keys


'''
username="Afla"

 #A   f   l   a
 #0   1   2   3   #positive Indexing 
#-4  -3  -2  -1    #negative indexing
 #1   2   3   4   #length

print(username[2])
print(len(username))
print(username[-2]) 
#indexing returns a single value and slicing gives a set of string or substring

#slicing
#syntax:-  [start:stop:step/skip value]
#start= default value is 0
#stop=value-1
#step=no. of skips(defaultly 1 for +ve numbers
data="python is a programming language"
print(data[:8])# PLEASE REMEBER THERE IS 0 IN INDEXING
print(data[2:8])
print(data[2:12:3])
print(data[6:])
print(data[1:10:-2])  # it wont work
print(data[10:1:-2])  #negative value kodth skip chyynmengil start big m stop small m aavnm
print(data[::-1])
print(data[::-2])

#string method
text="python is good"  # all are function thats why paranthesis is given
print(text.upper())  
print(text.lower())
print(text.capitalize())   # only the first letter is capital
print(text.title())
print(text.startswith("yt"))
print(text.endswith("good"))
#text[0]="r"  # we cant do this because string is immutable, 
#print(text)
print(id(text))
uppercase=text.upper()
print(id(uppercase))  # id will not be same because as we ahve said string is immutable so when we make changes its memory location also changes


#List
#crud operation-create, view, update,delete
userdata=["Afla",22,"tvm"]   #create
print(userdata)     #view
userdata.insert(1,"MCE")  #update
userdata.append(2026)
userdata.extend("python")
userdata.append(["eng","hindi","urdu"])
print(userdata)
print(userdata[11])
print(userdata[11][0])
userdata.extend(["c","python","java"])
print(userdata)
userdata[0]="Afla Rahim"
print(userdata)
userdata.remove("tvm")  #delete using remove
print(userdata)
userdata.pop(4)   #delete using pop ,here you use the index number
print(userdata)
userdata.reverse()
print(userdata) 
# thers more in notes try tht also
'''
'''
#tuple
tuple1=(1,2,3,4,5)
print(tuple1)
#nested tuple
tuple2=("afla","devika","thasni",(6,7,8))
print(tuple2)

#tuple unpacking  
person=("Afla",22,"Tvm")
name,age,place=person
print(name)

num=(10,20,30,40,50)
a,b,*c=num
print(c)
print(a)
print(b)

num1=(10,20,30,40,50)
e,*f,g=num1
print(f)
print(g)
print(e)

num2=(11,22,22,33,44,44)
print(num2.count(22)) # for example: used when there are many same names and we want to know the count
print(num2.index(33))
print(num2[2])

name=input("Enter a  string: ")
count=0
for char in name:
    count+=1
print("the count is: ",count)

user_input=input("enter a string: ")
for letter in user_input:
    if user_input.count(letter)==1:
        print("First non repeating character: ",letter)
        break
else:
        print("no non-repeating character")   

 # try : repeating character index,second non repeating character,without using the count function(imp,must do)

'''
'''
#SET:-unorderd,mutable,no duplicates,cannot access by indexing
student1={"english","hindi","malayalam"}
student2={"english","hindi","python"}
student3={"python","urdu"}
student1.add("C")
#student1.add("kannada","marathi") # only one argument can be passed like append

print(student1)
student1.update(["C++","java",])
print(student1)
student1.pop()

print(student1)
#student1.remove("arabic")   # remove keyword raises an error if we give a wrong element but in discard it doesnt show an error
#print(student1)
student1.discard("Arabic")
print(student1)



#try union ,intersection,difference,symmemtric difference

#UNION
print(student1.union(student2))     
print(student1|student2) 

#INTERSECTION
print(student2.intersection(student3))
print(student2&student3)

#DIFFERENCE
print(student1.difference(student2))   
print(student1-student2) 

#SYMMETRIC DIFFERENCE
print(student1.symmetric_difference(student2))   
#print(student1-student2) 

#subset,superset,disjoint (HW)

#frozen set=immutable 
fs1=frozenset("Afla")
fs2=frozenset([1,2,3,4,5,2,3,4])
print(fs1)
print(fs2)
'''
#DICTIONARY:- two ways to use 
'''
student={             #1st wway
    "name":"Afla",
    "age":22,
    "place":"tvm"
}
print(student)
print(student["name"])
info=dict(city="tvm",state="kerala") #2nd way
print(info)
print(info.keys())  # to print only the keys
#print(info["mark"])

student.pop("age")
print(student)   # try 

for key,value in student.items():  # to print both key and value use items()
    if key=="name":
        print(key,value)
'''
#nested dictionary
employee={
    "emp1":{"name":"afla","age":22},
        "emp2":{"name":"alan","age":23},
    "emp3":{"name":"afsal","age":22},
    "emp4":{"name":"arya","age":24}

}
print(employee)
print(employee["emp3"]["age"])

#saturday,even today itself- write every syntax you have learned until now