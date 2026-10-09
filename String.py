string_one= 'priya'
print(string_one)
string_two = "priya came to work at 7'clock"
print(string_two)
string_three ='''priya said"i love coding" that did really touch my heart.'''
print(string_three)

my_string ="python life"

print(my_string[0])
print(my_string[-11])
print(len(my_string))

#slicing
print(my_string[0:6])
print(my_string[7::])
print(my_string[0::2])
print(my_string[::-1])
#negative dire
print(my_string[-11:-5])
print(my_string[-4:])
# back ward directing negative slicing
print(my_string[-6:-11:-1])
# back ward direction positive slicing
print(my_string[5:0:-1])

sample ="  PythonLife is the best amazing coding language  "
message = sample.upper()
message2 = sample.lower()
print(message)
print(message2)
print(sample.count("i"))
stripped_string = sample.strip()
print(stripped_string)
print(len(stripped_string))

splite = "pythonlife,12345,priya,teja"
data = splite.split(",")
print(data)

date = ['priya','teja']
joint = " ".join(date)

print(joint)

replace = sample.replace('PythonLife','java')
print(replace)
starts = sample.startswith("  PythonLife")
endse = sample.endswith("language  ")
print(starts)
print(endse)
pos_a = sample.find('P')
pos_i = sample.index('t')
print(pos_a)
print(pos_i)

name = "gowripriya"
capi = name.capitalize()
print(capi)
number = '12345'
is_alpha = name.isalpha()
is_numer = number.isdigit()
print(is_alpha)
print(is_numer)