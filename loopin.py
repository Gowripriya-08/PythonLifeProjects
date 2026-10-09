emp_data = ["kiran","vasu","ashok","teja"]
for item in emp_data:
    print(f"{item} welcome to this world")

sample = "life"
for i in sample:
    print("hello everbody")

for i in range(10):
    print("hiii everyone ")

for i in range(5,10):
    print(f"{i}get lost")

for i in range(5,10,2):
    print(f"{i}hey you")

# multiplication table
for i in range(1,11):
   
    print(f"{i}*17 = {17*i}")

table = int(input("enter the number"))

for i in range (1,11):
    print(f"{i}*{table}= {table*i}")

for i in range(1,11):
    for j in range(1,10):
       # print(i,j)
        print(f"{i}*{j} = {i*j}")
        print()
    print("-"*20)


# while

count = 0
while count<3:
    print(count)
    count+=1

while True:
    print("heyy")
    while True:
        print("goo")
        break
    break

for i in range(1,10):
    username = input("enter your username")
    print(username)

