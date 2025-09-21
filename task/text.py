import tkinter as tk
from tkinter import filedialog, messagebox

# Основное окно приложения
root = tk.Tk()
root.title("Simple Python Text Editor")
root.geometry("800x600")

# Текстовое поле
text_area = tk.Text(root, wrap='word', undo=True)
text_area.pack(expand=1, fill='both')

# Функции для меню
def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))

def exit_editor():
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        root.destroy()

# Меню
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_editor)

menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

# Запуск приложения
root.mainloop()

