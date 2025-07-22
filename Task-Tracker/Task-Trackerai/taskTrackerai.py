import json
import os
from datetime import datetime

FILENAME = "Tasks.json"

def mainMenu():
    while True:
        print("\n========== Task Tracker ==========")
        print("1 - Add new task")
        print("2 - Update task status")
        print("3 - Delete task")
        print("4 - Show tasks")
        print("5 - Filter tasks by status")
        print("6 - Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            filter_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

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

def add_task():
    tasks = load_tasks()
    while True:
        task = input("Enter the task name (or 'exit' to return): ").strip()
        if task.lower() == "exit":
            break
        status = input("Enter task status (pending/completed): ").strip().lower()
        if status not in ("pending", "completed"):
            print("Invalid status! Setting status as 'pending'.")
            status = "pending"
        new_id = str(len(tasks) + 1)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks[new_id] = {
            "Task": task,
            "Status": status,
            "Created": now,
            "Updated": now
        }
        save_tasks(tasks)
        print(f"Task '{task}' added.")

def update_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to update!")
        return
    show_tasks(tasks)
    ind = input("Enter the task number to update: ").strip()
    if ind not in tasks:
        print("Invalid task number!")
        return
    new_status = input("Enter new status (pending/completed): ").strip().lower()
    if new_status not in ("pending", "completed"):
        print("Invalid status. Update cancelled.")
        return
    tasks[ind]["Status"] = new_status
    tasks[ind]["Updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_tasks(tasks)
    print("Task updated!")

def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete!")
        return
    show_tasks(tasks)
    ind = input("Enter the task number to delete: ").strip()
    if ind not in tasks:
        print("Invalid task number!")
        return
    del tasks[ind]
    # Renumber IDs sequentially
    tasks = {str(i + 1): v for i, v in enumerate(tasks.values())}
    save_tasks(tasks)
    print("Task deleted!")

def show_tasks(tasks=None):
    if tasks is None:
        tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour Tasks:")
    for k, v in tasks.items():
        print(f"{k}. {v['Task']} - [{v['Status']}] (Created: {v['Created']}, Updated: {v['Updated']})")

def filter_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to filter!")
        return
    status = input("Show which tasks? (pending/completed): ").strip().lower()
    if status not in ("pending", "completed"):
        print("Invalid status filter!")
        return
    filtered = {k: v for k, v in tasks.items() if v["Status"] == status}
    show_tasks(filtered)

if __name__ == "__main__":
    mainMenu()
