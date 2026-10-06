from datetime import datetime
current_datetime = datetime.now()

def hub_administrator_menu():
    print(
    "========================\n"
    "Hub Administrator Menu\n"
    "========================\n" \
    "Please Choose From the Options Below.\n" \
    "1. Manage spaces\n" \
    "2. View All Data\n" \
    "3. Generate Overall Reports\n" \
    "4. Exit\n")

    option = input("Enter your choice (1-4): ")
    if option == "1":
        print(
        "=====================================\n"
        "Choose from below options to continue\n"
        "=====================================\n" \
        "1. Add Space\n" \
        "2. Remove Space\n" \
        "3. Display Spaces\n" \
        "4. Return to Main Menu\n")
        sub_option = input("Enter your choice (1-4): ")
        if sub_option == "1":
            addSpace()
        elif sub_option == "2":
            removeSpace()
        elif sub_option == "3":
            display()
        elif sub_option == "4":
            return
        else:
            print("Invalid choice. Please try again.")
    elif option == "2":
        display()
    elif option == "3":
        print("Generating overall reports...")
        OverallReport()
    elif option == "4":
        return
    else:
        print("Invalid choice. Please try again.")
        
def ReadData(fileName):
    Store = []
    try:
        file = open(fileName, "r")
        for line in file:
            Store.append(line.strip())
        file.close()
    except:
        print("Cannot open file")
    return Store

def addSpace():
    SpaceID = input("Enter space ID: ")
    SpaceType = input("Enter space type(desk/room): ")
    spaces = ReadData("spaces.txt")

    # Check if the SpaceID already exists
    for line in spaces:
        line= line.split(", ")
        if line[0].lower() == f"{SpaceID}".lower():
            print("Space ID already exists.")
            return
        
    # Check if the SpaceType is valid
    if SpaceType.lower() not in ["desk", "room"]:
        print("Invalid space type. Please enter 'desk' or 'room'.")
        return

    # Append the new space to the file
    try:
        file = open("spaces.txt", "a")
        file.write(f"{SpaceID}, {SpaceType}\n")
        file.close()
    except:
        print("Cannot open file")

def removeSpace():
    SpaceID = input("Enter space ID to remove: ")
    spaces = ReadData("spaces.txt")
    newSpaces = []
    found = False

    # Check if the space is associated with any bookings
    bookings = ReadData("booking.txt")
    for line in bookings:
        line = line.split(", ")
        if line[4].lower() == f"{SpaceID}".lower():
            if line[3].lower() == current_datetime[0:10]:
                print(f"Cannot remove space {SpaceID} as it is associated with booking ID {line[0]}.")
            return

    # Remove the space from the spaces list
    for i in range(len(spaces)):
        line = spaces[i].split(", ")
        if line[0].lower() == f"{SpaceID}".lower():
            print("Found on line", i + 1, ":", line.strip())
            print(f"Removing {SpaceID}, {line[1]}")
            found = True
        if found == False:
            newSpaces.append(line)
        found = False

    # Write the updated spaces back to the file
    try:
        file = open("spaces.txt", "w")
        for line in newSpaces:
            file.write(line + "\n")
        file.close()
    except:
        print("Cannot open file")

def display():
    print(
    "=====================================\n"
    "Choose from below options to continue\n"
    "=====================================\n" \
    "1. View All Spaces\n" \
    "2. View All Users\n" \
    "3. View All Bookings\n" \
    "4. View All Payments\n" \
    "5. Return to Main Menu\n")

    option = input("Enter your choice (1-5): ")
    if option == "1":
        spaces = ReadData("spaces.txt")
        print("All Spaces:")
        for line in spaces:
            SpaceID, SpaceType = line.split(", ")
            print(f"Space ID: {SpaceID}, Space Type: {SpaceType}")
    elif option == "2":
        users = ReadData("users.txt")
        print("All Users:")
        for line in users:
            username, password = line.split(", ")
            print(f"Username: {username}, Password: {password}")
    elif option == "3":
        bookings = ReadData("booking.txt")
        print("All Bookings:")
        for line in bookings:
            Booking_ID, Username, Date, SpaceID, StartTime, EndTime, Status = line.split(", ")
            print(f"Booking ID: {Booking_ID}, Username: {Username}, Date: {Date}, Space ID: {SpaceID}, Start Time: {StartTime}, End Time: {EndTime}, Status: {Status}")
    elif option == "4":
        payments = ReadData("payment.txt")
        print("All Payments:")
        for line in payments:
            PaymentID, BookingID, UserID, TotalFee, AmountPaid, PaymentDate, Balance, Status = line.split(", ")
            print(f"Payment ID: {PaymentID}, Booking ID: {BookingID}, User ID: {UserID}, Total Fee: {TotalFee}, Amount Paid: {AmountPaid}, Payment Date: {PaymentDate}, Balance: {Balance}, Status: {Status}")
    elif option == "5":
        return
    else:
        print("Invalid choice. Please try again.")

def OverallReport():
    # Read booking data
    booking_data = ReadData("booking.txt")
    total_bookings = len(booking_data)

    # Read payment data and calculate total revenue
    payment_data = ReadData("payment.txt")
    total_revenue = 0
    for line in payment_data:
        line = line.split(", ")
        total_revenue += float(line[4]) #Amount Paid is at index 4

    # Calculate high demand spaces
    HighDemandSpace, HighestCount = high_demand_spaces()

    print(
    "====================\n"
    "Overall Report\n"
    "====================\n"
    f"Total Bookings: {total_bookings}\n"
    f"Total Revenue: ${total_revenue:.2f}\n"
    f"High Demand Space: {HighDemandSpace} (Booked {HighestCount} times)\n")
    #Display available spaces
    available_spaces()

def high_demand_spaces():
    space_count = {}
    Spaces = []
    # Read booking data and count the occurrences of each space
    booking_data = ReadData("booking.txt")
    for line in booking_data:
        line = line.split(",")
        SpaceID = line[3]
        Spaces.append(SpaceID)

    for space in Spaces:
        space_count.setdefault(space,0)
        space_count[space] += 1

    # Find the space with the highest count
    HighestCount = 0
    HighDemandSpace = ""
    for space, count in space_count.items():
        if count > HighestCount:
            HighestCount = count
            HighDemandSpace = space

    return HighDemandSpace, HighestCount

def available_spaces():
    spaces = ReadData("spaces.txt")
    bookings = ReadData("booking.txt")
    available = []
    # Check each space to see if it is booked
    for space in spaces:
        SpaceID, SpaceType = space.split(",")
        is_booked = False
        for booking in bookings:
            booking_data = booking.split(",")
            if booking_data[3].lower() == SpaceID.lower():
                is_booked = True
                break
        if not is_booked:
            available.append(space)

    print(
        "==================\n"
        "Available Spaces:\n"
        "==================\n")
    for space in available:
        print(space)

#Reference: W3Schools (n.d.) Python Datetime. https://www.w3schools.com/python/python_datetime.asp



