# name = input("enter your name: ")

# list = """
# Rice      Rs 10/kg
# Sugar     Rs 8/kg
# Oil       Rs 30/liter
# Salt      Rs 25/kg
# Paneer    Rs 40/kg
# Maggie    Rs 12/pack
# Boost     Rs 200/bottle
# """

# price = 0
# pricelist = []
# totalprice = 0
# Finalprice = 0
# ilist = []
# qlist = []
# plist = []

# items = {'rice':10,'sugar':8,'oil':30,'salt':25,'panner':40,'maggie':12,'boost':200}

# while True:
#     choice = int(input("Press 1 for list or 2 to exit: "))
#     if choice ==2:
#         print("Thank you for shoping")
#         break
#     elif choice == 1:
#         print(list)

#         while True:
#             input1 = input("To buy press 1 or press 2 to exit: ")
#             if input1 == '2':
#                 print("Thank you for shopping")
#                 break
#             elif input1=='1':
#                 item = input("Choose your item: ").lower()

#                 while True:
#                     quantity = input("Enter the Quantity:")
#                     if quantity.isdigit():
#                         quantity_list= int(quantity)
#                         break
#                     else:
#                         print("please enter a valid quantity. ")
#                 if item in items:
#                     price = quantity_list*items[item]
#                     pricelist.append((item,quantity_list,items[item],price))
#                     totalprice+=price
#                 else:
#                     print("Selected item is not avaible,Sorry for the Incovninece.")
#         if totalprice >0:
#             tax = (totalprice*18)/100
#             Finalprice = tax+totalprice

#             print(25* "=","Pythonlife SuperMarket", 25*"=")
#             print(28*" ","Hyderbad")
#             print("Name:",name, 30*" ","August 22 2026")
#             print(75*"-")
#             print("sno",10*" ","items",8*" ",'quantity',8*" ",'price')
#             for i in range(len(pricelist)):
#                 print(i,13*" ",ilist[i],8*" ",qlist[i],8*" ",plist[i])
#             print(75*"-")
#             print(50*" ",'Total amount', 'Rs',totalprice)
#             print("Tax amount",50*" ",'Rs',tax)
#             print(75*"-")
#             print(50*" ",'Final Amount:', 'Rs',Finalprice)
#             print(75*"-")
#             print(20*" ","Thank you & Visit again")
#             print(75*"-")

name = input("enter your name: ")

list = """
Rice      Rs 10/kg
Sugar     Rs 8/kg
Oil       Rs 30/liter
Salt      Rs 25/kg
Paneer    Rs 40/kg
Maggie    Rs 12/pack
Boost     Rs 200/bottle
"""

price = 0
pricelist = []
totalprice = 0
Finalprice = 0

items = {
    'rice': 10,
    'sugar': 8,
    'oil': 30,
    'salt': 25,
    'paneer': 40,
    'maggie': 12,
    'boost': 200
}

while True:
    choice = int(input("Press 1 for list or 2 to exit: "))

    if choice == 2:
        print("Thank you for shopping")
        break

    elif choice == 1:
        print(list)

        while True:
            input1 = input("To buy press 1 or press 2 to exit: ")

            if input1 == '2':
                print("Thank you for shopping")
                break

            elif input1 == '1':
                item = input("Choose your item: ").lower()

                while True:
                    quantity = input("Enter the Quantity: ")

                    if quantity.isdigit():
                        quantity_list = int(quantity)
                        break
                    else:
                        print("Please enter a valid quantity.")

                if item in items:
                    price = quantity_list * items[item]

                    pricelist.append(
                        (item, quantity_list, items[item], price)
                    )

                    totalprice += price

                else:
                    print("Selected item is not available, Sorry for the inconvenience.")

        if totalprice > 0:
            tax = (totalprice * 18) / 100
            Finalprice = tax + totalprice

            print(25 * "=", "Pythonlife SuperMarket", 25 * "=")
            print(28 * " ", "Hyderabad")
            print("Name:", name, 30 * " ", "August 22 2026")
            print(75 * "-")

            print("sno", 10 * " ", "items", 8 * " ", "quantity", 8 * " ", "price")

            # FIXED PART
            for i in range(len(pricelist)):
                print(
                    i + 1,
                    13 * " ",
                    pricelist[i][0],
                    10 * " ",
                    pricelist[i][1],
                    12 * " ",
                    pricelist[i][3]
                )

            print(75 * "-")
            print(50 * " ", "Total amount", "Rs", totalprice)
            print("Tax amount", 50 * " ", "Rs", tax)
            print(75 * "-")
            print(50 * " ", "Final Amount:", "Rs", Finalprice)
            print(75 * "-")
            print(20 * " ", "Thank you & Visit again")
            print(75 * "-")
