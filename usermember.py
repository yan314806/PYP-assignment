def view_spaces():
    print("\n===== AVAILABLE SPACES =====")
    try:
        file = open("spaces.txt", "r")
        for line in file:
            if line.strip():
                print(line.strip())
        file.close()
    except:
        print("Cannot open spaces file.")


def check_conflict(space, date, start, end):
    try:
        file = open("booking.txt", "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) >= 7:
                if data[2] == date and data[3].lower() == space.lower():
                    if start < data[5] and end > data[4]:
                        file.close()
                        return True

        file.close()

    except:
        print("Cannot check booking.")

    return False


def request_booking():
    print("\n===== REQUEST BOOKING =====")

    booking_id = input("Booking ID: ")
    username = input("Username: ")
    date = input("Date: ")
    space = input("Desk/Room: ")
    start = input("Start time: ")
    end = input("End time: ")

    if end <= start:
        print("End time must be later.")
        return

    if check_conflict(space, date, start, end):
        print("Space is already booked at this time.")
        return

    booking = booking_id + "," + username + "," + date + "," + space + "," + start + "," + end + ",Pending"

    try:
        file = open("booking.txt", "a")
        file.write(booking + "\n")
        file.close()
        print("Booking request submitted.")
    except:
        print("Booking could not be added.")


def request_extension():
    booking_id = input("Booking ID: ")
    new_end = input("New end time: ")

    try:
        file = open("booking.txt", "r")
        lines = file.readlines()
        file.close()

        new_lines = []
        found = False

        for line in lines:
            data = line.strip().split(",")

            if len(data) >= 7 and data[0] == booking_id:
                found = True

                if new_end <= data[5]:
                    print("New time must be later.")
                    return

                data[5] = new_end
                data[6] = "Extension Requested"
                line = ",".join(data) + "\n"

            new_lines.append(line)

        file = open("booking.txt", "w")
        file.writelines(new_lines)
        file.close()

        if found:
            print("Extension request submitted.")
        else:
            print("Booking ID not found.")

    except:
        print("Could not update booking.")


def booking_history():
    username = input("\nUsername: ")
    found = False

    try:
        file = open("booking.txt", "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) >= 7 and data[1].lower() == username.lower():
                print("Booking ID:", data[0])
                print("Date:", data[2])
                print("Space:", data[3])
                print("Time:", data[4], "-", data[5])
                print("Status:", data[6])
                print()
                found = True

        file.close()

        if found == False:
            print("No booking history found.")

    except:
        print("Cannot open booking file.")


def payment_history():
    username = input("\nUsername: ")
    found = False

    try:
        file = open("payment.txt", "r")
        file.readline()

        for line in file:
            data = line.strip().split(",")

            if len(data) >= 8 and data[2].lower() == username.lower():
                print("Payment ID:", data[0])
                print("Booking ID:", data[1])
                print("Paid: RM", data[4])
                print("Balance: RM", data[5])
                print("Status:", data[6])
                print()
                found = True

        file.close()

        if found == False:
            print("No payment history found.")

    except:
        print("Cannot open payment file.")






#reference: Python Software Foundation. (2025). Input and output. Python 3 documentation. https://docs.python.org/3/tutorial/inputoutput.html
#reference: Python Software Foundation. (2025). Built-in types. Python 3 documentation. https://docs.python.org/3/library/stdtypes.html
