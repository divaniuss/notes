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


note1 = Note.create("Tema", "some text")
print(note1)