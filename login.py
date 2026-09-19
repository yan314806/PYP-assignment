def register_user():
    print("Username requirements: 3-10 characters, only letters/numbers/underscores allowed ")
    while True: #check block
        username = input("Enter your username: ").strip()
        if not validate_username(username):
            continue
        if check_user_exists(username):
            print("Username taken, please use another username.")
            continue
        break
    print("Password requirements: min 6 characters long, no space or commas allowed")
    while True:
        password = input("Enter your password: ").strip()
        if validate_password(password):
            break
    with open("users.txt", "a") as register:
        register.write(f"{username},{password}\n")
        print("Registered successfully!")

def validate_username(username):
    if len(username)<3 or len(username)>10:
        print("Too long! Username must be between 3 and 10 characters long.")
        return False
    for char in username:
        if not (char.isalnum() or char == "_"):
            print("Username cannot contain special characters or spaces.")
            return False
    return True

def validate_password(password):
    if len(password)<6:
        print("Password must be at least 6 characters long.")
        return False
    invalid_char = ", "
    if set(invalid_char).intersection(password):
        print("Password cannot contain spaces or commas.")
        return False
    return True

def check_user_exists(username):
    try:
        with open("users.txt", "r") as user:
            for line in user:
                line = line.strip()
                if not line:
                    continue
                existing_user = line.split(",")
                if existing_user[0].lower() == username.lower():
                    return True
    except FileNotFoundError:
        return False
    return False

def login_user():
    username, password = validate_login_username()
    validate_login_password(password)
    print(f"Welcome back, {username}!")
    return username, password

def validate_login_username():
    while True:
        username = input("Enter your username: ").strip()
        password = get_name_n_password(username)
        if get_name_n_password(username) is None:
            print("Username not found. Please register or try again.")
            continue
        return username, password

def get_name_n_password(username):
    try:
        with open("users.txt", "r") as validation:
            for line in validation:
                line = line.strip()
                if not line:
                    continue
                existing_user, existing_password = line.split(",")
                if existing_user.lower() == username.lower():
                    return existing_password
    except FileNotFoundError:
        return None
    return None

def validate_login_password(password):
    while True:
        correct_password = input("Enter your password: ").strip()
        if correct_password == password:
            print("Login successful!")
            return True
        else:
            print("Incorrect password. Please try again.")


register_user()