# Write a Python function square_all(numbers) that takes a list of numbers as input
# and returns a new list containing the square of each number in the input list.
# Use the map() function with a lambda function to implement this


def square(*numbers):   
    result = map(lambda a:a**2,numbers)  
    return list(result)
print(square(1,2,3,4,5,6))

# Write a Python function filter_positive(numbers) that takes a list of numbers as
# input and returns a new list containing only the positive numbers from the
# input list. Use the filter() function with a lambda function to implement this.

def filters(* numbers):
        result = filter(lambda a: a>0,numbers)
        return list(result)
print(filters(1,2,3,4,5,6,7,-6,-5,-3,-2))

# Write a Python function calculate_factorial(n) that calculates the factorial of a
# given number n . Use the reduce() function with an appropriate lambda
# function to implement this.

from functools import reduce

def calculator(n):
      result = reduce(lambda a,b:a*b,range(1,n+1))
      return result
print(calculator(5))

# # Write a Python function count_vowels(string) that takes a string as input and
# returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce()
# function with an appropriate lambda function to implement this

from functools import reduce

vowels = "aeiou"

def count_vowels(string):
    result = reduce(lambda count, letter: count + (letter in vowels), string, 0)
    return result

print(count_vowels("hello"))