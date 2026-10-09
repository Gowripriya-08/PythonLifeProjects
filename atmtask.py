# balance = 1000
# transactions = []


# def credit():
#     global balance

#     amount = float(input("Enter amount to credit: "))

#     if amount <= 0:
#         print("Please enter a positive amount.")
#     else:
#         balance += amount
#         transactions.append(f"Credited: +${amount}")
#         print(f"${amount} credited to your account.")


# def debit():
#     global balance

#     amount = float(input("Enter amount to debit: "))

#     if amount <= 0:
#         print("Please enter a positive amount.")
#     elif amount > balance:
#         print("Insufficient balance.")
#     else:
#         balance -= amount
#         transactions.append(f"Debited: -${amount}")
#         print(f"${amount} debited from your account.")


# def show_balance():
#     print(f"Your current balance is: ${balance}")


# def mini_statement():
#     print("\n----- MINI STATEMENT -----")

#     if len(transactions) == 0:
#         print("No transactions yet.")
#     else:
#         for transaction in transactions:
#             print(transaction)

#     print(f"Current Balance: ${balance}")
#     print("--------------------------")


# while True:
#     print("\nATM Menu:")
#     print("1. Credit")
#     print("2. Debit")
#     print("3. Balance")
#     print("4. Mini Statement")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == "1":
#         credit()

#     elif choice == "2":
#         debit()

#     elif choice == "3":
#         show_balance()

#     elif choice == "4":
#         mini_statement()

#     elif choice == "5":
#         print("Thank you for using the ATM. Goodbye!")
#         break

#     else:
#         print("Invalid choice. Please try again.")



# Atm project using oops concept

# class atm():
#     balance = 1000
#     transcation = []
#     def credit(self,):
#         amount = float(input("enter amount you want to credit:"))

#         if amount<= 0:
#             print(f"please enter the postive number")
#         else:
#             self.balance +=amount
#             self.transcation.append(f"credited: ${amount}")
#             print(f" the amount of {amount} is credited succesfully")
#     def debit(self):
#         amount = float(input("enter amount you want to debit: "))
#         if amount <=0:
#             print(f"plese enter a positive number")
#         elif amount >self.balance:
#             print("insuffcient balance ")
#         else:
#             self.balance -= amount
#             self.transcation.append(f"debited : {amount}")
#             print(f"the amount has been debited successfully")
#     def show_balance(self):
#         print(f" your balance is {self.balance}")
#     def mini_statement(self):
#         print(f"\n--------Mini Statement---------")
#         for i in self.transcation:
#             print(i)
#         print(f"Current Balance: ${self.balance}")
#         print("--------------------------")
# obj1 = atm()
# while True:
#     print("\nATM Menu:")
#     print("1. Credit")
#     print("2. Debit")
#     print("3. Balance")
#     print("4. Mini Statement")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == "1":
#         obj1.credit()

#     elif choice == "2":
#       obj1.debit()

#     elif choice == "3":
#         obj1.show_balance()

#     elif choice == "4":
#         obj1.mini_statement()

#     elif choice == "5":
#         print("Thank you for using the ATM. Goodbye!")
#         break

#     else:
#         print("Invalid choice. Please try again.")



## polymorphism and encasuplation
class ATM:
    def __init__(self):
        self.__balance = 1000
        self.__transaction = []

    # Encapsulation - credit controls access to balance
    def credit(self):
        amount = float(input("Enter amount you want to credit: "))

        if amount <= 0:
            print("Please enter a positive number")
        else:
            self.__balance += amount
            self.__transaction.append(f"Credited: ${amount}")
            print(f"The amount of ${amount} is credited successfully")

    # Encapsulation - debit controls access to balance
    def debit(self):
        amount = float(input("Enter amount you want to debit: "))

        if amount <= 0:
            print("Please enter a positive number")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            self.__transaction.append(f"Debited: ${amount}")
            print(f"The amount of ${amount} has been debited successfully")

    def show_balance(self):
        print(f"Your balance is ${self.__balance}")

    def mini_statement(self):
        print("\n-------- Mini Statement --------")

        for i in self.__transaction:
            print(i)

        print(f"Current Balance: ${self.__balance}")
        print("-------------------------------")

    # Polymorphism
    def show_message(self):
        print("Welcome to the ATM")


class StudentATM(ATM):
    def show_message(self):
        print("Welcome to the Student ATM")



# Object creation
obj1 = StudentATM()

obj1.show_message()

while True:
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Mini Statement")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        obj1.credit()

    elif choice == "2":
        obj1.debit()

    elif choice == "3":
        obj1.show_balance()

    elif choice == "4":
        obj1.mini_statement()

    elif choice == "5":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

