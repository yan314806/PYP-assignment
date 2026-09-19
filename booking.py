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
