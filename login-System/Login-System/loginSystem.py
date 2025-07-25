import json
import os
import hashlib

# ----------- Utility Functions -----------

def hash_password(password: str) -> str:
    """Hashes the password using SHA-256 and returns hex string."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_data() -> dict:
    """Loads user data from JSON file (returns empty dict if missing)."""
    if os.path.exists("userData.json"):
        with open("userData.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(data: dict):
    """Saves user data into JSON file."""
    with open("userData.json", "w") as file:
        json.dump(data, file, indent=4)

def username_exists(username: str) -> bool:
    """Checks if username already exists."""
    data = load_data()
    return username in data

# ---------- Core Features ----------

def sign_up():
    print("\n----- Sign-Up -----")
    username = input("Enter a username: ").strip()

    if not username:
        print("Error: Username cannot be empty.")
        return

    if username_exists(username):
        print(f"Error: Username '{username}' already exists.")
        return

    password = input("Enter a password: ").strip()
    if not password:
        print("Error: Password cannot be empty.")
        return

    hashed_pw = hash_password(password)

    # Save the new user
    data = load_data()
    data[username] = {"password": hashed_pw}
    save_data(data)

    print(f"Account created successfully for '{username}' (password stored securely).")

def login():
    print("\n----- Login -----")
    username = input("Enter your username: ").strip()
    if not username_exists(username):
        print(f"Error: Username '{username}' not found.")
        return

    password = input("Enter your password: ").strip()
    data = load_data()

    # Compare hashed password
    if data[username]["password"] == hash_password(password):
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Error: Incorrect password.")

def reset_password():
    print("\n----- Password Reset -----")
    username = input("Enter your username: ").strip()

    if not username_exists(username):
        print(f"Error: Username '{username}' not found.")
        return

    old_password = input("Enter your current password: ").strip()
    data = load_data()

    # Verify old password
    if data[username]["password"] != hash_password(old_password):
        print("Error: Current password is incorrect.")
        return

    new_password = input("Enter a new password: ").strip()
    if not new_password:
        print("Error: Password cannot be empty.")
        return

    data[username]["password"] = hash_password(new_password)
    save_data(data)
    print(f"Password updated successfully for '{username}'.")

# ---------- Menu System ----------

def menu():
    while True:
        print("\n========== User Management ==========")
        print("1. Sign Up")
        print("2. Login")
        print("3. Reset Password")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if not choice.isdigit():
            print("Error: Please enter a valid number (1-4).")
            continue

        choice = int(choice)
        if choice == 1:
            sign_up()
        elif choice == 2:
            login()
        elif choice == 3:
            reset_password()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select 1-4.")

# Run the program
if __name__ == "__main__":
    menu()
