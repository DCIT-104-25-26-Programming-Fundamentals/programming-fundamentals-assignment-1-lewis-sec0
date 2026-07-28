def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks(tasks):
    if len(tasks) == 0:
        print("You have no tasks yet.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    choice = int(input("Enter task number to delete: "))

    if choice < 1 or choice > len(tasks):
        print("Error: Invalid task number.")
    else:
        removed = tasks.pop(choice - 1)
        print(f'Task "{removed}" has been removed.')


def show_menu():
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


# Main block
tasks = []

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Error: Invalid choice. Please enter a number between 1 and 4.")

    print()  # blank line for readability between menu cycles