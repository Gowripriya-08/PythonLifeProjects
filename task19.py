#Write Python code to reverse the order of elements in the given list my_list .
# Print the reversed list.

my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()
print(my_list)

# Given two lists list1 and list2 , find and print the common elements between
# them.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
empy_list = []
for i in list1:
     if i in list2:
          empy_list.append(i)
print(empy_list)

# Create a new list unique_list containing only the unique elements from the
# given list original_list . Print the unique list.

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for i in original_list:
     if i not in unique_list:
          unique_list.append(i)

print(unique_list)

# Remove duplicate elements from the given list duplicated_list and print the list
# without duplicates while preserving the order.

duplicated_list = [1, 2, 2, 3, 4, 4, 5]
listee = []
for i in duplicated_list:
     if i not in listee:
          listee.append(i)
print(listee)

# Write a Python script that concatenates two lists and prints the result.

list_1= [1,2,3,4,5]
list_2 = [6,7,8,9,10]
list_1.extend(list_2)
print(list_1)

# Write a Python script that repeats a list three times and prints the result.
my_list = [10,20,30]
repeat_list = []
for i in range (3):
     repeat_list.extend(my_list)
print(repeat_list)

# Write a Python script that removes the elements at even indices from a list.

priya_list = [1,2,3,4,5,6,7,8,9,10]
print(priya_list[1::2])

# Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of
# a list

priya_list.insert(0,10)
priya_list.insert(1,11)
priya_list.insert(2,12)
print(priya_list)

# square_list =[]
# for i in range(1,11):
#       result= i**2
#       square_list.append(result)
# print(square_list)

# 1. Square Numbers: Create a list of squares of numbers from 1 to 10.
print([i**2 for i in range(1,11)])

# 2. Even Numbers: Generate a list of even numbers from 1 to 20.

result = [i for i in range(1,21) if i%2==0]
print(result)

# 3. Words Lengths: Given a list of words, create a list containing the lengths of
# each word.

words = ["apple", "banana", "cherry", "date"]
print([len(i) for i in words])

