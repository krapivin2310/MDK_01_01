import os
 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
 
def view_tasks(tasks):
    clear_screen()
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")
 
def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"'{task}' added to the list.")
 
def remove_task(tasks):
    if tasks:
        view_tasks(tasks)
        task_index = int(input("Enter the number of the task you want to remove: ")) - 1
        removed_task = tasks.pop(task_index)
        print(f"'{removed_task}' removed from the list.")
    else:
        print("Your To-Do List is empty.")
 
def main():
    tasks = []
 
    while True:
        print("\nTo-Do List Actions:")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Remove tasks")
        print("4. Quit")
 
        action = input("Choose an action: ")
 
        if action == "1":
            view_tasks(tasks)
        elif action == "2":
            add_task(tasks)
        elif action == "3":
            remove_task(tasks)
        elif action == "4":
            break
        else:
            print("Invalid choice, please try again.")
 
if name == "main":
    main()