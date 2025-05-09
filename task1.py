users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def create_user(user_id, name, email):
    users.append({"id": user_id, "name": name, "email": email})
    return "User added."

def read_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return "User not found."

def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            return "User updated."
    return "User not found."

def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return "User deleted."

def display_menu():
    print("\nChoose an operation to perform:")
    print("1. Create user")
    print("2. Read user")
    print("3. Update user")
    print("4. Delete user")
    print("5. Exit")

while True:
    try:
        print("\n--- Enter User Information ---")
        user_id = int(input("Enter user ID: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
    except ValueError:
        print("Invalid input. ID must be an integer.")
        continue

    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(create_user(user_id, name, email))
    elif choice == "2":
        print(read_user(user_id))
    elif choice == "3":
        print(update_user(user_id, name, email))
    elif choice == "4":
        print(delete_user(user_id))
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
