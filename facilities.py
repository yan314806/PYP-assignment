option = ""
status = ""
print("""
    STAFF LOGIN""")

user = input(
"""Enter Staff ID (S01, S02, ....): 
         """).strip()

def menu():
    while True:
        option = input("""    
        FACILITIES STAFF MENU:

1.View Room Avaliability & Status
2.Log Maintaince Record
3.Update Maintenance Status  
4.Generate Maintenance Summary
5.Exit / Sign out

Please enter your option : 
        """).strip()

        match option:   
            case '1':
                view_avaliability_and_status()
            case '2': 
                Maintenance_record()
            case '3':
                Update_status()
            case '4': 
                Maintenance_report()
            case '5':
                print("Exiting...")
                break
            case _:
                print("Invalid choice")


def Maintenance_record():
    status = "Booked"
    roomID = input("Enter RoomID to book for maintenance (eg: R01, R02,...): ").strip()
    date = input("Enter date : ").strip()
    task = input("Enter the task needed (Clean/Repair/IT Setup):  ").strip().lower()
    task_description = input("Enter details of the task needed: ").strip()

    if task != "clean" and task != "repair" and task != "it setup":
        print("Invalid task choice. Please choose 1 from the 3")
        return

    if roomID == "" or date == "" or task == "" or task_description == "":
        print("Please enter all values!")
        status = "Failed"
        return
    else:
        print("Logging in progress...")

        log = user + "," + roomID + "," + date + "," + task + "," + task_description + "," + status 
        
        try:
            with open('Maintenance.txt','a', encoding='utf-8') as f:
                f.write(f"{log}\n")
        except FileNotFoundError:
            print("Maintenance.txt not found")
        except PermissionError:
            print("You do not have access")
        except Exception:
            print("Maintenance log failed")
        else: 
            print("Sucessfully logged!")
        finally:
            print("Returning back to menu...")

def Update_status():
    print("""
    UPDATE ROOM STATUS FOR MAINTENANCE
     """)
    find = input("Enter RoomID to update: ").strip()
    find_lower = find.lower()
    if find == "":
        print("Please enter the roomID!")
        return
    
    readtxt = []
    try:
        with open('Maintenance.txt','r', encoding='utf-8') as f:
            for line in f:
                    remove_line  = line.strip()
                    separate = remove_line.split(",")
                    readtxt.append(separate)

            for i in readtxt:
                if i[1].strip().lower() == find_lower:
                    if i[0].strip().lower() == user.lower():
                        new_status= str(input(f"Update your maintenance status for {find} (Booked/Ongoing/Comepleted): ")).strip().lower()
                        if new_status == 'booked' or new_status == 'ongoing' or new_status == 'completed':
                            i[5] = new_status
                            print("Updated sucessfully")
                        else:
                            print("Please enter valid status")
                            return
                    else:
                        print("Access denied. This maintenance record does not belong to you.")

        with open('Maintenance.txt','w',encoding= 'utf-8') as f:
            for i in readtxt:
                f.write(f"{','.join(i)}\n" )
            
    except FileNotFoundError:
        print("Maintenance.txt not found")
    except Exception:
        print("Failed to update")

def Maintenance_report():
    print("""
    MAINTENANCE SUMMARY REPORT
""")
    total = 0
    booked = 0
    ongoing = 0
    completed = 0
    clean = 0
    repair = 0
    It_setup = 0

    readtxt = []

    try:
        with open('Maintenance.txt','r', encoding = 'utf-8') as f:
            for i in f:
                 remove = i.strip()
                 split = remove.split(",")
                 readtxt.append(split)

            for i in readtxt:
                total += 1
                if i[5].strip().lower() == "booked":
                    booked += 1
                if i[5].strip().lower() == "ongoing":
                    ongoing += 1    
                if i[5].strip().lower() == "completed":
                    completed += 1
                if i[3].strip().lower() == "clean":
                    clean += 1
                if i[3].strip().lower() == "repair":
                    repair += 1
                if i[3].strip().lower() == "it setup":
                    It_setup += 1
        print(f""" 
Total : {total}
Total Booked : {booked}
Total Ongoing : {ongoing}
Total Completed : {completed}
Total Clean : {clean}
Total Repair : {repair}
Total IT Setup : {It_setup}
""")

    except FileNotFoundError:
        print("Maintenance.txt not found")
    except Exception:
        print("Error ocucured. Try again")

def view_avaliability_and_status():
    print("""
    VIEW ROOM AVAILABILITY & STATUS
    """)
    readdata = []
    Unavailable = []
    Avaliable = []

    try:
        with open('Maintenance.txt','r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if stripped == "":
                    continue
                else:
                    divide = stripped.split(",")
                    readdata.append(divide)

            for i in readdata:
                if i[5].strip().lower() == "booked":
                        Unavailable.append(i[1].strip())
                if i[5].strip().lower() == "ongoing":
                        Unavailable.append(i[1].strip())
                if i[5].strip().lower() == "completed":
                        Avaliable.append(i[1].strip())

            print(f"Available Rooms: {Avaliable}")
            print(f"Unavailable Rooms: {Unavailable}")
                        
    except FileNotFoundError:
        print("Maintenance.txt not found")
    except Exception:
        print("An error occured. Please try again later.")









if __name__ == "__main__":
    menu()

            