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

manager = Manager()

note1 = Note.create("Tema", "some text")
note2 = Note.create("Tema2", "some text2")


manager.notes.append(note1)
manager.notes.append(note2)

for note in manager.get_all_notes():
    print(note)
    print('\n')