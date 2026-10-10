def menu():
    while True:
        print("""
=============================================== 
          FACILITIES STAFF MENU:
===============================================

1.View Room Avaliability & Status
2.Log Maintaince Record
3.Update Maintenance Status  
4.Generate Maintenance Summary
5.View Space Utilisation & Demand Tracking
6.Exit 
        """)

        option = input("Please enter your option : ").strip()
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
                Space_Utilisation_and_Demand_Tracking()
            case '6':
                print("Exiting...")
                break
            case _:
                print("Invalid choice")


def Maintenance_record():
    print("""
===============================================
           LOG MAINTENANCE RECORD
===============================================
    """)
    exist_room =[]
    record = []
    status = "Booked"
    roomID = input("Enter RoomID to book for maintenance (eg: R001, R002,...): ").strip().upper()
    exist = False
    
    try:
        with open('spaces.txt','r', encoding='utf-8') as f:
            for line in f:
                remove_line = line.strip()
                if remove_line == "":
                    continue
                separate = remove_line.split(",")
                exist_room.append(separate)

            if len(exist_room) == 0:
                            print("No rooms found in spaces.txt. Please add rooms first.")
                            return
            
            for i in exist_room:
                if i[0].strip().lower() == roomID.lower().strip():
                    exist = True
                    break
            
            if not exist:
                print(f"Room {roomID} does not exist. Please enter a valid RoomID.")
                return
            
    except FileNotFoundError:
        print('spaces.txt not found')
    except Exception:
        print("An error occured. Please try again later.")
    try:
        with open('Maintenance.txt','r', encoding='utf-8') as f:
            for line in f:
                remove_line = line.strip()
                if remove_line == "":
                    continue
                separate = remove_line.split(",")
                record.append(separate)
                
        for i in record:
            if i[0].strip().lower() == roomID.lower().strip():
                if i[4].strip().lower() == "booked" or i[4].strip().lower() == "ongoing":
                    print(f"Room {roomID} is unavaliable for now.")
                    print(f"Please try again later or choose another room.")
                    return    
                elif i[4].strip().lower() == "completed":
                    record.remove(i)
                    
    except FileNotFoundError:
        pass
    except Exception:
        print("An error occured. Please try again later.")
            
    date = input("Enter date : ").strip()
    task = input("Enter the task needed (Clean/Repair/IT Setup):  ").strip().title()
    task_description = input("Enter details of the task needed: ").strip().title()

    if roomID == "" or date == "" or task == "" or task_description == "":
        print("Please enter all values!")
        status = "Failed"
        return
    
    if task.lower() != "clean" and task.lower() != "repair" and task.lower() != "it setup":
        print("Invalid task choice. Please choose 1 from the 3")
        return
    
    log = [roomID, date, task, task_description, status] 
    log_history = [roomID, date, task, task_description, status]
    record.append(log)

    try:
        with open('Maintenance.txt','w', encoding='utf-8') as f:
            for i in record:
                f.write(f"{','.join(i)}\n")

        with open('Log_history.txt','a', encoding='utf-8') as f:
            f.write(f"{','.join(log_history)}\n")

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
==================================================
        UPDATE ROOM STATUS FOR MAINTENANCE
==================================================
     """)
    find = input("Enter RoomID to update: ").strip()
    find_lower = find.lower()
    if find == "":
        print("Please enter the roomID!")
        return

    exist = False
    readtxt = []
    try:
        with open('Maintenance.txt','r', encoding='utf-8') as f:
            for line in f:
                remove_line = line.strip()
                if remove_line == "":
                    continue
                separate = remove_line.split(",")
                readtxt.append(separate)

        for i in readtxt:
            if i[0].strip().lower() == find_lower:
                exist = True
                new_status = str(input(f"Update your maintenance status for {find} (Booked/Ongoing/Completed): ")).strip().lower()
                if new_status == 'booked' or new_status == 'ongoing' or new_status == 'completed':
                    i[4] = new_status.title()
                    print("Updated sucessfully")
                    break
                else:
                    print("Please enter valid status")
                    return

        if not exist:
            print(f"RoomID {find} hasn't been logged for maintenance yet. Please log it first.")
            return

        with open('Maintenance.txt','w',encoding= 'utf-8') as f:
            for i in readtxt:
                f.write(f"{','.join(i)}\n")
            
    except FileNotFoundError:
        print("Maintenance.txt not found")
    except Exception:
        print("Failed to update")

def Maintenance_report():
    print("""
================================================
        MAINTENANCE SUMMARY REPORT
================================================
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
                if remove == "":
                    continue
                split = remove.split(",")
                readtxt.append(split)

            for i in readtxt:
                total += 1
                if i[4].strip().lower() == "booked":
                    booked += 1
                if i[4].strip().lower() == "ongoing":
                    ongoing += 1    
                if i[4].strip().lower() == "completed":
                    completed += 1
                if i[2].strip().lower() == "clean":
                    clean += 1
                if i[2].strip().lower() == "repair":
                    repair += 1
                if i[2].strip().lower() == "it setup":
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
================================================
      VIEW ROOM AVAILABILITY & STATUS
================================================
    """)
    readdata = []
    Unavailable = []
    Avaliable = []
    all = []
    try:
        with open('spaces.txt','r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if stripped == "":
                    continue
                else:
                    divide = stripped.split(",")
                    all.append(divide)

                if len(all) == 0:
                    print("No rooms found in spaces.txt. Please add rooms first.")
                    return

    except FileNotFoundError:
        print("spaces.txt not found")
    except Exception:
        print("An error occured. Please try again later.")
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
                if i[4].strip().lower() == "booked":
                    Unavailable.append(i[0].strip())
                if i[4].strip().lower() == "ongoing":
                    Unavailable.append(i[0].strip())
                if i[4].strip().lower() == "completed":
                    Avaliable.append(i[0].strip())
                    
            for i in all:
                if i[0].strip() not in Unavailable and i[0].strip() not in Avaliable:
                    Avaliable.append(i[0].strip())

            if len(Avaliable) == 0:
                print("Available Rooms: 0")
            else:
                print(f"Available Rooms: {Avaliable}")

            if len(Unavailable) == 0:
                print("Unavailable Rooms: 0")
            else:
                print(f"Unavailable Rooms: {Unavailable}")

            for i in readdata:
                print(f"RoomID: {i[0].strip()} | Status: {i[4].strip()}")
                        
    except FileNotFoundError:
        print("Maintenance.txt not found")
    except Exception:
        print("An error occured. Please try again later.")

def Space_Utilisation_and_Demand_Tracking():
    print("""
=====================================================
      VIEW SPACE UTILISATION & DEMAND TRACKING
=====================================================
    """)
    counts = {}

    try:
        with open('Log_history.txt','r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if stripped == "":
                    continue
                else:
                    split = stripped.split(",")
                    roomID = split[0].strip()
                    counts[roomID] = counts.get(roomID, 0) + 1
                if len(counts) == 0:
                    print("No log records found.")

        print("Space Utilisation & Demand Tracking:")
        for roomID, count in counts.items():
            print(f"RoomID: {roomID} | Total Maintenance Records: {count}")

    except FileNotFoundError:
        print("Log_history.txt has not been created yet. Please log a maintenance record first.")
    except Exception:
        print("An error occured. Please try again later.")


if __name__ == "__main__":
    menu()
