import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_tasks()
        entry.delete(0, tk.END)

def remove_task():
    try:
        task = listbox.get(listbox.curselection())
        tasks.remove(task)
        update_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def update_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

root = tk.Tk()
root.title("Task Manager")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=5)

del_btn = tk.Button(root, text="Remove Task", command=remove_task)
del_btn.pack(pady=5)

root.mainloop()