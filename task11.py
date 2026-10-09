#1. Vowel Checker:
#Write a Python program that takes a character as input and checks whether
#it is a vowel or not. Use the
#f-else statement.

letter = input("enter any letter ")
vowel = "aeiouAEIOU"
if letter in vowel:
    print(f"your letter {letter} is a vowel")
else:
    print(f"your letter {letter} is not vowel")

#2. Age Group Classification
# Write a program that takes an age as input and classifies the person into
# one of the following age groups:
# Child: 0-12 years
# Teenager: 13-17 years
# Adult: 18-64 years
# Senior: 65 years and older
age = int(input("enter your age: "))
if (age>=0 and age <=12):
    print("your are a child")
elif(age>=12 and age<=17):
    print("you are a teenager")
elif(age>=18 and age<=64):
    print("you are an adult")
elif(age>=65):
    print("you are a senior")
else:
    print("please print the correct number")

# #3. Number Classifier:
# Write a program that takes an integer as input and classifies it as positive,
# negative, or zero. Use the
# if-elif-else statement
number = int(input("enter a number:"))
if(number>0):
    print(f"{number} is a postive integer")
elif(number<0):
    print(f"{number} is a negative integer")
else:
    print("the number you enter is 0")

#4. Leap Year Checker:
# Create a program that checks whether a given year is a leap year or not. A
# leap year is divisible by 4, but not by 100 unless it is divisible by 400.
year = int(input("enter the year- "))
if( (year%4)==0):
    print("its a leap year")
elif((year%100)==0):
    print("it is not a leap year")
elif((year%400)==0):
    print("it is a leap year")
else:
    print("it is not a leap year")

# 5. Calculator:
# Build a simple calculator program that takes two numbers and an operator
# (+, -, *, /) as input and performs the corresponding operation.

inp1 = int(input("enter the input number1: "))
inp2 = int(input("enter the input numebr2: "))
operator = input("enter your operator ")
if(operator =="+"):
    print(inp1+inp2)
elif(operator == "-"):
    print(inp1-inp2)
elif(operator=="*"):
    print(inp1*inp2)
elif(operator=="/"):
    print(inp1/inp2)
else:
    print("enter the correct operator")

# 6. Short Hand If:
# Rewrite the following code using the short-hand
# if statement:
# Quiz Questions: 3
# x = 8
# if x % 2 == 0: result = "Even"
# else: result = "Odd"

x =8
result = "Even" if x%2 == 0 else "Odd"
print(result)

# 7. Discount Calculator:
# Create a program that calculates the final price after applying a discount.
# The program should take the original price and the discount percentage as
# input.

price = int(input("enter the price of the item: "))
discount = int(input("enter the discount price: "))
result = price*(discount/100)
print(price-result)

#8. BMI Calculator:
# Write a program that calculates the Body Mass Index (BMI) using the
# formula: BMI = weight (kg) / (height (m))^2. The program should take
# weight and height as input.
weight = int(input("enter the weight in kgs: "))
height = int(input("enter the height in m: "))
bodymass = weight/(height**2)
print(f"the body mass is {bodymass}")