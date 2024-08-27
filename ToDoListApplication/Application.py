import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("450x500")
        self.root.config(bg="#f0f0f0")

        # Task list
        self.tasks = []

        # Creating UI components
        self.task_label = tk.Label(root, text="Enter your task:", font=("Arial", 14), bg="#f0f0f0")
        self.task_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=35, font=("Arial", 12))
        self.task_entry.pack(pady=10, ipady=5)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.add_task_button.pack(pady=10)

        self.task_listbox = tk.Listbox(root, height=15, width=40, font=("Arial", 12), selectmode=tk.SINGLE, bg="#ffffff", activestyle="dotbox")
        self.task_listbox.pack(pady=20)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task, font=("Arial", 12), bg="#f44336", fg="white", padx=10, pady=5)
        self.delete_task_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

