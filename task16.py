# #Problem 1: Using break in a While Loop
# Write a Python program that takes a list of numbers as input numbers = [25, 30,
# 20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds
# 100, stop adding numbers and print "Sum exceeded 100".



numbers = [25, 30,20, 40, 15, 25]
sum = 0
for i in numbers:
    sum+=i
    if(sum>100):
        print("the sum exceeds 100")
        break

# Write a Python script that uses a for loop to iterate through numbers from 1 to
# 600. Print only the odd numbers, skipping the even ones using the continue
# statement
for i in range(1,601):
    if i%2==0:
        continue
    print(i)

# #Write a Python script that checks if a number is even or odd. If the number is
# even, print "Even"; if odd, do nothing (use the pass statement).
for i in range(1,10):
    if i%2 == 0:
        print(f"{i} is a even number")
    else:
        pass

# #Write a Python script that iterates through a list of words. If the word is "break,"
# exit the loop using the break statement. If the word is "skip," skip the rest of the
# code for the current iteration using the continue statement. For any other word,
# print the word.
words = ["skip","go","dontgo","stop","break","continue","skip"]
for i in words:
    if i =="break":
        break
    elif i =="skip":
        continue
    else:
        print(i)