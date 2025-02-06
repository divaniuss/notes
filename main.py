import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.title} ({self.created_at.strftime('%Y-%m-%d %H:%M:%S')})\n{self.text}"


class Manager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, text):
        self.notes.append(Note(title, text))

    def get_all_notes(self):
        return self.notes

    def find_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        return None

    def delete_note_by_title(self, title):
        self.notes = [note for note in self.notes if note.title != title]

    def save_to_file(self, file_path):
        try:
            with open(file_path, "w") as file:
                for note in self.notes:
                    file.write(str(note) + "\n\n")
            messagebox.showinfo("Успех", "Заметки сохранены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


manager = Manager()


def add_note():
    def save():
        title = entry_title.get()
        text = entry_text.get()
        if title and text:
            manager.add_note(title, text)
            add_window.destroy()
        else:
            messagebox.showwarning("Ошибка", "Заполните все поля")

    add_window = tk.Toplevel(root)
    add_window.title("Добавить заметку")
    add_window.geometry("400x300")

    tk.Label(add_window, text='Введите название:').pack()
    entry_title = tk.Entry(add_window, width=30)
    entry_title.pack()

    tk.Label(add_window, text='Введите текст:').pack()
    entry_text = tk.Entry(add_window, width=30)
    entry_text.pack()

    tk.Button(add_window, text="Сохранить", command=save).pack()


def view_notes():
    view_window = tk.Toplevel(root)
    view_window.title("Все заметки")
    view_window.geometry("400x300")

    notes = manager.get_all_notes()
    if notes:
        for note in notes:
            tk.Label(view_window, text=str(note)).pack()
    else:
        tk.Label(view_window, text="Заметок нет").pack()


def find_note():
    def search():
        title = entry_search.get()
        note = manager.find_note_by_title(title)
        label_result.config(text=str(note) if note else "Не найдено")

    find_window = tk.Toplevel(root)
    find_window.title("Поиск заметки")
    find_window.geometry("400x300")

    tk.Label(find_window, text="Введите название:").pack()
    entry_search = tk.Entry(find_window, width=30)
    entry_search.pack()

    tk.Button(find_window, text="Поиск", command=search).pack()

    label_result = tk.Label(find_window, text="")
    label_result.pack()


def delete_note():
    def delete():
        title = entry_delete.get()
        manager.delete_note_by_title(title)
        delete_window.destroy()

    delete_window = tk.Toplevel(root)
    delete_window.title("Удаление заметки")
    delete_window.geometry("400x300")

    tk.Label(delete_window, text="Введите название:").pack()
    entry_delete = tk.Entry(delete_window, width=30)
    entry_delete.pack()

    tk.Button(delete_window, text="Удалить", command=delete).pack()


def save_to_file():
    def save():
        file_path = entry_file.get()
        manager.save_to_file(file_path)
        save_window.destroy()

    save_window = tk.Toplevel(root)
    save_window.title("Сохранить в файл")
    save_window.geometry("400x300")

    tk.Label(save_window, text="Введите путь к файлу:").pack()
    entry_file = tk.Entry(save_window, width=30)
    entry_file.pack()

    tk.Button(save_window, text="Сохранить", command=save).pack()


def exit_app():
    root.quit()


root = tk.Tk()
root.title("Заметки")
root.geometry("600x600")

btn_add = tk.Button(root, text="Add Note", command=add_note)
btn_add.grid(row=0, column=0, padx=150, pady=100)

btn_view = tk.Button(root, text="View All Notes", command=view_notes)
btn_view.grid(row=0, column=1, padx=5, pady=5)

btn_find = tk.Button(root, text="Find Note by Title", command=find_note)
btn_find.grid(row=1, column=0, padx=5, pady=100)

btn_delete = tk.Button(root, text="Delete Note", command=delete_note)
btn_delete.grid(row=1, column=1, padx=5, pady=5)

btn_save = tk.Button(root, text="Save to .txt file", command=save_to_file)
btn_save.grid(row=2, column=0, padx=5, pady=80)

btn_exit = tk.Button(root, text="Exit", command=exit_app)
btn_exit.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()