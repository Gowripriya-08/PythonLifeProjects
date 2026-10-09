# addition
num1 = 10
num2 = 20
result = num1+num2
print(result)

#subratction
sub = num2-num1
print(sub)
#multiplication
mult = num1*num2
print(mult)
#division
div = num2/num1
print(div)
#floor division
float = num2//num1
print(float)
#modulus 
mode = num2%num1
print(mode)

# expo
a = 3
b = 2
total = (a+b)**2
print(total)


num1+=5
num2+=5
compo = num1+num2
print(compo)


cost = int(input("enter number for comparsion"))
cost2 = int(input("enter other number for comparsion"))
print( cost>=cost2)
print(cost==cost2)
print(cost<=cost2)
print(cost!=cost2)
print( cost>cost2)
print( cost<cost2)


name = "priya"
year = "2028"
print(name =="priya" and year =="2028")
print(name =="priya" or year =="2028")

sample = True
print(not sample)

age = 4565806537537
brge = 4565806537537
print(age is brge)
print(age is not brge)


data = ["love", "gage","rest","freinds"]
print("love" in data)

product_cost = int(input("enter your value"))
discount = int(input("enter the discount"))
result = product_cost*discount/100
product_cost-=result
print(f"my discount is {result}")
print(f"after taking the discount i need to pay only {product_cost}")


# exponential
x = int(input("enter value for the base"))
y = int(input( "enter value for the power" ))
expone = x**y
print(expone)