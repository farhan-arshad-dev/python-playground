import sys

print("Hello World!")
print("System Vesion: " + sys.version)

# single-line comment

"""
This is a
multi-line comment
or docstring.
"""

# Data types

# Integer assignment
a = 45
# Floating-point assignment
b = 1456.8
# String assignment
c = "Farhan"

print(a)
print(b)
print(c)

# Python is dynamically typed, so variables can change type.
# Use triple quotes ('''...''' ) or ( """...""") for strings that
# span multiple lines. Newlines are preserved.
# string, immutable, Ordered Collection(Elements have positions (indexes)),
x = "Hello World"
y = """Hello
World"""

print("Print Single line and multiline string")
print(x)
print(y)

# Strgin Manipulation
s = "Hello World"
substring = s[1:8]  # Output: ello Wo
reversed_s = s[::-1]  # Output: dlroW olleH

s = "Python"
first_char = s[0]  # Output: P
last_char = s[-1]  # Output: n


# Rule of thumb If changing a value creates a new object => it’s immutable
# Immutable objects are safer in multi-threaded programs.

print("Checking the x as integer is immutable.")
x = 50  # integer (immutable)
# id() => Reference means the memory location (object identity) where the value is stored.
print(id(x))
x = x + 5
print(id(x))

x = 60.5  # float (immutable)
x = 3j  # complex (immutable)

print("*********************")
print("Complex number")
print(x)

# Sequence Types
# list (Ordered Collection, mutable, Slower due to dynamic nature, memory overhead)
x = ["geeks", "for", "geeks"]
print("Accessing element from the list")
print(x[0])
print(x[2])

print("Accessing element using negative indexing")
print(x[-1])
print(x[-3])

# tuple (Ordered Collection, immutable, memory-efficient, Faster for read-intensive)
x = ("geeks", "for", "geeks")
x = {"name": "Suraj", "age": 24}  # dict (Key vale, mutable)

# set (Mutable,  Unordered (order not guaranteed))
x = {"geeks", "for", "geeks"}
print("*********************")
print("Printing Set")
print(x)

# frozenset => immutable version of a set

x = True  # bool    (immutable)

x = b"Geeks"  # binary (immutable)
print("Printing binary")
print(x)
x = bytes(5)  # Creates a bytes object of length 5, with all zero values
print(x)

# None(value) => NoneType(data type)
# Represents “no value”
# None is Singleton
x = None
type(x)  # <class 'NoneType'>

print("Reference of the None:")
y = None
print(id(x))
print(id(y))


# the value entered by the user is stored as a string by default.
val = input("Enter your value: ")
print("You entered:", val)

name = input("Enter your name: ")
age = int(input("Enter your age: "))  # need to convert explicitly

print(type(name))  # type() Returns the class/type of the given object
print(type(age))

# Object Reference in Python
# Python variables hold references to objects, not the actual objects themselves.
x = 5
y = x  # assigns the reference of the x to y. called a Shared Reference,

#  Delete a Variable
x = 10
print(x)
del x  # This deletes the variable and frees up the memory it was using.

# type() vs isinstance()
if type(age) == int:  # Works, but not recommended use isinstance()
    print("Integer")

print(isinstance(age, int))

type(age)  # Returns the exact class of an object, Performs a strict type check

# Checks whether an object is an instance of a class OR its subclasses, Supports inheritance & polymorphism
isinstance(age, int)

# Boolean Trap cuz bool inherits from int
isinstance(True, int)  # True
type(True) == int  # False

# Multiple Type Checking
# bad practice
x = 3
type(x) == list or type(x) == tuple

# best practice
isinstance(x, (list, tuple))

# is Operator
a is b  # Equivalent to id(a) == id(b)
a == b  # True  (values same)
a is b  # False (different objects, checks identity (same object))


# Conditional Statements
i = 10
# Checking if i is greater than 15
if i > 15:
    print("10 is less than 15")

print("I am Not in if")

# Truthy and Falsy Values
if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")

i = 20
# Checking if i is greater than 0
if i > 0:
    print("i is positive")
else:
    print("i is 0 or Negative")

#  nested if else
i = 10
if i == 10:
    #  First if statement
    if i < 15:
        print("i is smaller than 15")

    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
else:
    print("i is not equal to 10")

# if…elif…else Statement
i = 25

# Checking if i is equal to 10
if i == 10:
    print("i is 10")
# Checking if i is equal to 15

elif i == 15:
    print("i is 15")
# Checking if i is equal to 20

elif i == 20:
    print("i is 20")

# If none of the above conditions are true
else:
    print("i is not present")

# Loops
# For loop iterate over a sequence such as a list, tuple, string or range.
for i in range(0, 10, 2):
    print(i)

count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")

# Continue, Break, Pass Statement
# Continue, Break same as C++
# Pass is also used for empty control statements

# In this example, the loop iterates over each letter in 'geeksforgeeks'
# but doesn't perform any operation, and after the loop finishes, the last letter ('s') is printed.
for letter in "geeksforgeeks":
    pass
print("Last Letter :", letter)


# Python Functions
'''    
def function_name(parameters):
    """Docstring"""
    # body of the function
    return expression
'''


def evenOdd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


evenOdd(2)
evenOdd(3)

# Default Arguments


def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myFun(10)

# Keyword Arguments


def student(fname, lname):
    print(fname, lname)


student(fname="Geeks", lname="Practice")
student(lname="Practice", fname="Geeks")

# Arbitrary Arguments


def myFun(*args, **kwargs):
    """
    Non-Keyword Arguments (*args)
        special syntax *args allows us to pass any number of positional
        (non-keyword) arguments to a function. These arguments are collected into a tuple

    Keyword Arguments (**kwargs)
    The special syntax **kwargs allows us to pass any number of keyword
    arguments (arguments in the form key=value). These arguments are collected into a dictionary, where:
    Keys = argument names
    Values = argument values
    """
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")


# Function call with both types of arguments
myFun("Hey", "Welcome", first="Geeks", mid="for", last="Geeks")

# Pass by Reference and Pass by Value
# Technically, Python uses "pass-by-object-reference".
# Mutable objects behave like pass by reference,
# while immutable objects behave like pass by value.

# List Comprehension
print("List Comprehension")
a = [2, 3, 4, 5]
res = [val**2 for val in a]
print(res)  # [4, 9, 16, 25]


# Lambda Functions
# Lambda Functions are anonymous functions means that the function is without a name.
def n(x):
    return "Positive" if x > 0 else "Negative" if x < 0 else "Zero"


print(n(5))
print(n(-3))
print(n(0))

# Lambda Functions with List Comprehension
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

# Returning Multiple Results


def calc(x, y):
    return (x + y, x * y)  # return the tuple


res = calc(3, 4)
print(res)
