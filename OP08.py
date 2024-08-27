import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task[0])

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="blue")

def save_tasks():
    tasks = task_listBox.get(0, tk.END)
    with open('tasks.dat', 'wb') as file:
        pickle.dump(tasks, file)

def load_tasks():
    try:
        with open('tasks.dat', 'rb') as file:
            tasks = pickle.load(file)
            task_listBox.delete(0, tk.END)
            for task in tasks:
                task_listBox.insert(tk.END, task)
    except FileNotFoundError:
        messagebox.showinfo("Информация", "Сохраненные задачи не найдены.")

def edit_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task = task_listBox.get(selected_task[0])
        new_task = simpledialog.askstring("Редактировать задачу", "Измените вашу задачу:", initialvalue=task)
        if new_task:
            task_listBox.delete(selected_task[0])
            task_listBox.insert(selected_task[0], new_task)

root = tk.Tk()
root.title("Список задач")
root.configure(background='Hotpink')

text1 = tk.Label(root, text='Введите вашу задачу:', background='Hotpink', fg='White')
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, background='DeepPink1', fg='White')
task_entry.pack(pady=15, padx=15)

add_task_button = tk.Button(root, text='Добавить задачу', command=add_task)
add_task_button.pack(pady=15, padx=15)

delete_button = tk.Button(root, text='Удалить задачу', command=delete_task)
delete_button.pack(pady=15, padx=15)

mark_button = tk.Button(root, text='Отметить выполненным', command=mark_task)
mark_button.pack(pady=15, padx=15)

edit_button = tk.Button(root, text='Редактировать задачу', command=edit_task)
edit_button.pack(pady=15, padx=15)

save_button = tk.Button(root, text='Сохранить задачи', command=save_tasks)
save_button.pack(pady=15, padx=15)

load_button = tk.Button(root, text='Загрузить задачи', command=load_tasks)
load_button.pack(pady=15, padx=15)

text2 = tk.Label(root, text='Список задач:', background='Hotpink', fg='White')
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, background='gold')
task_listBox.pack(pady=15, padx=15)

root.mainloop()
