result = lambda a,b: a+b
print(result(10,10))

square = lambda x: x * x

print(square(5))

numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))

numbers = [1, 2, 3, 4, 5]

result = filter(lambda x: x > 2, numbers)

print(list(result))


from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)

