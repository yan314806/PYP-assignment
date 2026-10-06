def open_file(filename):
    record=[]
    try:
        file=open(filename,"r")
        for line in file:
            record.append(line.strip())
        file.close
    except():
        print("File not found!")
    return record

def add_payment():
#The option to add a new payment for a new client
# Asks user to input important details for record keeping 
    PaymentID=input("Please enter your Payment ID: ")
    BookingID=input("Please enter booking ID: ")
    UserID=input("Please enter user ID: ")
    TotalFee=input("Please enter total fee: ")
    AmountPaid=input("Please enter amount paid: ")
    PaymentDate=input("Please enter payment date (YYYY-MM-DD): ")
    Balance=(float(TotalFee)-float(AmountPaid))
    Status="Paid" if Balance==0 else "Partial"
    payment=PaymentID+","+ BookingID +","+ UserID +","+ TotalFee +","+ AmountPaid+","+ PaymentDate+ ","+ str(Balance) +"," + Status 
    #Joins the specified data and separates them using commas(CVS)
    try:
        file=open("payment.txt","a")
        #Opens the file in append mode so that new payments are added to the end 
        file.write(payment+"\n")
        #Appends the new details on a new line
        file.close()
        #Closes the opened file
        print("Your payment was successfuly added.")
    except:
    #Error handling incase something goes wrong instead of crashing the whole program
        print("Payment could not be added. Please try again.")

def outstanding_payments():
#Looks for any unfinished payments or balances
    found=False
    #helps to track whether something happened
    try:
        with open("payment.txt","r") as file:
            file.readline()
            for line in file:
                #loops through each payment row (header is skipped)
                data=line.strip().split(",")
                Balance=float(data[6])
                #converts the balance into a float
                if Balance>0:
                    print("PaymentID: ", data[0])
                    print("BookingID: ", data[1])
                    print("UserID: ", data[2])
                    print("Balance: ", data[6])
                    print("Status: ", data[7])
                    print()
                    found=True
                #Checks if balance is greater than 0 then updates the found statement to true
        if not found:
            print("You have no outstanding balances.")
    except FileNotFoundError:
        print("Payment file could not be read.")

def update_payments():
#Function to edit an existing payment
    PaymentID=input("Please enter your Payment ID: ").strip()
    new_amount=float(input("Please enter amount to be paid: "))
    try:
        file=open("payment.txt","r")
        lines=file.readlines()
        file.close()
        found=False
        new_lines=[]
        for line in lines:
        #Reads all lines into a list
            data=line.strip().split(",")
            if data[0]=="PaymentID":
                new_lines.append(line)
                #Rebuilds the list
            elif data[0]==PaymentID:
                Balance=float(data[6])
                if new_amount>Balance:
                    print("Amount entered is greater than your balance!")
                    return
                new_balance=Balance-new_amount
                if new_balance==0:
                    new_status="Paid"
                else:
                    new_status="Partial"
                data[4]=str(new_amount)
                data[6]=str(new_balance)
                data[7]=new_status
                new_line=",".join(data) + "\n"
                new_lines.append(new_line)
                found=True
            else:
                new_lines.append(line)
        file=open("payment.txt","w")
        file.writelines(new_lines)
        file.close()
        if found==True:
            print("Payment updated successfully.")
        else:
            print("Payment ID not found.")
    except:
        print("Could not update payment.")

def income_summary():
#Calculates the total amount paid
    total_income=0
    #Sets the totatal income to 0
    try: 
        file=open("payment.txt","r")
        file.readline()
        for line in file:
            data=line.strip().split(",")
            amount=float(data[4])
            total_income += amount
            #Adds up amount paid column(4) for every record
        file.close()
        print("The total income is: RM ",total_income)
    except:
        print("Could not generate income summary.")

def monthly_financial_summary():
#Calculates total income for a month
    selected_month=input("Please input the selected month (YYYY-MM): ")
    #Allows user to choose which month to calculate total income
    monthly_summary=0
    found=False
    try:
        file=open("payment.txt","r")
        file.readline()
        for line in file:
            data=line.strip().split(",")
            payment_date=data[5]
            payment_month=payment_date[0:7]
            #Slices the date string with[0:7] to get the year and month part 
            #Counts the index from 0 to 6 to give 2026-09
            if payment_month==selected_month:
            #If it matches the selected month it is added to the running monthly summary
                amount=float(data[4])
                monthly_summary += amount
            found=True
        file.close()    
        if found:
            print("Income for ",selected_month,"is: RM ",monthly_summary)
        else:
            print("No payments found for that month")
    except:
        print("Could not compute the monthly financial summary.")

def main_menu():
    while True:
        print("1. Add payment.")
        print("2. View outstanding payment.")
        print("3. Update payment.")
        print("4. Generate income summary.")
        print("5. Generate a monthly financial summary")
        print("6. Exit")
        choice=input("Please pick an option: ").strip()
        if choice=="1":
            add_payment()
        elif choice=="2":
            outstanding_payments()
        elif choice=="3":
            update_payments()
        elif choice=="4":
            income_summary()
        elif choice=="5":
            monthly_financial_summary()
        elif choice=="6":
            print("Have a nice day!")
            break

main_menu()

# add_payment()
# outstanding_payments()
# update_payments()
# income_summary()
# monthly_financial_summary()
















