# What is Python

Python is a general purpose and high-level programming language. Created in 1991 by Guido Van Rossum (GVR) and further developed by the Python Software Foundation.

Its used for:
1. System scripting
2. Web/Software Development
3. Game Development
4. Complex Mathematics

# Benefits of Python

1. High-level programming
2. OOP language
3. Dynamically typed
4. Extensive support for ML libraries
5. Matured open source community
6. Portable across operationg systems

# Is Python a compiled or interperted language?

Its partially compiled and partially interpreted

# How do we comment on Python?

by wrapping the code around `""" ..... """` or with the `#` symbol

5 Difference between a mutable and immutable data type

Mutable datatypes can be edited. they can change in run time e.g List, Dictionaries
Immutable datatypes cannot be edited. they cannot change during run time e.g Strings, Tuple

# How are arguments passed by value or by reference in python

They are passed by object reference a.k.a they are passed by assignment. this means functions receive references to the same objects

# Difference between Set and Dictionary

A set is a collect of unordered and unique values that are iterable and mutable.

A Dictionary is an ordered collection of values use to store key-value pairs

# List comprehension

A list comprehension is a syntax contruction to ease the construction of lists based on a existing iterable

E.g 

```
list = [for i in range(0, 10)]
```

# What is a lamda function?

It is an Anonymous function. it can have numerous parameters but just one statement

```
a = lamda x, y: x * y

print(a(2, 2))
```

# What is Pass in Python
Pass means 'Peforming no operation' or simply a placeholder for an empty statement

# Difference between / and //

/ results in a floating value

// results to an integer


# How are errors handled in Python

By using `try...except...finally`

Try is the monitored block for errors

Except is the block that catches the error raised from try and

finally runs inevitably runs and is used for cleanup/reset activities

# What is swapcase?

Used to alter existing cases of a string. swaps uppercase to lowercase and vise versa

```string.swapcase()```

# For loop and while loop differences

For loop is used on iterable data types and where the start and end condition are known. while loops are use when the the end condition is known


# Higher-order functions

They are functions that accept other functions as arguments

# How to use floor and ceil in Python

with the `.floor()` and `.ceil()`

# What are the built in data types in Python?

1. Strings
2. Integers
3. Float
4. Boolean
5. Dictionaries
6. Lists
7. Tuples
8. Sets
9. Range

# What is Break, continue and pass

break - it breaks out of a loop completely

continue - it contues to the next iteration in a loop 

pass - Means performing no operation


# Statically and dynamically typed languages

Statically typed - You must assign types to variables. data types are known at compile time
Dynamically typed - you dont have to assign types to variables as the data types can be infered at run time

# What is a docstring

created by using ```''' '''``` or ```"""..."""```


# Scope in Python

Where a variable is located and where it can be accessed is scope

Local scope : variables in functions
Global scope:  variables outside functions


