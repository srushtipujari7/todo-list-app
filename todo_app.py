import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple To-Do List Application")
        self.root.geometry("400x450")
        self.root.config(bg="#f0f0f0")

        # Title Label
        self.title_label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        # Entry Box for new tasks
        self.task_entry = tk.Entry(root, font=("Arial", 14), width=24)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=15, command=self.add_task)
        self.add_button.pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, font=("Arial", 12), width=30, height=10, selectbackground="#a6a6a6")
        self.task_listbox.pack(pady=10)

        # Delete Task Button
        self.delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12, "bold"), bg="#f44336", fg="white", width=15, command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()