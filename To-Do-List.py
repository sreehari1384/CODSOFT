"""import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#0814bb")

        self.tasks = []

        self.title_label = tk.Label(root, text="Tasks for Today", font=("Helvetica", 16, "bold"), bg="#f4f4f4")
        self.title_label.pack(pady=10)

        self.task_frame = tk.Frame(root, bg="#f90404", bd=2, relief=tk.GROOVE)
        self.task_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(self.task_frame, font=("Helvetica", 12), selectbackground="#d3d3d3", activestyle="none")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.task_frame, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry_frame = tk.Frame(root, bg="#f4f4f4")
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=25, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_btn = tk.Button(self.entry_frame, text="Add", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
        self.add_btn.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(root, bg="#f4f4f4")
        self.button_frame.pack(pady=5)

        self.complete_btn = tk.Button(self.button_frame, text="Mark as Done", command=self.mark_done, bg="#2196F3", fg="white", width=15)
        self.complete_btn.pack(side=tk.LEFT, padx=5)

        self.delete_btn = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", width=12)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Empty Input", "Please enter a task.")
            return
        self.tasks.append({'task': task, 'done': False})
        self.task_entry.delete(0, tk.END)
        self.refresh_tasks()

    def mark_done(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a task to mark as done.")
            return
        index = selection[0]
        self.tasks[index]['done'] = not self.tasks[index]['done']
        self.refresh_tasks()

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a task to delete.")
            return
        index = selection[0]
        del self.tasks[index]
        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display = task['task']
            if task['done']:
                display = f"✔ {display}"
            self.task_listbox.insert(tk.END, display)
            if task['done']:
                self.task_listbox.itemconfig(tk.END, fg="gray", selectforeground="gray")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
"""
import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Task List ---")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter the new task: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully!")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter the updated task title: ")
            tasks[index]["title"] = new_title
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Mark task as complete")
    print("5. Delete a task")
    print("6. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            mark_task_complete(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
