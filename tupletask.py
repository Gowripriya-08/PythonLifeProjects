# Create a Tuple: Write a program that creates a tuple containing three
# elements: your name, your age, and your favorite color. Then print the
# Quiz Questions: 

tuple1 = ('priya',23,'black')
print(tuple1)

# Access Tuple Elements: Write a program that creates a tuple containing the
# days of the week. Then, print the third element of the tuple.

tuple2 = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print(tuple2[2])

# Tuple Concatenation: Write a program that creates two tuples, one
# containing odd numbers from 1 to 5 and another containing even numbers
# from 2 to 6. Concatenate these two tuples and print the result.

tuple3 = (1,3,5)
tuple4 =(2,4,6)
print(tuple3+tuple4)

# Tuple Unpacking: Write a program that defines a tuple containing the
# dimensions of a rectangle (length and width). Then, unpack this tuple into
# two variables and calculate the area of the rectangle

tuple4 = (10,5)
l,b = tuple4
area = l*b
print(area)

# Check if an Element Exists: Write a program that checks if a given element
# exists in a tuple.

tuple= (1,2,3,4,5)
print(3 in tuple)


# Write a Python program to generate a bill for a supermarket purchase. The
# program should store the items and their prices in a list of tuples. It should
# then iterate over this list to print out each item along with its price. Finally,
# calculate and print the total cost of all the items

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
total = 0
print(f"Item\tPrice")
print("-"*22)
for i,j in items:
    j = float(j)
    print(f"{i}\t{j}")
    
    total +=j
print("-"*22)
print(f"total\t{total}")
