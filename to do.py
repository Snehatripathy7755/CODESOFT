import json
import os

# Constants
TODO_FILE = 'todo_list.json'

# Load the to-do list from a file
def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

# Save the to-do list to a file
def save_todo_list(todo_list):
    with open(TODO_FILE, 'w') as file:
        json.dump(todo_list, file, indent=4)

# Add a new task to the to-do list
def add_task(todo_list):
    task = input("What's the new task? ")
    todo_list.append({"task": task, "done": False})
    print("Task added!")

# View all tasks in the to-do list
def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list.")
        return
    for index, item in enumerate(todo_list):
        status = "Done" if item["done"] else "Not Done"
        print(f"{index + 1}. {item['task']} [{status}]")

# Update the status of a task
def update_task(todo_list):
    view_tasks(todo_list)
    task_number = int(input("Which task would you like to update? ")) - 1
    if 0 <= task_number < len(todo_list):
        todo_list[task_number]["done"] = not todo_list[task_number]["done"]
        print("Task updated!")
    else:
        print("Invalid task number.")

# Delete a task from the to-do list
def delete_task(todo_list):
    view_tasks(todo_list)
    task_number = int(input("Which task would you like to delete? ")) - 1
    if 0 <= task_number < len(todo_list):
        del todo_list[task_number]
        print("Task deleted!")
    else:
        print("Invalid task number.")

# Main application loop
def main():
    todo_list = load_todo_list()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("What would you like to do? ")
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            update_task(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            save_todo_list(todo_list)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()

