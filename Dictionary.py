sample = {"user1":"gowri","user2":"priya","user3":"yellow"}
# sample.clear()
print(sample)

cleari = sample.copy()
print(cleari)
print(sample.keys())
print(sample.values())
print(sample.items())

sample1 = [('user1', 'gowri'), ('user2', 'priya'), ('user3', 'yellow')]
dictionary = dict(sample)
print(dictionary)

sample3 = {'user4':'anusha','user5':'priyanka'}
sample.update(sample3)
print(sample)

print(sample.get('user1'))
sample.pop('user1')
print(sample)
sample['user6'] = 'prashanthi'
print(sample)