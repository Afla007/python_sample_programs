print("ONLINE LIBRARY MANAGEMENT")

book_name=["Python","Java","C++"]
issued_books=[]
members=["Alan","Bista","Carl"]
print("Available books: ",book_name)
print("Issued books: ",issued_books)
print("Members: ",members)

print(book_name[0])
print(book_name[1])
print(book_name[2])
print(book_name[0:2])

print("[Python,Java,C++]".upper())
print("[Python,Java,C++]".lower())
print("[Python,Java,C++]".title())

issued_books.append("sql")
print(issued_books)
book_name.insert(1,"C#")
print(book_name)
book_name.remove("Java") 
print(book_name)
members.pop(1)
print(members)
book_name.sort()
print(book_name)
book_name.reverse()
print(book_name)

available_books=[book for book in book_name]
print("Available Books: ",available_books)
p_books=[book for book in book_name if book.startswith("P")]
print("Books starting with P:",p_books)
uppercase_books=[book.upper() for book in book_name]
print("Uppercase Book Names: ",uppercase_books)

categories=("Programming","Database","Networking")
print("Book Categories: ")
cat1,cat2,cat3=categories
print(cat1)
print(cat2)
print(cat3)

genres={"Python","Java","Python","C++"}
print("Unique Genres:",genres)
genres.add("Database")
genres.remove("Java")
print("Updated Genres:",genres)

genres1={"Python","Java","C++"}
genres2={"Python","Database","C++"}
print("Union: ",genres1.union(genres2))
print("Intersection: ",genres1.intersection(genres2))

book = {
    "book_id":101,
    "title":"Python Basics",
    "author":"Alex",
    "status":"Available"
}
print("Book Details: ",book)
print("Book Title: ",book["title"])
print("Dictionary Keys: ",book.keys())
print("Dictionary Values: ",book.values())
print("Dictionary Items: ",book.items())
print("Book Author: ",book.get("author"))

book.update({"title":"Python Programming"})
print("Updated Book: ",book)
book.pop("author")
print("After Removing Author: ",book)

member = {
    "name": "Alan",
    "member_id":101,
    "age":22
}
print("Member Details: ",member)
print("Member Name: ",member["name"])

issue_status={
    "Python":"Issued",
    "Java":"Available",
    "C++":"Available"
}
print("Issue Status:",issue_status)

library={
    101:{
        "title":"Python",
        "author":"Alex",
        "status":"Available"
    },
    102:{
        "title":"Java",
        "author":"David",
        "status":"Issued"
    }
}
print("Nested Dictionary Data: ",library)
print("First Book: ",library[101])
print("First Book Title: ",library[101]["title"])

student={
    "name":"Afla",
    101:"Python",
    (1,2):"Programming"
}
print("Immutable Keys Dictionary: ",student)

