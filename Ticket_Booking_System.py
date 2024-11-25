class Train:
    def __init__(self, total_seats=400):
        self.total_seats = total_seats
        self.available_seats = total_seats

    def display_seats(self):
        print(f"Available seats: {self.available_seats}")

    def book_seats(self):
        try:
            self.display_seats()
            seats_to_book = int(input("Enter the number of seats to book: "))
            if seats_to_book <= 0:
                print("Invalid input. Please enter a positive number.")
                return
            if seats_to_book > self.available_seats:
                print(f"Only {self.available_seats} seats are available. Please try again.")
                return
            self.available_seats -= seats_to_book
            print(f"Booking of {seats_to_book} seat(s) is confirmed!")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def book(self):
        while True:
            proceed = input("Do you want to book a seat? (Y/N): ").strip().upper()
            if proceed == "Y":
                self.book_seats()
                if self.available_seats == 0:
                    print("All seats are booked! No more bookings can be made.")
                    break
            elif proceed == "N":
                print("Thank you for visiting. Have a great day!")
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")


train = Train()
train.book()
