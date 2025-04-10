# Movie Ticket Booking System
def display_movies():
    print("1. Avengers: Endgame")
    print("2. Interstellar")
    print("3. Inception")

def book_ticket():
    movie = input("Enter movie name: ")
    seats = input("Enter number of seats: ")
    print(f"Booked {seats} tickets for {movie}!")

def check_seat_availability():
    print("Seats Available: 42")

def main():
    while True:
        print("\n--- Movie Ticket Booking System ---")
        print("1. Show Movies\n2. Book Ticket\n3. Check Seat Availability\n4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            display_movies()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            check_seat_availability()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

