import login

def booking_menu():
    print(
    "========================\n"
    "Booking Coordinator Menu\n"
    "========================\n" \
    "Please Choose From the options below.\n" \
    "1. Register new users\n" \
    "2. Process desk and room bookings\n" \
    "3. Process cancellations and extensions\n" \
    "4. View current bookings and user booking history\n")
    
    Option_chosen = input("Enter your option: ")
    
    if Option_chosen == "1":
        login.register_user()
    elif Option_chosen == "2":
        option_2()
    elif Option_chosen == "3":
        pass
    elif Option_chosen == "4":
        pass

def option_2():
    print(
    "=====================================\n"
    "Choose from below options to continue\n"
    "=====================================\n" \
    "1. Process Desk Bookings\n" \
    "2. Process Room Bookings\n")
    Option = input("Enter your option: ")
    if Option == "1":
        pass
    elif Option == "2":
        pass




def booking():
    try:
        with open("booking.txt", "r") as booking:
            for line in booking:
                line = line.strip()
                if not line:
                    continue
                existing_booking = line.split(",")
                print(f"{existing_booking}found")
    except FileNotFoundError:
        print("File Not Found. Please make a booking first.")

def view_booking():
    try:
        with open("booking.txt", "r") as booking:
            for line in booking:
                line = line.strip()
                if not line:
                    continue
                existing_booking = line.split(",")
                print(f"Booking ID: {existing_booking[0]}, Name: {existing_booking[1]}, Date: {existing_booking[2]}")
    except FileNotFoundError:
        print("File Not Found. Please make a booking first.")

def booking_history():
    try:
        with open("booking.txt", "r") as booking:
            for line in booking:
                line = line.strip()
                if not line:
                    continue
                existing_booking = line.split(",")
                print(f"Booking ID: {existing_booking[0]}, Name: {existing_booking[1]}, Date: {existing_booking[2]}")
    except FileNotFoundError:
        print("File Not Found. Please make a booking first.")

if __name__ == "__main__":
    booking_menu()