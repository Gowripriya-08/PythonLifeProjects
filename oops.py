class Priya(): #class definition
    user_name = "mogali" 
    emp_id = 2082691
    def details(self): #methods
        print(f"he works in abc company {self.user_name}")
    def mogali(self):#methods
        print(f"he works in abc company {self.emp_id}")
priyamogali = Priya()
priyamogali.details()
priyamogali.mogali()
priyamogali.user_name
priyamogali.emp_id


#keypad phone

class Keypad():
    brand = "nokia"
    color = "black"
    model = 2015
    def call(self,person):
        print(f"you are calling {person}")
    def message(self,):
        print(f"you are calling form {self.brand}")
nokiaphone = Keypad()
nokiaphone.call("vinay")
nokiaphone.message()

samsung = Keypad()
samsung.call("vinay")
samsung.message()


class feature():
    def __init__(self,brand,color,model):
        self.brand = brand
        self.color = color
        self.model = model
    def calling(self):
        print(f"you are calling for m {self.brand}")
    def message (self,text):
        print(f"{text}message sent succesfully")
objname = feature("nokia","black",2015)
objname.calling()

samsung = feature("samsung","white",2022)
samsung.calling()

class smartphones(feature):
    
    def browsing(self,browsing):
        print(f"you are brwsing from {browsing}")
    def capture():
        print(f"you are capturing")


class laptop():
    def __init__(self,ram,storage,brand):
        self.ram = ram
        self.storage = storage
        self.brand = brand
    def display(self,a):
       print(f"this laptop is of brand {a}")
    def display2 (self):
        print(f"this laptop is very good laptop")
obj = laptop("512gb","16gb","lenovo")
obj.display("corei7")
obj.display2()
