print("Welcome to To-Do List")
print("Type 'exit' when all tasks are entered")

tasks = {}  # dictionary to store tasks
i = 1       # task ID counter

while True:
    job = input("Enter the job: ").lower()
    if job == 'exit':
        break
    status = input("Enter the status of the job: ")
    tasks[i] = {"task": job, "status": status}  # nested dictionary
    i += 1  # increment ID

# Print all tasks
print("\nYour To-Do List:")
for key, value in tasks.items():
    print(f"[{key}] {value['task']} - {value['status']}")

while True:
    print("If you want to update any task, enter its index (or 0 to exit):")
    ind = int(input(">>> "))

    if ind == 0:  # exit update loop
        break

    if ind in tasks:
        status = input("Enter the new status: ")
        tasks[ind]["status"] = status  # only update the status
        print(f"Task [{ind}] updated successfully!")
    else:
        print("Invalid index! Please try again.")

print("\nYour updated iTo-Do List:")
for key, value in tasks.items():
    print(f"[{key}] {value['task']} - {value['status']}")

