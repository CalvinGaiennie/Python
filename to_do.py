import os

# File to store tasks
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = [task.strip() for task in file.readlines()]
    else:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

# Display tasks
def show_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nYour To-Do List is empty.")

# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added.')

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f'Task "{removed_task}" deleted.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Options:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()