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
    "4. View current bookings and user booking history\n"
    "5. Return to Main Menu\n")
    
    Option_chosen = input("Enter your option: ")
    
    if Option_chosen == "1":
        login.register_user()
    elif Option_chosen == "2":
        option_2()
    elif Option_chosen == "3":
        option_3()
    elif Option_chosen == "4":
        option_4()
    elif Option_chosen == "5":
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
        with open ("spaces.txt","r") as f:
            pass   
    elif Option == "2":
        pass

def option_3():
    print(
    "=====================================\n"
    "Choose from below options to continue\n"
    "=====================================\n" \
    "1. Process Cancellations\n" \
    "2. Process Extension\n"
    "3. Return\n")
    option = input("Enter your option: ")
    if option == "1":
        process_cancellations()
    elif option == "2":
        process_extensions()   
    elif option == "3":
        return   

def option_4():
    print(
    "=====================================\n"
    "Choose from below options to continue\n"
    "=====================================\n" \
    "1. View Current Bookings\n" \
    "2. View User Booking history\n"
    "3. Return\n")
    option = input("Enter your option: ")
    if option == "1":
        view_booking()
    elif option == "2":
        booking_history()   
    elif option == "3":
        return   

def process_cancellations():
    booking_id = input("Enter the booking ID you are trying to cancel(Type exit to leave): ").strip()
    booking_list = []
    found = False
    if booking_id.lower() == "exit":
        return
    else:
        with open ("booking.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                bookings = line.split(",")
                booking_list.append(bookings)
                if bookings[0] == booking_id:
                    found = True
                    print("BookingID Found!")
            if found is False:
                print("BookingID Doesn't Exist!")
                return
            cancel(booking_id, booking_list)

def cancel(booking_id, booking_list):
    for data in booking_list:
        if data[0] == booking_id:
            if data[6] == "Cancelled":
                print("BookingID is already cancelled!")
                return
            else:
                data[6] = "Cancelled"
    
    with open ("booking.txt", "w") as f:
        for line in booking_list:
            new_list = ",".join(line) + "\n"
            f.write(new_list)
        print("Booking Cancelled Successfully!")
    
def process_extensions():
    booking_id = input("Enter the booking ID you are trying to approve extention for(Type exit to leave): ").strip()
    booking_list = []
    found = False
    if booking_id.lower() == "exit":
        return
    else:
        with open ("booking.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                bookings = line.split(",")
                booking_list.append(bookings)
                if bookings[0] == booking_id:
                    found = True
                    print("BookingID Found!")
            if found is False:
                print("BookingID Doesn't Exist!")
                return
            extension(booking_id, booking_list)

def extension(bookingid, booking_list):
    for data in booking_list:
        if data [0] == bookingid:
            if data[6] == "Extended":
                print("BookingID had already been extended!")
                return
            elif data [6] == "Extension Requested":
                data[6] = "Extended"
            else:
                print("This booking did not request for extention.")
                return
        
    with open ("booking.txt", "w") as f:
        for line in booking_list:
            new_list = ",".join(line) + "\n"
            f.write(new_list)
        print("Booking Extended Successfully!")

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
    
    with open ("booking.txt", "r") as f:
        print(
            f"{'BookingID':<12}" f"{'Username':<13}" f"{'Date':<15}" f"{'Space':<10}" f"{'Start':<10}" f"{'End':<10}" f"{'Status':<10}")
        for line in f:
            line = line.strip()
            if not line:
                continue
            bookings = line.split(",")
            if bookings[6] != "Cancelled":
                print(
                    f"{bookings[0]:<12}" f"{bookings[1]:<13}" f"{bookings[2]:<15}" f"{bookings[3]:<10}" f"{bookings[4]:<10}" f"{bookings[5]:<10}" f"{bookings[6]:<10}")

def booking_history():
    username = input("Enter the username of the history you are looking for: ")
    try:
        with open("booking.txt", "r") as booking:
            print(f"{'BookingID':<12}" f"{'Username':<13}" f"{'Date':<15}" f"{'Space':<10}" f"{'Start':<10}" f"{'End':<10}" f"{'Status':<10}")
            for line in booking:
                line = line.strip()
                if not line:
                    continue
                bookings = line.split(",")
                if username == bookings[1]:
                    print(f"{bookings[0]:<12}" f"{bookings[1]:<13}" f"{bookings[2]:<15}" f"{bookings[3]:<10}" f"{bookings[4]:<10}" f"{bookings[5]:<10}" f"{bookings[6]:<10}")
    except FileNotFoundError:
        print("File Not Found. Please make a booking first.")

if __name__ == "__main__":
    booking_history()