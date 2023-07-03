import json
from datetime import datetime

NOTES_FILE = "notes.json"

def create_note():
    note_id = input("Введите номер заметки: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "content": content,
        "created_at": created_at,
        "updated_at": created_at
    }
    return note

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
        return print("Файла не существует")

def list_notes(notes):
    if not notes:
        print("Нет доступных заметок.")
    else:
        print("Список заметок:")
        for note in notes:
            print("-----------------------")
            print("Идентификатор:", note["id"])
            print("Заголовок:", note["title"])
            print("Содержимое:", note["content"])
            print("Дата создания:", note["created_at"])
            print("Дата последнего изменения:", note["updated_at"])
        print("-----------------------")

def add_note():
    notes = load_notes()
    note = create_note()
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена")

def find_note_by_id(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None

def edit_note():
    note_id = input("Введите номер заметки для редактирования: ")
    notes = load_notes()
    note = find_note_by_id(notes, note_id)
    if note:
        print("Редактирование заметки:")
        new_title = input("Введите новый заголовок заметки: ")
        new_content = input("Введите новое содержимое заметки: ")
        note["title"] = new_title
        note["content"] = new_content
        note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes(notes)
        print("Заметка отредактирована.")
    else:
        print("Заметка с указанным номером не найдена.")

def delete_note():
    note_id = input("Введите номер заметки для удаления: ")
    notes = load_notes()
    note = find_note_by_id(notes, note_id)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("Заметка удалена.")
    else:
        print("Заметка с указанным номером не найдена.")

def note():
    while True:
        print("1- просмотр заметок")
        print("2- добавить заметку")
        print("3- редактировать заметку")
        print("4- удалить заметку")
        print("5- выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            notes = load_notes()
            list_notes(notes)
        elif choice == "2":
            add_note()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Не существует")
print("----------------------")

note()