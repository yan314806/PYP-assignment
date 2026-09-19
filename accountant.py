def add_payment():
    PaymentID=input("Please enter your Payment ID: ")
    BookingID=input("Please enter booking ID: ")
    UserID=input("Please enter user ID: ")
    TotalFee=input("Please enter total fee: ")
    AmountPaid=input("Please enter amount paid: ")
    Balance=input("Please enter balance: ")
    Status=input("Please enter payment status: ")
    PaymentDate=input("Please enter payment date (YYYY-MM-DD): ")
    payment=PaymentID+","+ BookingID +","+ UserID +","+ TotalFee +","+ AmountPaid+","+ Balance +"," + Status+"," + PaymentDate
    try:
        file=open("payment.txt","a")
        file.write(payment+"\n")
        file.close
        print("Your payment was successfuly added.")
    except:
        print("Payment could not be added. Please try again.")

def outstanding_payments():
    found=False
    try:
        with open("payment.txt","r") as file:
            file.readline() 
            for line in file:
                data=line.strip().split(",")
                Balance=float(data[5])
                if Balance>0:
                    print("PaymentID: ", data[0])
                    print("BookingID: ", data[1])
                    print("UserID: ", data[2])
                    print("Balance: ", data[5])
                    print("Status: ", data[6])
                    print()
                    found=True
        if found==False:
            print("You have no outstanding balances.")
    except:
        print("Payment file could not be read.")

def update_payments():
    client_ID=input("Please enter your Payment ID: ")
    new_amount=input("Please enter amount to be paid: ")
    new_balance=input("Please enter new balance: ")
    new_status=input("New payment status: ")
    try:
        file=open("payment.txt","r")
        lines=file.readlines()
        file.close()
        found=False
        new_lines=[]
        for line in lines:
            data=line.strip().split(",")
            if data[0]=="PaymentID":
                new_lines.append(line)
            elif data[0]==client_ID:
                data[4]=new_amount
                data[5]=new_balance
                data[6]=new_status
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
    total_income=0
    try: 
        file=open("payment.txt","r")
        file.readline()
        for line in file:
            data=line.strip().split(",")
            amount=float(data[4])
            total_income += amount
        file.close()
        print("The total income is: RM ",total_income)
    except:
        print("Could not generate income summary.")

def monthly_financial_summary():
    selected_month=input("Please input the selected month (YYYY-M): ")
    monthly_summary=0
    found=False
    try:
        file=open("payment.txt","r")
        file.readline()
        for line in file:
            data=line.strip().split(",")
            payment_date=data[7]
            payment_month=payment_date[0:6]
            if payment_month==selected_month:
                amount=float(data[4])
                monthly_summary += amount
                found=True
        file.close()
        if found==True:
            print("Income for ",selected_month,"is: RM ",monthly_summary)
    except:
        print("Could not compute the monthly financial summary.")

# add_payment()
# outstanding_payments()
# update_payments()
# income_summary()
# monthly_financial_summary()
















