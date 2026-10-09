for i in range(10):
     
     if i == 3:
         break
     print(i)


liste = ["laxmi","chocklate","bannana","hero"]
for i in liste:
     if i == "bannana":
          print("i found the bannana")
          break
          
print(f"the last iteration is {i}")

items = ["ok","ok","ok","ok","defect","defect","ok","ok","good","defect","good"]
for i in items:
     if i == "defect":
         
          continue
     print(f"the item is {i}")


for i in range(10):
     pass
print(f"the last iteration is {i}")


name = "harsh"
if name =="harsh":
     pass