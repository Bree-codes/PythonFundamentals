import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):  # Corrected: __init__ instead of _init_
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")

        # Task list
        self.tasks = []

        # Creating UI components
        self.task_label = tk.Label(root, text="Enter your task:")
        self.task_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.task_listbox = tk.Listbox(root, height=10, width=40, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
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

if __name__ == "__main__":  # Corrected: __main__ instead of _main_
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
