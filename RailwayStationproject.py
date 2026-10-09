import random


class Train:
    def __init__(self, train_number, train_name, source, destination, seats):
        self.train_number = train_number
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.total_seats = seats
        self.available_seats = seats

    def display_train(self):
        print(
            f"{self.train_number:<12}"
            f"{self.train_name:<20}"
            f"{self.source:<15}"
            f"{self.destination:<15}"
            f"{self.available_seats}"
        )


class Passenger:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def display_passenger(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")


class Ticket:
    used_pnrs = set()

    def __init__(self, train, passengers, username):
        self.pnr = self.generate_pnr()
        self.train = train
        self.passengers = passengers
        self.username = username

    def generate_pnr(self):
        while True:
            pnr = random.randint(100000, 999999)
            if pnr not in Ticket.used_pnrs:
                Ticket.used_pnrs.add(pnr)
                return pnr

    def display_ticket(self):
        print("\n========== TICKET DETAILS ==========")
        print(f"PNR Number: {self.pnr}")
        print(f"Booked By: {self.username}")
        print(f"Train Number: {self.train.train_number}")
        print(f"Train Name: {self.train.train_name}")
        print(f"Route: {self.train.source} to {self.train.destination}")
        print(f"Number of Passengers: {len(self.passengers)}")

        print("\nPassenger Details:")
        for number, passenger in enumerate(self.passengers, start=1):
            print(f"\nPassenger {number}")
            passenger.display_passenger()

        print("====================================")


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tickets = []

    def check_password(self, password):
        return self.password == password

    def add_ticket(self, ticket):
        self.tickets.append(ticket)


class RailwayBookingSystem:
    def __init__(self):
        self.accounts = {}
        self.current_account = None

        self.trains = [
            Train(101, "Express A", "Hyderabad", "Chennai", 50),
            Train(102, "Superfast B", "Delhi", "Mumbai", 40),
            Train(103, "Intercity C", "Bangalore", "Hyderabad", 30),
            Train(104, "Passenger D", "Kolkata", "Delhi", 60)
        ]

    def get_integer(self, message, minimum=None, maximum=None):
        while True:
            try:
                value = int(input(message))

                if minimum is not None and value < minimum:
                    print(f"Please enter a number greater than or equal to {minimum}.")
                    continue

                if maximum is not None and value > maximum:
                    print(f"Please enter a number less than or equal to {maximum}.")
                    continue

                return value

            except ValueError:
                print("Invalid input. Please enter a number.")

    def create_account(self):
        print("\n========== CREATE ACCOUNT ==========")

        username = input("Enter username: ").strip()

        if username == "":
            print("Username cannot be empty.")
            return

        if username in self.accounts:
            print("Username already exists.")
            return

        password = input("Enter password: ")

        if len(password) < 4:
            print("Password must contain at least 4 characters.")
            return

        self.accounts[username] = Account(username, password)
        print("Account created successfully.")

    def login(self):
        print("\n============== LOGIN ===============")

        username = input("Enter username: ").strip()
        password = input("Enter password: ")

        if username in self.accounts:
            account = self.accounts[username]

            if account.check_password(password):
                self.current_account = account
                print("Login successful.")
                return

        print("Invalid username or password.")

    def logout(self):
        if self.current_account is not None:
            print(f"{self.current_account.username} logged out successfully.")
            self.current_account = None

    def display_trains(self):
        print("\n================ AVAILABLE TRAINS ================")
        print(
            f"{'Train No.':<12}"
            f"{'Train Name':<20}"
            f"{'Source':<15}"
            f"{'Destination':<15}"
            f"Available Seats"
        )
        print("-" * 80)

        for train in self.trains:
            train.display_train()

        print("-" * 80)

    def find_train(self, train_number):
        for train in self.trains:
            if train.train_number == train_number:
                return train

        return None

    def validate_phone(self):
        while True:
            phone = input("Enter phone number: ").strip()

            if phone.isdigit() and len(phone) == 10:
                return phone

            print("Phone number must contain exactly 10 digits.")

    def book_ticket(self):
        if self.current_account is None:
            print("Please log in before booking a ticket.")
            return

        self.display_trains()

        train_number = self.get_integer("Enter train number: ")
        train = self.find_train(train_number)

        if train is None:
            print("Train not found.")
            return

        if train.available_seats == 0:
            print("No seats are available on this train.")
            return

        passenger_count = self.get_integer(
            "Enter number of passengers: ",
            1,
            train.available_seats
        )

        passengers = []

        for number in range(1, passenger_count + 1):
            print(f"\nEnter details for Passenger {number}")

            name = input("Enter passenger name: ").strip()

            while name == "":
                print("Name cannot be empty.")
                name = input("Enter passenger name: ").strip()

            age = self.get_integer("Enter passenger age: ", 1, 120)
            phone = self.validate_phone()

            passenger = Passenger(name, age, phone)
            passengers.append(passenger)

        train.available_seats -= passenger_count

        ticket = Ticket(
            train,
            passengers,
            self.current_account.username
        )

        self.current_account.add_ticket(ticket)

        print("\nTicket booked successfully!")
        ticket.display_ticket()

    def view_bookings(self):
        if self.current_account is None:
            print("Please log in first.")
            return

        if len(self.current_account.tickets) == 0:
            print("You do not have any bookings.")
            return

        print("\n========== YOUR BOOKINGS ==========")

        for ticket in self.current_account.tickets:
            ticket.display_ticket()

    def cancel_ticket(self):
        if self.current_account is None:
            print("Please log in first.")
            return

        if len(self.current_account.tickets) == 0:
            print("You do not have any bookings.")
            return

        pnr = self.get_integer("Enter PNR number to cancel: ")

        for ticket in self.current_account.tickets:
            if ticket.pnr == pnr:
                ticket.train.available_seats += len(ticket.passengers)
                self.current_account.tickets.remove(ticket)
                Ticket.used_pnrs.remove(ticket.pnr)

                print("Ticket cancelled successfully.")
                return

        print("Ticket not found.")

    def user_menu(self):
        while self.current_account is not None:
            print("\n========== USER MENU ==========")
            print("1. Display Available Trains")
            print("2. Book Ticket")
            print("3. View My Bookings")
            print("4. Cancel Ticket")
            print("5. Logout")

            choice = self.get_integer("Enter your choice: ", 1, 5)

            if choice == 1:
                self.display_trains()

            elif choice == 2:
                self.book_ticket()

            elif choice == 3:
                self.view_bookings()

            elif choice == 4:
                self.cancel_ticket()

            elif choice == 5:
                self.logout()

    def run(self):
        while True:
            print("\n====== RAILWAY TICKET BOOKING SYSTEM ======")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = self.get_integer("Enter your choice: ", 1, 3)

            if choice == 1:
                self.create_account()

            elif choice == 2:
                self.login()

                if self.current_account is not None:
                    self.user_menu()

            elif choice == 3:
                print("Thank you for using the Railway Ticket Booking System.")
                break


if __name__ == "__main__":
    system = RailwayBookingSystem()
    system.run()