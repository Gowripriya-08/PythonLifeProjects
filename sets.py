sample = {1,}
print(sample)
print(type(sample))
sample2 = set()
print(type(sample2))
sample3 = {1,2.3,"pythonlife",(1,2,3),36,36,36}
print(sample3)

# adding
sete = {32,36,"pythonlife"}
sete.add("welcome")
print(sete)

sample3.clear()
print(sample3)

sample3 = {1,2.3,"pythonlife",(1,2,3),36,36,36}
sample4 = sample3.copy()
print(sample4)

sample3.pop()
print(sample3)

sample4.remove("pythonlife")
print(sample4)

sample5 = {'cheke','love'}
sample4.update(sample5)
print(sample4)

#union
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)

set5 = set1.symmetric_difference(set2)
print(set5)

set6 = set1.difference(set2)
print(set6)

print(set1.isdisjoint(set2))

set10 = {1,2,3,4,5}
set20 = {1,2,3}
print(set10.issuperset(set20))
print(set20.issubset(set10))

seta = {1,2,3,4,5}
setb = frozenset(seta)
print(setb)


