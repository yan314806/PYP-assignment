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
    while option != "4":
        if option == "1":
            print(
            "=====================================\n"
            "Choose from below options to continue\n"
            "=====================================\n" \
            "1. Add Space\n" \
            "2. Update Space\n" \
            "3. Remove Space\n" \
            "4. Display Spaces\n" \
            "5. Return to Main Menu\n")
            sub_option = input("Enter your choice (1-5): ")
            if sub_option == "1":
                addSpace()
            elif sub_option == "2":
                updateSpace()
            elif sub_option == "3":
                removeSpace()
            elif sub_option == "4":
                display("spaces.txt")
            elif sub_option == "5":
                pass #Return to main menu
            else:
                print("Invalid choice. Please try again.")
        elif option == "2":
            displayAll()
        elif option == "3":
            print("Generating overall reports...")
            OverallReport()
        else:
            print("Invalid choice. Please try again.")
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
        line= line.split(",")
        if line[0].lower() == f"{SpaceID}".lower():
            print("Space ID already exists.")
            return
        
    # Check if the SpaceType is valid
    if SpaceType.lower() not in ["desk","room"]:
        print("Invalid space type. Please enter 'desk' or 'room'.")
        return

    # Append the new space to the file
    try:
        file = open("spaces.txt", "a")
        file.write(f"{SpaceID},{SpaceType}\n")
        file.close()
    except:
        print("Cannot open file")

# Update space type
def updateSpace():
    SpaceID = input("Enter space ID to update: ")
    spaces = ReadData("spaces.txt")
    found = False
    newSpaces = []

    for space in spaces:
        space = space.split(",")
        if space[0].lower() == f"{SpaceID}".lower():
            print("Found:", space)
            newSpaceType = input("Enter new space type(desk/room): ")
            if newSpaceType.lower() not in ["desk","room"]:
                print("Invalid space type. Please enter 'desk' or 'room'.")
                return
            space[1] = newSpaceType
            newSpaces.append(space[0] + "," + space[1])
            found = True
        else:
            newSpaces.append(space[0] + "," + space[1])

    if not found:
        print(f"Space ID: {SpaceID} not found.")
    else:
        # Write the updated spaces back to the file
        try:
            file = open("spaces.txt", "w")
            for space in newSpaces:
                file.write(space + "\n")
            file.close()
        except:
            print("Cannot open file")

def removeSpace():
    SpaceIDRemove = input("Enter space ID to remove: ")
    spaces = ReadData("spaces.txt")
    bookings = ReadData("booking.txt")
    newSpaces = []
    found = False

    # Check each space to see if it is booked
    for space in spaces:
        SpaceID, SpaceType = space.split(",")
        is_booked = False
        for booking in bookings:
            booking_data = booking.split(",")
            if booking_data[3].lower() == SpaceID.lower():
                if booking_data[2].lower() == str(current_datetime)[0:10]:
                    if booking_data[6].lower() != "cancelled":
                        is_booked = True
                        break

    if not is_booked:
        # Remove the space from the spaces list
        for i in range(len(spaces)):
            line = spaces[i].split(",")
            if line[0].lower() == f"{SpaceIDRemove}".lower():
                print("Found on line", i + 1, ":", spaces[i])
                print(f"Removing {SpaceIDRemove}, {line[1]}")
                found = True
            else:
                newSpaces.append(line[0] + "," + line[1])

    if not found:
        print(f"Space ID: {SpaceIDRemove} not found.")
    else:
        # Write the updated spaces back to the file
        try:
            file = open("spaces.txt", "w")
            for line in newSpaces:
                file.write(line + "\n")
            file.close()
        except:
            print("Cannot open file")

def displayAll():
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
            SpaceID, SpaceType = line.split(",")
            print(f"Space ID: {SpaceID}, Space Type: {SpaceType}")
    elif option == "2":
        users = ReadData("users.txt")
        print("All Users:")
        for line in users:
            username, password = line.split(",")
            print(f"Username: {username}, Password: {password}")
    elif option == "3":
        bookings = ReadData("booking.txt")
        print("All Bookings:")
        for line in bookings:
            Booking_ID,Username,Date,SpaceID,StartTime,EndTime,Status = line.split(",")
            print(f"Booking ID: {Booking_ID}, Username: {Username}, Date: {Date}, Space ID: {SpaceID}, Start Time: {StartTime}, End Time: {EndTime}, Status: {Status}")
    elif option == "4":
        payments = ReadData("payment.txt")
        print("All Payments:")
        for line in payments:
            PaymentID,BookingID,UserID,TotalFee,AmountPaid,PaymentDate,Balance,Status = line.split(",")
            print(f"Payment ID: {PaymentID}, Booking ID: {BookingID}, User ID: {UserID}, Total Fee: {TotalFee}, Amount Paid: {AmountPaid}, Payment Date: {PaymentDate}, Balance: {Balance}, Status: {Status}")
    elif option == "5":
        return
    else:
        print("Invalid choice. Please try again.")

def display(filename):
    spaces = ReadData(filename)
    print("All Spaces:")
    for line in spaces:
        SpaceID, SpaceType = line.split(",")
        print(f"Space ID: {SpaceID}, Space Type: {SpaceType}")
    

def OverallReport():
    total_bookings = 0
    # Read booking data
    booking_data = ReadData("booking.txt")
    for booking in booking_data:
        booking = booking.split(",")
        if booking[6].lower() == "confirmed":  # Assuming "confirmed" is the status for completed bookings
            total_bookings += 1

    # Read payment data and calculate total revenue
    payment_data = ReadData("payment.txt")
    total_revenue = 0
    for line in payment_data:
        line = line.split(",")
        total_revenue += float(line[4]) #Amount Paid is at index 4

    # Calculate high demand spaces
    HighDemandSpace, HighestCount = high_demand_spaces()

    print(
    "====================\n"
    "Overall Report\n"
    "====================\n"
    f"Total Bookings: {total_bookings}\n"
    f"Total Revenue: RM{total_revenue:.2f}\n"
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
        status = line[6].lower()
        SpaceID = line[3]
        if status == "confirmed":  # Only count confirmed bookings
            Spaces.append(SpaceID)

    if Spaces == []:
        return "No bookings", 0
    else:
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
                if booking_data[2].lower() == str(current_datetime)[0:10]:
                    if booking_data[6].lower() != "cancelled":
                        is_booked = True
                        break
        if not is_booked: 
            available.append(space)

    if available == []:
        print("No available spaces.")
    else:
        print(
            "==================\n"
            "Available Spaces:\n"
            "==================\n")
        for space in available:
            print(space)

#Reference: W3Schools (n.d.) Python Datetime. https://www.w3schools.com/python/python_datetime.asp



