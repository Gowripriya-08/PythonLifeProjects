sample = ()
print(sample)
print(type(sample))

sample = (1,2,3.5,True,{1,2,3},[1,2,3],"python")
print(sample)

sample1 = tuple()
print(type(sample1))

a = 1,2,3.5,True,'pythonlife'
print(a)

#  swapping of two variables
a = 10
b = 20
a,b = b,a
print(a)
print(b)

sample = (1,2,3.5,True,{1,2,3},[1,2,3],"python")
print(len(sample))

print(sample.index("python"))

tuple1 = (1,2,3)
tupe2 = (3,4,5)
print(tuple1+tupe2)

print(tuple1*3)

print(tuple1[0])
print(tuple1[-2])
print(tuple1[0:2])

tuplee = ()
print(all(tuplee))