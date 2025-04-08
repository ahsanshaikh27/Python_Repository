# Day 2: Input, Output, Type Casting, Comments & String Basics

# Taking input from user

name = input("Enter your name: ")
age = input("Enter your age: ")

# Type of casting

age =int(age) # converting string to int
print(f"Hello {name}, you are {age} years old.")
print("In 5 years you will be:" , age + 5)

# string Operations
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("length of name:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])
print("Middle characters:, name[1:-1]")

# Comments

# This is a single-line comment

"""
This is a 
multi-line comment
"""
# f-string formatting
print(f"Welcome {name}, enjoy learning Python!")