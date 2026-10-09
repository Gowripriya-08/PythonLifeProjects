# #Exercise 1: Sum of Squares
# Write a Python program that calculates and prints the sum of the squares of
# numbers from 1 to 5 using a
# for loop.
sum = 0
for i in range(1,6):
    result = i**2
    print(f"sum of square{i} = {result}")
    sum+= result
print(sum)
# Exercise 2: Countdown
# Write a Python program that uses a
# while loop to print a countdown from 5 to 1.
count = 5
while count >=1:
    print(count)
    count-=1
# Exercise 3: Multiplication Table with Nested For Loop
# Write a Python program to print the multiplication table for a user-specified
# number using a nested for loop.
table = int(input("enter the number1:"))
for i in range (1,11):
    for j in range(1):
        print(f"{table}*{i} = {table * i}")
# Exercise 4:
# Write a Python program that uses a "for" loop to find the sum of all even
# numbers between 0 and 10 (inclusive)
sum = 0
for i in range(0,11):
    if i%2==0:
        sum+=i
print(sum)
# Exercise 5:
# Calculate the sum of all numbers from 1 to a given number

number = int(input("enter the number"))
sum = 0
for i in range(1,number+1):
    sum+=i
print(sum)
# Exercise 6:
# Display numbers from a list using loop
box = [1,2,3,4,5,6,7,8,9,10]
for i in box:
   print(i)

#Exercise 7:
# Display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)

# Exercise 8:
# Write a Python program to print the cube of all numbers from 1 to a given
# number
result = int(input("enter your value "))
for i in range (1):
    for j in range(1,result):
        cube = j**3
        print(cube)
