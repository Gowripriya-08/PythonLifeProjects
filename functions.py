def function():
    print("welcome to python")
function()

def even(num1,num2):
    print(num1+num2)
even(4,6)

def number(num1,num2):
    return num1*num2
print(number(2,2))

def sample(*python):
    return python
obj = sample(5.7,6,2,3,4,5)
print(obj)

def sample(**a):
    return a
obj = sample(a=1,b=2,c=3)
print(obj)

def name(name="priya",year="sophomre"):
    print(name,year)
name()
name("vinay","junior")

def discount(price,dis=10):
    dis = (price*10)/100
    final_price = price - dis
    return final_price
print(discount(600,10))