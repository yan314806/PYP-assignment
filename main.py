import accountant
import booking
import facilities
import hub_administrator
import login
import usermember

def welcome_msg():
    print("""
=====================================================================
==            ==  ======  ==        ====    =======  ==   ==  ======
 ==          ==   ==      ==      ==    ==  ==   ==  === ===  ==
  ==   ==   ==    ====    ==      ==        ==   ==  == = ==  ====
   ====  ====     ==      ==      ==    ==  ==   ==  ==   ==  == 
    ==    ==      ======  =======   ====    =======  ==   ==  ======
=====================================================================
    """)

def role_check():
    staff = ["staff1", "staff2", "staff3", "staff4", "staff5"]
    username, password = login.login_user()
    if username in staff:
        staff_main_menu()
    else:
        normal_member_menu()
    
def staff_main_menu():
    while True:
        print("""
=====================================
Choose from the following options.
=====================================
1. Hub Administrator
2. Booking Officer
3. Accountant
4. Maintenance Staff
5. Exit
=====================================
            """)
        option = input("Enter Your Option: ")
        if option == "1":
            hub_administrator.hub_administrator_menu()
        elif option == "2":
            booking.booking_menu()
        elif option == "3":
            accountant.main_menu()
        elif option == "4":
            facilities.menu()
        elif option == "5":
            break

def normal_member_menu():
    while True:
        print("""
=====================================
Choose from the following options.
=====================================
1. Member
2. Exit
=====================================
            """)
        option = input("Enter Your Option: ")
        if option == "1":
            usermember.user_menu()
        elif option == "2":
            break


welcome_msg()
role_check()