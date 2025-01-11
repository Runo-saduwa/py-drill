"""
Writing for loop in Python is a tad different from C++ and Java counterparts. In this question, we'll learn to print table by using the for loop.

You are given a number N, you need to print its multiplication table.

Note: Please go through the range function to understand why it's useful in for loops.

Example 1:

Input:
N = 5
Output:
5 10 15 20 25 30 35 40 45 50
Example 2:

Input:
N = 6
Output:
6 12 18 24 30 36 42 48 54 60
Your Task:
This is a function problem. You don't need to take input of testcases. Just complete the function multiplicationTable() that takes N as input.

Constraints:
1 <= N <= 1018
"""

def multiply(N):
    for i in range(1, 11):
      print(i * N)
      
      
      
"""
Welcome to the part 2 of For Loops in Python. In this question, we'll learn to print characters of a string at even indices.

You are given a string str, you need to print its characters at even indices(index starts at 0).

Note: Please go through the range function to understand how to jump 2 steps.

Example 1:

Input:
str = DoctorPhenomenal
Output:
DcoPeoea
Example 2:

Input:
str = Geeks
Output:
Ges
Your Task:
This is a function problem. You don't need to take input. Just complete the function stringJumper() that takes str as input.
"""

def stringJumper(str: str):
    for i in range(0, len(str), 2):
        print(str[i])