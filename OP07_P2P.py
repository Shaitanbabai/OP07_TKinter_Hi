# Файл Дмитрия для Р2Р проверки
import tkinter as tk


def hi_user():
    name = entry.get()
    hi = "Привет, " + name + "!"
    label.config(text=hi)

root = tk.Tk()
root.title("Приветствие")

label = tk.Label(root, text="Введите ваше имя:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Приветствовать", command=hi_user)
button.pack()

root.mainloop()
