import tkinter as tk


def greet_user():
    user_name = entry.get()  # Получить имя пользователя из поля ввода
    greeting = f"Привет, {user_name}!"  # Сформировать приветственное сообщение
    label["text"] = greeting  # Отобразить приветственное сообщение на лейбле


# Создать главное окно
window = tk.Tk()
window.title("Приветствие")

# Создать поле ввода для имени
label_name = tk.Label(window, text="Введите свое имя:")
label_name.pack()

entry = tk.Entry(window)
entry.pack()

# Создать кнопку для приветствия
button = tk.Button(window, text="Приветствовать", command=greet_user)
button.pack()

# Создать лейбл для отображения приветствия
label = tk.Label(window, text="")
label.pack()
window.mainloop()