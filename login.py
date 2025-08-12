import tkinter as tk
import json
import os

# ------------------ Data Functions ------------------
def load_data(file):
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)
    with open(file, "r") as f:
        return json.load(f)

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ Signup Logic ------------------
def userSignup1(eid, epass):
    data = load_data("user.json")
    id = eid.get()
    password = epass.get()
    acc = {
        "id": id,
        "password": password
    }
    data.append(acc)
    save_data("user.json", data)

def userSignup():
    root.destroy()
    signup_window = tk.Tk()
    signup_window.title("Sign-Up")
    icon = tk.PhotoImage(file=r"C:\Users\Aditya\Desktop\login_icon_176905.png")
    signup_window.iconphoto(False, icon)

    signUp_label = tk.Label(signup_window, text="Enter user-id:-", padx=40, pady=20)
    eid = tk.Entry(signup_window, width=35, border=5)
    pass_label = tk.Label(signup_window, text="Generate your password:-", padx=40, pady=20)
    epass = tk.Entry(signup_window, width=35, border=5, show="*")

    signUp = tk.Button(signup_window, text="Sign-up", padx=10, pady=10, 
                       command=lambda: userSignup1(eid, epass))

    signUp_label.grid(row=1, column=0)
    eid.grid(row=2, column=0, padx=40, pady=5, columnspan=2)
    pass_label.grid(row=3, column=0)
    epass.grid(row=4, column=0, padx=40, pady=5, columnspan=2)
    signUp.grid(row=5, column=0, pady=10)

    signup_window.mainloop()


# ------------------ Login Logic ------------------
def login_user():
    user_id = eid.get()
    password = epass.get()
    data = load_data("user.json")
    for acc in data:
        if acc["id"] == user_id and acc["password"] == password:
            tk.Label(root, text="Login Successful ✅", fg="green").grid(row=6, column=0, columnspan=2)
            return
    tk.Label(root, text="Invalid ID or Password ❌", fg="red").grid(row=6, column=0, columnspan=2)

# ------------------ Main Window ------------------
root = tk.Tk()
icon = tk.PhotoImage(file=r"C:\Users\Aditya\Desktop\login_icon_176905.png")
root.iconphoto(False, icon)
root.title("Login-page")

login_label = tk.Label(root, text="Enter user-id:-", padx=40, pady=20)
eid = tk.Entry(root, width=35, border=5)
pass_label = tk.Label(root, text="Enter your password:-", padx=40, pady=20)
epass = tk.Entry(root, width=35, border=5, show="*")
login = tk.Button(root, text="Login", padx=10, pady=10, command=login_user)
signUp = tk.Button(root, text="Sign-up", padx=10, pady=10, command=userSignup)

login_label.grid(row=1, column=0)
eid.grid(row=2, column=0, padx=40, pady=5, columnspan=2)
pass_label.grid(row=3, column=0)
epass.grid(row=4, column=0, padx=40, pady=5, columnspan=2)
login.grid(row=5, column=0, pady=10)
signUp.grid(row=5, column=1, pady=10)

root.mainloop()
