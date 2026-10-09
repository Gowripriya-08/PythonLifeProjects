# import time # to find out the time
# def square(number):
#     print(f'square of numbers:')
#     for i in number:
#         time.sleep(0.2) # to find out the delay execution for a given number of seconds
#         print(f'squares :{i**2}')
# intial_time = time.time()
# list_1 =[1,2,3,4,5]
# square(list_1)
# print(f"time taken{time.time() - intial_time}")
#  # until 1st execution of this one the next wont be done


# def cubes(number):
#     print(f'square of numbers:')
#     for i in number:
#         time.sleep(0.2)
#         print(f'cubes :{i**3}')
# intial_time = time.time()
# list_1 =[1,2,3,4,5]
# cubes(list_1)
# print(f"time taken{time.time() - intial_time}")


import threading
import time
def square(number):
     print(f'square of numbers:')    
     for i in number:
        time.sleep(0.2) # to find out the delay execution for a given number of seconds
        print(f'squares :{i**2}')
def cubes(number):
    print(f'square of numbers:')
    for i in number:
        time.sleep(0.2)
        print(f'cubes :{i**3}')
intial_time = time.time()
list_1 =[1,2,3,4,5]
threa = threading.Thread(target=square ,args=(list_1,)) # comma is very important for tuple format 
t2 = threading.Thread(target=cubes,args=(list_1,))
threa.start() #for executiond 
t2.start()
threa.join() # to produce acurate timing
t2.join()
print(f"intial time {time.time()-intial_time}")

