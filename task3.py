import hashlib

users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users_db:
        return "Username already exists."
    users_db[username] = hash_password(password)
    return "User created successfully."

def login(username, password):
    hashed = hash_password(password)
    if users_db.get(username) == hashed:
        return "Login Successful"
    else:
        return "Invalid credentials"

# Main loop
while True:
    print("\nChoose an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        print(register(username, password))

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        print(login(username, password))

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
