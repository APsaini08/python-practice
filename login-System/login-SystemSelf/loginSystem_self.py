import json
import os
import hashlib

def menu():
    print("\n********** Main Menu **********")
    print("1. Login (if already registered)")
    print("2. Sign Up (if not registered)")
    print("3. Exit")

    val = input("Enter your choice: ")

    if not val.isdigit():  # Ensure input is a number
        print("Error: Please enter a valid number (1, 2, or 3)")
        return menu()

    val = int(val)  # Convert to int

    if val == 1:
        login()
    elif val == 2:
        sign_up()
    elif val == 3:
        print("Goodbye!")
        exit()
    else:
        print("Error: Enter a valid choice (1, 2, or 3)")
        menu()

def load_data():
    """Loads JSON data or returns an empty dict if not found/invalid."""
    if os.path.exists("userData.json"):
        with open("userData.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(data):
    """Saves the given dict to JSON file."""
    with open("userData.json", "w") as file:
        json.dump(data, file, indent=4)

def checkUsername(username):
    """Checks if a username exists."""
    data = load_data()
    return username in data

def sign_up():
    print("\n********** Welcome to Sign-Up Page **********")
    username = input("Enter a username: ")

    if checkUsername(username):
        print(f"Error: Username '{username}' already exists.")
        return menu()

    password = input("Enter a password: ")
    password = hashlib.sha256(password.encode()).hexdigest()
    # Load current data and add new user
    data = load_data()
    data[username] = {"password": password}
    save_data(data)

    print(f"Account created successfully for '{username}'!")
    menu()

def login():
    print("\n********** Welcome to Login Page **********")
    username = input("Enter your username: ")

    if not checkUsername(username):
        print(f"Error: Username '{username}' does not exist.")
        return menu()

    password = input("Enter your password: ")
    password = hashlib.sha256(password.encode()).hexdigest()

    data = load_data()

    if data[username]["password"] == password:
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Error: Incorrect password.")
    menu()

# Start the program
menu()
