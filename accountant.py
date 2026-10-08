# System header
File_payments="payment.txt"
Late_Fee=200

def main_menu():
    while True:
        print(
        "===================================\n"
        "Accountant operations Menu\n"
        "===================================" 
    )
        print("\n1. Record new payment.")
        print("2. View outstanding payment(s).")
        print("3. Update payment.")
        print("4. Generate income summary.")
        print("5. Generate a monthly financial summary")
        print("6. Exit")

        choice=input("Please pick an option: ").strip()
        if choice=="1":
            record_payment()
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
        else:
            print("Value entered is invalid.")


def open_file(filename):
    record=[]
    try:
        file=open(filename,"r")
        for line in file:
            record.append(line.strip())
        file.close()
    except:
        print("File not found!")
    return record

def record_payment():
    print(
        "\n===============================\n"
        "Add new payment.\n"
        "==============================="
    )
#The option to add a new payment for a new client
# Asks user to input important details for record keeping 
    PaymentID=input("Please enter your Payment ID: ")
    BookingID=input("Please enter booking ID: ")
    UserID=input("Please enter user ID: ")

    try:
        TotalFee=float(input("Please enter total fee: "))
        AmountPaid=float(input("Please enter amount paid: "))
        #float() converts strings to numbers for comparison
        if TotalFee <=0 or AmountPaid<0:
            print("Amount entered is invalid.")
            return
        if AmountPaid>TotalFee:
            print("Amount paid cannot be greater that the total.")
            return
    except ValueError:
        print("Invalid number.")
        return
    
    PaymentDate=input("Please enter payment date (YYYY-MM-DD): ")
    methods={"1": "Cash", "2": "Online Payment", "3": "Credit card", "4": "Bank transfer"}
    print(methods)
    choice=input("Please pick your preffered payment method (1-4): ").strip()
    if choice not in methods:
        print("Invalid payment method.")
        return
    payment_method=methods[choice]

    Balance=(float(TotalFee)-float(AmountPaid))
    if Balance>0:
        Balance += Late_Fee
        print("A late fee of RM 200 has been added to your balance.")
        print(f"Your total balance is: RM {Balance}")


    Status="Paid" if Balance==0 else "Partial"
    
    payment=f"{PaymentID},{BookingID},{UserID},{str(TotalFee)},{str(AmountPaid)},{PaymentDate},{payment_method},{str(Balance)},{Status}" 
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
    print(
    "\n===============================\n"
    "List of incomplete payments.\n"
    "==============================="
    )
#Looks for any unfinished payments or balances
    found=False
    #helps to track whether something happened
    try:
        with open("payment.txt","r") as file:
            file.readline()
            for line in file:
                #loops through each payment row (header is skipped)
                data=line.strip().split(",")
                Balance=float(data[7])
                #converts the balance into a float
                if Balance>0:
                    print("\nPaymentID: ", data[0])
                    print("BookingID: ", data[1])
                    print("UserID: ", data[2])
                    print("Balance: ", data[7])
                    print("Status: ", data[8])
                    print()
                    found=True
                #Checks if balance is greater than 0 then updates the found statement to true
        if not found:
            print("You have no outstanding balances.")
    except FileNotFoundError:
        print("Payment file could not be read.")

def update_payments():
    print(
        "====================================\n"
        "Update existing payment status.\n"
        "====================================="
    )
#Function to edit an existing payment
    PaymentID=input("Please enter your Payment ID: ").strip() 
    try:
        file=open("payment.txt","r")
        lines=file.readlines()
        file.close()
        found=False
        new_lines=[]
        new_lines.append(lines[0])

        for line in lines[1:]:
        #Reads all lines into a list
            data=line.strip().split(",")

            if data[0]==PaymentID:
                found=True
                Balance=float(data[7])
                print("Your current balance is: RM ",Balance)

                try:
                    new_amount=float(input("Please enter amount to be paid: "))
                except ValueError:
                    print("Invalid amount entered.")
                    return
                
                if new_amount>Balance:
                    print("Amount entered is greater than your balance!")
                    return

                new_balance=Balance-new_amount

                if new_balance==0:
                    new_status="Paid"
                else:
                    new_status="Partial"
                data[4]=str(float(data[4]) + float(new_amount))
                #Adds the new paid amount to the original one
                data[7]=str(new_balance)
                data[8]=new_status
                new_line=",".join(data) + "\n"
                new_lines.append(new_line)

                print("Payment updated successfully.")
                print(f"Your new balance is: RM {new_balance}")
                print(f"Your new payment status is {new_status}")

            else:
                new_lines.append(line)

        if not found:
            print("ID not found.")
            return
            
        file=open("payment.txt","w")
        file.writelines(new_lines)
        file.close()

        print("Payment update successful.")
    except (OSError,IndexError,ValueError):
        print("Could not update payment.")

def income_summary():
    print(
        "=============================\n"
        "Generating total income.\n"
        "============================="
    )
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
        print("Total income is: RM ",total_income)
    except:
        print("Could not generate income summary.")

def monthly_financial_summary():
    print(
        "=======================================\n"
        "Total income for a specific month.\n"
        "======================================="
    )
#Calculates total income for a month
    selected_month=input("Please input the selected month (YYYY-MM): ").strip()
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
            print(f"No payments found for {selected_month}")
    except:
        print("Could not compute the monthly financial summary.")

if __name__=="__main__":
    try:
        with open("payment.txt", "x") as file:
            file.write("PaymentID,BookingID,UserID,TotalFee,AmountPaid,PaymentDate,PaymentMethod,Balance,Status\n")
            file.close()
    except FileExistsError:
        pass
        
    main_menu()



















