from datetime import datetime
current_datetime = datetime.now()

def hub_administrator_menu():
    print(
    "\n========================\n"
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
            "\n=====================================\n"
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
            "\n========================\n"
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
            if line.strip() != "":
                Store.append(line.strip())
        file.close()
    except:
        print("Cannot open file")
    return Store

def SpaceID_Validation(SpaceID):
    valid = True
    if SpaceID == "":
        print("Space ID cannot be empty.")
        valid = False  

    if SpaceID[0].lower() != "r" and SpaceID[0].lower() != "d":
        print("Invalid Space ID. It should start with 'R' for room or 'D' for desk.")
        valid = False

    if len(SpaceID) != 4 or not SpaceID[1:].isdigit():
        print("Invalid Space ID. It should follow the format start with 'R' or 'D' and followed by 3 digits")
        valid = False

    return valid

def addSpace():
    while True:
        newSpaceID = input("Enter space ID: ")
        spaces = ReadData("spaces.txt")
        price = input("Enter the price: ")
        SpaceID = []

        if newSpaceID == "":
            print("Space ID cannot be empty")
            continue

        if not SpaceID_Validation(newSpaceID):
            continue

        # Check if the SpaceID already exists
        for line in spaces:
            line = line.split(",")
            SpaceID.append(line[0].lower())

        if newSpaceID.lower() in SpaceID:
            print("Space ID already exists.")
            continue
        break   # Exit the loop if the SpaceID is valid
    while True:
        if not price.replace('.', '').isdigit():
            print("Invalid price. Please enter a valid number.")
            price = input("Enter new price for the space: ")
            continue
        break   # Exit the loop if the price is valid

    if newSpaceID[0].lower() == "r":
        SpaceType = "room"
    elif newSpaceID[0].lower() == "d":
        SpaceType = "desk"

    # Append the new space to the file
    try:
        file = open("spaces.txt", "a")
        file.write(f"{newSpaceID},{SpaceType},{price}\n")
        file.close()
        print(f"Space {newSpaceID} of type {SpaceType} with price: RM{price} added successfully.")
    except:
        print("Cannot open file")

# Update space type
def updateSpace():
    found = False
    newSpaces = []
    spaces = ReadData("spaces.txt")
    Dlargest = 0
    Rlargest = 0
    for space in spaces:
        space = space.split(",")
        SpaceID = space[0].lower()
        if SpaceID[0] == "d":
            if int(SpaceID[1:]) > Dlargest:
                Dlargest = int(SpaceID[1:])
        else:
            if int(SpaceID[1:]) > Rlargest:
                Rlargest = int(SpaceID[1:])

    while True:
        SpaceID = input("Enter space ID to update: ")
        SpaceIDList = []

        if SpaceID == "":
            print("Space ID cannot be empty")
            continue
        
        if not SpaceID_Validation(SpaceID):
            continue

        # Check if the SpaceID already exists
        for line in spaces:
            line = line.split(",")
            SpaceIDList.append(line[0].lower())

        if SpaceID.lower() not in SpaceIDList:
            print("Space ID not exists.")
            continue

        break  # Exit the loop if the SpaceID is valid

    for space in spaces:
        space = space.split(",")
        if space[0].lower() == SpaceID.lower():
            print("Found:", space)
            option = input("Do you want to update the space type or price? (1 for type, 2 for price, 3 for both): ").strip().lower()
            while option not in ["1","2","3"]:
                print("Invalid option. Please choose 1, 2, or 3.")
                option = input("Do you want to update the space type or price? (1 for type, 2 for price, 3 for both): ").strip().lower()
            
            if option == "1":
                if space[1].lower() == "desk":
                    newSpaceType = "room"
                else:
                    newSpaceType = "desk"
                if newSpaceType.lower() == "desk":
                    Dlargest += 1
                    newSpaceID = "D" + str(Dlargest).zfill(3) # zero padding method
                else:
                    Rlargest +=1
                    newSpaceID = "R" + str(Rlargest).zfill(3) # add 0 to the string until it reaches specific length
                newPrice = space[2]  # Keep the old price if only updating type
            elif option == "2":
                newPrice = input("Enter new price for the space: ")
                while not newPrice.replace('.', '').isdigit():
                    print("Invalid price. Please enter a valid number.")
                    newPrice = input("Enter new price for the space: ")
                newSpaceType = space[1]  # Keep the old type if only updating price
                newSpaceID = space[0]
            elif option == "3":
                if space[1].lower() == "desk":
                    newSpaceType = "room"
                else:
                    newSpaceType = "desk"
                if newSpaceType.lower() == "desk":
                    Dlargest += 1
                    newSpaceID = "D" + str(Dlargest).zfill(3) # zero padding method
                else:
                    Rlargest += 1
                    newSpaceID = "R" + str(Rlargest).zfill(3) # add 0 to the string until it reaches specific length
                newPrice = input("Enter new price for the space: ")
                while not newPrice.replace('.', '').isdigit():
                    print("Invalid price. Please enter a valid number.")
                    newPrice = input("Enter new price for the space: ")

            # Update the space with new values
            newSpaces.append(newSpaceID + "," + newSpaceType + "," + newPrice)
            found = True
        # If the space ID does not match, keep the original space data
        else:
            newSpaces.append(space[0] + "," + space[1] + "," + space[2])

    if not found:
        print(f"Space ID: {SpaceID} not found.")
    else:
        # Write the updated spaces back to the file
        try:
            file = open("spaces.txt", "w")
            for space in newSpaces:
                file.write(space + "\n")
            file.close()
            print(f"Space ID: {SpaceID} updated successfully. Below is new information for {SpaceID}")
            print(f"Space ID: {newSpaceID}, Space Type: {newSpaceType}, Price: {newPrice}")
        except:
            print("Cannot open file")

def removeSpace():
    spaces = ReadData("spaces.txt")
    bookings = ReadData("booking.txt")
    newSpaces = []
    found = False
    while True:
        SpaceIDRemove = input("Enter space ID to remove: ")
        SpaceIDList = []
        if SpaceIDRemove == "":
            print("Space ID cannot be empty")
            continue
        if not SpaceID_Validation(SpaceIDRemove):
            continue
        # Check if the SpaceID already exists
        for line in spaces:
            line = line.split(",")
            SpaceIDList.append(line[0].lower())

        if SpaceIDRemove.lower() not in SpaceIDList:
            print("Space ID not exists.")
            continue
        break

    # Check each space to see if it is booked
    is_booked = False
    for booking in bookings:
        booking_data = booking.split(",")
        if booking_data[3].lower() == SpaceIDRemove.lower():
            if booking_data[2].lower() == str(current_datetime)[0:10]:
                if booking_data[6].lower() != "cancelled":
                    is_booked = True
                    break

    if not is_booked:
        # Remove the space from the spaces list
        for i in range(len(spaces)):
            line = spaces[i].split(",")
            if line[0].lower() == SpaceIDRemove.lower():
                print("Found on line", i + 1, ":", spaces[i])
                print(f"Removing {SpaceIDRemove}, {line[1]}")
                found = True
            else:
                newSpaces.append(line[0] + "," + line[1] + "," + line[2])

    if is_booked:
        print(f"Space ID: {SpaceIDRemove} is currently booked and cannot be removed.")
    elif not found:
        print(f"Space ID: {SpaceIDRemove} not found.") 
    else:
        # Write the updated spaces back to the file
        try:
            file = open("spaces.txt", "w")
            for line in newSpaces:
                file.write(line + "\n")
            file.close()
            print(f"Space ID: {SpaceIDRemove} removed successfully.")
        except:
            print("Cannot open file")

def displayAll():
    print(
    "\n=====================================\n"
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
            SpaceID, SpaceType, Price = line.split(",")
            print(f"Space ID: {SpaceID}, Space Type: {SpaceType}, Price: {Price}")
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
        for i in range(1, len(payments)):  # Skip the header line
            line = payments[i]
            PaymentID,BookingID,UserID,TotalFee,AmountPaid,PaymentDate,Payment_Method,Balance,Status = line.split(",")
            print(f"Payment ID: {PaymentID}, Booking ID: {BookingID}, User ID: {UserID}, Total Fee: {TotalFee}, Amount Paid: {AmountPaid}, Payment Date: {PaymentDate}, Payment Method: {Payment_Method}, Balance: {Balance}, Status: {Status}")
    elif option == "5":
        return
    else:
        print("Invalid choice. Please try again.")

def display(filename):
    spaces = ReadData(filename)
    print("All Spaces:")
    for line in spaces:
        SpaceID, SpaceType, Price = line.split(",")
        print(f"Space ID: {SpaceID}, Space Type: {SpaceType}, Price: {Price}")

def OverallReport():
    total_bookings = 0
    # Read booking data
    booking_data = ReadData("booking.txt")
    for booking in booking_data:
        booking = booking.split(",")
        if booking[6].lower() == "confirmed": 
            total_bookings += 1

    # Read payment data and calculate total revenue
    payment_data = ReadData("payment.txt")
    total_revenue = 0
    for i in range(1, len(payment_data)):
        line = payment_data[i].split(",")
        if line[8].lower() == "paid" or line[8].lower() == "partial":  
            total_revenue += float(line[4]) #Amount Paid is at index 4

    # Calculate high demand spaces
    HighDemandSpace, HighestCount = high_demand_spaces()

    print(
    "\n====================\n"
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
            elif count == HighestCount:
                HighDemandSpace += f", {space}"  # Append space ID to the string if there's a tie

        return HighDemandSpace, HighestCount

def available_spaces():
    spaces = ReadData("spaces.txt")
    bookings = ReadData("booking.txt")
    available = []
    # Check each space to see if it is booked
    for space in spaces:
        SpaceID, SpaceType, Price = space.split(",")
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
            "\n==================\n"
            "Available Spaces:\n"
            "==================\n")
        for space in available:
            print(space)

#Reference: W3Schools (n.d.) Python Datetime. https://www.w3schools.com/python/python_datetime.asp
#Reference: W3Schools (n.d.) Python String zfill() Method https://www.w3schools.com/python/ref_string_zfill.asp


