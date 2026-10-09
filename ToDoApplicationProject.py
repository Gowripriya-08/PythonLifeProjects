class Task:
    def __init__(self, task_id, title):
        self.task_id = task_id
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def display_task(self):
        status = "Completed" if self.completed else "Not Completed"
        print(f"{self.task_id}. {self.title} - {status}")


class TodoList:
    def __init__(self):
        self.tasks = {}
        self.next_task_id = 1

    def add_task(self):
        title = input("Enter the task: ").strip()

        if title == "":
            print("Task cannot be empty.")
            return

        task = Task(self.next_task_id, title)
        self.tasks[self.next_task_id] = task
        self.next_task_id += 1

        print("Task added successfully.")

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
            return

        print("\n========== TASK LIST ==========")

        for task in self.tasks.values():
            task.display_task()

        print("===============================")

    def find_task(self, task_id):
        return self.tasks.get(task_id)

    def remove_task(self):
        self.display_tasks()

        if len(self.tasks) == 0:
            return

        try:
            task_id = int(input("Enter the task ID to remove: "))

            if task_id in self.tasks:
                del self.tasks[task_id]
                print("Task removed successfully.")
            else:
                print("Task not found.")

        except ValueError:
            print("Please enter a valid task ID.")

    def update_task(self):
        self.display_tasks()

        if len(self.tasks) == 0:
            return

        try:
            task_id = int(input("Enter the task ID to update: "))
            task = self.find_task(task_id)

            if task is None:
                print("Task not found.")
                return

            new_title = input("Enter the new task description: ").strip()

            if new_title == "":
                print("Task cannot be empty.")
                return

            task.title = new_title
            print("Task updated successfully.")

        except ValueError:
            print("Please enter a valid task ID.")

    def mark_task_completed(self):
        self.display_tasks()

        if len(self.tasks) == 0:
            return

        try:
            task_id = int(input("Enter the task ID to mark as completed: "))
            task = self.find_task(task_id)

            if task is None:
                print("Task not found.")
                return

            if task.completed:
                print("This task is already completed.")
            else:
                task.mark_completed()
                print("Task marked as completed.")

        except ValueError:
            print("Please enter a valid task ID.")

    def run(self):
        while True:
            print("\n====== TO-DO LIST APPLICATION ======")
            print("1. Add Task")
            print("2. Display Tasks")
            print("3. Update Task")
            print("4. Mark Task as Completed")
            print("5. Remove Task")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.display_tasks()

            elif choice == "3":
                self.update_task()

            elif choice == "4":
                self.mark_task_completed()

            elif choice == "5":
                self.remove_task()

            elif choice == "6":
                print("Thank you for using the To-Do List Application.")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_application = TodoList()
    todo_application.run()