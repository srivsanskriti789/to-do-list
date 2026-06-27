class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. [{status}] {task['task']}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")


def main():
    todo = TodoList()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            try:
                num = int(input("Enter task number to complete: "))
                todo.complete_task(num - 1)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            todo.view_tasks()
            try:
                num = int(input("Enter task number to remove: "))
                todo.remove_task(num - 1)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()