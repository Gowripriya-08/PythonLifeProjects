number = [1,2,3,4,5,6,7,8,9,10,4,4,4,4]
print(number)
number.append("pythonlife")
number.append([22,34,55,67])
print(number)
number.extend([100,200,300])
print(number)
me = number.copy()
print(number.count(1))
print(number.index(4))
number.remove(4)
print(number)
obj = number.pop(1)
print(obj*32)
number.insert(1,"priya")
print(number)
print(number.reverse())

print(len(number))


#list compresion
empty_list = []

for i in range(1,11):
    result = i**2
    empty_list.append(result)
print(empty_list)

result = [i**2 for i in range(1,11)]
print(result)
result.sort(reverse=True)
print(result)

#
result = [i for i in range(11) if i%2 ==0]
print(result)

number = [1,2,3,4,5,6,7,8,9,10,10,3,1,1,1,1,]
for i in number:
    if i ==1:
        number.remove(i)
print(number)