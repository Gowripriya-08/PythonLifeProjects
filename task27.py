# ask 1: Add Function
# Write a Python function named add that takes two arguments a and b and
# returns their sum.
def add(a,b):
    return a+b
print(add(1,2))

# Task 2: Square Function
# Write a Python function named square that takes a number x as input and
# returns its square.
def square(base,expo = 2):
    return base**expo
print(square(2))

# Task 3: Factorial Function
# Write a Python function named factorial that takes a positive integer n as
# input and returns its factorial
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result
print(factorial(5))

# Task 4: Maximum Function
# Write a Python function named maximum that takes a list of numbers as input and
# returns the maximum value in the list.

def maximum(*a):
    a = [1,2,3,4,5]
    return max(a)
print(maximum())

# Write a Python function named reverse that takes a string s as input and
# returns its reverse.

def reverse(*name):
    name = "python"
    return name[::-1]
print(reverse())

# Task 6: Check Prime Function
# Write a Python function named is_prime that takes a positive integer n as input
# and returns True if n is prime, otherwise False .

def is_prime(n):
    if n %2 == 0:
        print("True")
    else:
        print("False")
is_prime(4)

# Task 7: Fibonacci Function
# Write a Python function named fibonacci that takes a positive integer n as
# input and returns the n th Fibonacci number.

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a

print(fibonacci(6))

# Write a Python function named is_palindrome that takes a string s as input and
# returns True if s is a palindrome, otherwise False .
def is_palindrome(*s):
    if s == s[::-1]:
        print("True")
    else:
        print("False")
is_palindrome("madam")

# # Task 9: Sum of Squares Function
# Write a Python function named sum_of_squares that takes a list of numbers as
# input and returns the sum of the squares of those numbers.

def sum_of_squares(*n):
    result = 0
    for i in n:
       expo= i**2
       result+=expo
    return result
print(sum_of_squares(1,2,3,4,5,6,7))

# Task 10: Average Function
# Functions Quiz: 3
# Write a Python function named average that takes a list of numbers as input and
# returns the average value.
def average(*n):
    add = 0
    for i in n:
        add+=i
        result = add/len(n)
    return result
print(average(10,20,30))