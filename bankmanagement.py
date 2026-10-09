
import random


# ================= ACCOUNT CLASS =================

class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Encapsulation
        self.__balance = 0
        self.__transactions = []

        # Generate account number
        self.account_number = random.randint(127000000, 127999999)

    def deposit(self, amount):

        if amount <= 0:
            print("Please enter a positive amount")
            return

        self.__balance += amount

        self.__transactions.append(
            f"Deposited: ${amount}"
        )

        print(f"Amount deposited: ${amount}")
        print(f"Current balance: ${self.__balance}")

    def withdraw(self, amount):

        if amount <= 0:
            print("Please enter a positive amount")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount

            self.__transactions.append(
                f"Withdrawn: ${amount}"
            )

            print(f"Amount withdrawn: ${amount}")
            print(f"Remaining balance: ${self.__balance}")

    def get_balance(self):

        return self.__balance

    def get_mini_statement(self):

        print("\n-------- MINI STATEMENT --------")
        print(f"Username: {self.username}")
        print(f"Account Number: {self.account_number}")

        if len(self.__transactions) == 0:
            print("No transactions yet")

        else:
            for transaction in self.__transactions:
                print(transaction)

        print(f"Current Balance: ${self.__balance}")
        print("--------------------------------")


# ================= SAVINGS ACCOUNT =================

class SavingsAccount(Account):

    def account_type(self):
        print("Account Type: Savings Account")


# ================= CURRENT ACCOUNT =================

class CurrentAccount(Account):

    def account_type(self):
        print("Account Type: Current Account")


# ================= BANKING SYSTEM =================

class BankingSystem:

    def __init__(self):

        # Stores username as key
        # Account object as value
        self.accounts = {}

    def create_account(self, username, password):

        if username in self.accounts:

            print("Username already exists")

        else:

            # Polymorphism
            account_type = input(
                "Enter account type (1-Savings / 2-Current): "
            )

            if account_type == "1":
                account = SavingsAccount(username, password)

            elif account_type == "2":
                account = CurrentAccount(username, password)

            else:
                print("Invalid account type")
                return

            self.accounts[username] = account

            print("\nAccount created successfully")
            print("------- Welcome to PYTHON Bank -------")
            print(f"Account Number: {account.account_number}")

    def login(self, username, password):

        if username in self.accounts:

            account = self.accounts[username]

            if account.password == password:

                print("\nLogin Successful!")
                return account

            else:

                print("Invalid password")

        else:

            print("Invalid username")

        return None


# ================= MAIN PROGRAM =================

bank = BankingSystem()


while True:

    print("\n========== PYTHON BANK ==========")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")


    # CREATE ACCOUNT
    if choice == "1":

        username = input("Enter username: ")
        password = input("Enter password: ")

        bank.create_account(username, password)


    # LOGIN
    elif choice == "2":

        username = input("Enter username: ")
        password = input("Enter password: ")

        account = bank.login(username, password)


        if account is not None:

            # Polymorphism
            account.account_type()

            while True:

                print("\n----- BANK ACCOUNT MENU -----")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Mini Statement")
                print("5. Logout")

                choice = input("Enter your choice (1-5): ")


                if choice == "1":

                    amount = float(
                        input("Enter amount to deposit: ")
                    )

                    account.deposit(amount)


                elif choice == "2":

                    amount = float(
                        input("Enter amount to withdraw: ")
                    )

                    account.withdraw(amount)


                elif choice == "3":

                    print(
                        f"Current balance: ${account.get_balance()}"
                    )


                elif choice == "4":

                    account.get_mini_statement()


                elif choice == "5":

                    print("\n-------- LOGGED OUT --------")
                    break


                else:

                    print("Invalid choice")


    # EXIT
    elif choice == "3":

        print("\n------ THANK YOU ------")
        print("Thank you for using Python Bank!")

        break


    else:

        print("Invalid choice. Please try again.")

