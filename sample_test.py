print("HELLO")

python
variablese-->store datadatatypes-->


'''
# Tuple

categories = ("Programming", "Database", "Networking")

print("Book Categories:")

cat1, cat2, cat3 = categories

print(cat1)
print(cat2)
print(cat3)


# Tuple immutability

# categories[0] = "AI"
# This gives an error because tuples are immutable.


# Set

genres = {"Python", "Java", "Python", "C++"}

print("Unique Genres:")
print(genres)

genres.add("Database")
genres.remove("Java")

print("Updated Genres:")
print(genres)


# Set operations

genres1 = {"Python", "Java", "C++"}
genres2 = {"Python", "Database", "C++"}

print("Union:")
print(genres1.union(genres2))

print("Intersection:")
print(genres1.intersection(genres2))


# Dictionary

book = {
    "book_id": 101,
    "title": "Python Basics",
    "author": "Alex"
}

print("Book Details:")
print(book)

print("Book title:")
print(book["title"])


# Dictionary methods

print("Dictionary Keys:")
print(book.keys())

print("Dictionary Values:")
print(book.values())

print("Dictionary Items:")
print(book.items())

print("Book Author:")
print(book.get("author"))

book.update({"title": "Python Programming"})

print("Updated Book:")
print(book)

book.pop("author")

print("After removing author:")
print(book)


# Nested dictionary

library = {
    101: {"title": "Python", "author": "Alex"},
    102: {"title": "Java", "author": "David"}
}

print("Nested Dictionary Data:")
print(library)

print("First Book:")
print(library[101])

print("First Book Title:")
print(library[101]["title"])


# Immutable keys

student = {
    "name": "Afla",
    101: "Python",
    (1, 2): "Programming"
}

print("Immutable Keys Dictionary:")
print(student)

# A list cannot be used as a dictionary key
# example:
# {[1, 2]: "Python"}
# This gives an error because list is mutable.


# Hashing

print("Hash Value:")
print(hash("Python"))


# None and NoneType

book_issued = None
member_fine = None

print("Book Not Issued:")
print(book_issued)

print("Member Fine:")
print(member_fine)

print("Type of None:")
print(type(None))

'''