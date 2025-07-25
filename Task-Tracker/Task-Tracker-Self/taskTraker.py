import json
import os

FILENAME = "Tasks.json"

def mainMenu():
    while True:
        print("\n========== Task-Tracker ==========")
        print("1 - Add new task")
        print("2 - Update task")
        print("3 - Delete task")
        print("4 - Show tasks")
        print("5 - Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            new_tasks()
        elif choice == "2":
            update_tasks()
        elif choice == "3":
            delete_tasks()
        elif choice == "4":
            get_list()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_tasks(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

def new_tasks():
    tasks = load_tasks()
    while True:
        task = input("Enter the name of task (or type 'exit' to return): ").strip()
        if task.lower() == "exit":
            break
        status = input("Enter the status of task: ").strip()
        new_id = str(len(tasks) + 1)
        tasks[new_id] = {"Task": task, "Status": status}
        save_tasks(tasks)
        print(f"Task '{task}' added.")

def update_tasks():
    tasks = load_tasks()
    get_list(tasks)
    ind = input("Enter the task number to update: ").strip()
    if ind not in tasks:
        print("Invalid task number!")
        return
    new_status = input("Enter new status: ").strip()
    tasks[ind]["Status"] = new_status
    save_tasks(tasks)
    print("Task updated!")

def delete_tasks():
    tasks = load_tasks()
    get_list(tasks)
    ind = input("Enter the task number to delete: ").strip()
    if ind not in tasks:
        print("Invalid task number!")
        return
    del tasks[ind]
    # Renumber IDs so tasks stay in order
    tasks = {str(i+1): v for i, v in enumerate(tasks.values())}
    save_tasks(tasks)
    print("Task deleted!")

def get_list(tasks=None):
    if tasks is None:
        tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour Tasks:")
    for k, v in tasks.items():
        print(f"{k}. {v['Task']} - [{v['Status']}]")

if __name__ == "__main__":
    mainMenu()
