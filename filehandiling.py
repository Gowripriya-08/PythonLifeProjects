# import os 
# fn = "demo.txt"
# nn = "sample.txt"
# os.rename(nn,fn)


file = open("demo.txt",mode ='r')
read_dat = file.read()
print(read_dat)
file.close()

file = open("demo.txt",mode ='r')
read_dat = file.readline()
print(read_dat)
file.close()

file = open("demo.txt",mode ='r')
read_dat = file.readlines()
print(read_dat)
file.close()

#  mode -a
file = open("demo.txt",mode ='a')
write_data = file.write("\n we are using append operation")
file.close()

file = open("demo1.txt",mode ='a')
write_data = file.write("\n we are using append operation")
file.close()

# /write lines
voter = ["hey\n","stupid\n","hesss\n"]
file = open("demo.txt",mode = 'a')
write_data = file.writelines(voter)
file.close()

# mode w 
file = open("demo123.txt",mode = 'w')
write_data = file.write("\n welcome to python life")
file.close()

# mode = w+
file = open("demo123.txt",mode = 'w+')
write_data = file.write("\n join by 8 am")

print(file.tell())
file.seek(0)
read_data =file.read()
print(read_data)
file.close()

# rename file

# mode a+ is to append and read together
file = open("demo.txt",mode= 'a+')
write_data = file.write("\n i love you")
print(write_data)
file.close()

# mode r+  is to read and write together
file = open("demo1.txt",mode='r+')
read_data = file.read()
write_data = file.write("\n I love you")
print(write_data)
print(read_data)
file.close()
