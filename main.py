from datetime import datetime


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.title} ({self.created_at})\n{self.text}"


    def create(title, text):
        return Note(title, text)


class Manager:
    def __init__(self):
        self.notes = []

    def get_all_notes(self):
        return self.notes

    def find_note(self, title: str):
        return [note for note in self.notes if note.title == title]

    def delete_note(self, title: str):
        self.notes = [note for note in self.notes if note.title != title]


class Menu:
    def __init__(self):
        self.manager = Manager()

    def show_choices(self):
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Find Note by Title")
        print("4. Delete Note")
        print("5. Exit")

    def run(self):
        while True:
            self.show_choices()
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Введите название: ")
                text = input("Введите текст: ")
                note = Note.create(title, text)
                self.manager.notes.append(note)
                print("Добавлено")

            elif choice == "2":
                notes = self.manager.get_all_notes()
                if notes:
                    for note in notes:
                        print("\n")
                        print(note)
                        print("\n")
                else:
                    print("Заметок нету.")

            elif choice == "3":
                title = input("Введите названия для поиска: ")
                notes = self.manager.find_note(title)
                if notes:
                    for note in notes:
                        print("\n")
                        print(f"Заметка с названием {title}:")
                        print(note)
                        print("\n")
                else:
                    print("не найдена")

            elif choice == "4":
                title = input("Введите названия для удаления: ")
                self.manager.delete_note(title)
                print("Удалено.")
            elif choice == "5":
                print("Выход")
                break
            else:
                print("Введите число от 1 до 5")

menu = Menu()
menu.run()