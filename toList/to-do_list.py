def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task Status")
    print("4. Exit")


def add_task(tasks, task_id):
    task_name = input("Enter task name: ").strip()
    status = input("Enter task status (e.g., pending/done): ").strip()
    tasks[task_id] = {"task": task_name, "status": status}
    print(f"Task added with ID: {task_id}")
    return task_id + 1


def view_tasks(tasks):
    if not tasks:
        print("No tasks added yet.")
    else:
        print("\n------ TASK LIST ------")
        for id, task in tasks.items():
            print(f"[{id}] {task['task']} - {task['status']}")
        print("------------------------")


def update_task(tasks):
    try:
        task_id = int(input("Enter task ID to update: "))
        if task_id in tasks:
            new_status = input("Enter new status: ").strip()
            tasks[task_id]["status"] = new_status
            print(f"Task [{task_id}] updated to status: {new_status}")
        else:
            print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")


def main():
    tasks = {}
    task_id = 1

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            task_id = add_task(tasks, task_id)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
