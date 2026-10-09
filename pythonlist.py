listee = ["apple",1,3.5,[1,2,3],(1,2,3),{1,2,3},False]
print(listee)
print(type(listee))

# define list
sample = list()
print(sample)

# indexing
sample1= ["apple","banana","cherry","mango","grapes","kiwi","orange","watermelon"]
print(sample1[2])
print(sample1[-6])

print(sample1[0:3])
print(sample1[3:])
print(sample1[::3])

sample_list = [10,20,30,40,50,60,70,80,90]
#forward direction
print(sample_list[1:4])
print(sample_list[5:])
print(sample_list[:3])
print(sample_list[-8:-5])
print(sample_list[-9:-5])
print(sample_list[-3:])

# back ward direction
print(sample_list[::-1])
print(sample_list[6:2:-1])
print(sample_list[2::-1])
print(sample_list[3:1:-1])
print(sample_list[-2:-5:-1])
print(sample_list[-7:-10:-1])


mylist = [[1,2,3],[4,5,6],[7,8,9]]
print(mylist[1][2])