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
    desk = input("Enter desk name: ")
    room = input("Enter room name: ")
    try:
        file = open("spaces.txt", "a")
        file.write(f"{desk}, {room}\n")
        file.close()
    except:
        print("Cannot open file")

def removeSpace():
    desk = input("Enter desk name to remove: ")
    room = input("Enter room name to remove: ")
    data = ReadData("spaces.txt")
    newData = []
    found = False
    for i in range(len(data)):
        line = data[i]
        if line.lower() == f"{desk}, {room}".lower():
            print("Found on line", i + 1, ":", line.strip())
            print(f"Removing {desk}, {room}")
            found = True
        if found == False:
            newData.append(line)
        found = False
    try:
        file = open("spaces.txt", "w")
        for line in newData:
            file.write(line + "\n")
        file.close()
    except:
        print("Cannot open file")

def display(fileName):
    spaces = ReadData(fileName)
    print("Current spaces:")
    for space in spaces:
        print(space)

if __name__ == '__main__':
    display("spaces.txt")
    print()
    addSpace()
    display("spaces.txt")
    print()
    removeSpace()
    display("spaces.txt")