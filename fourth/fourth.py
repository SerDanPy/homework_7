"""Створи JSON-файл з інформацією про книги, кожна книга повинна мати:
Назву
Автора
Рік видання
Наявність (True або False)
Copy code
[
    {"назва": "Книга 1", "автор": "Автор 1", "рік": 2015, "наявність": true},
    {"назва": "Книга 2", "автор": "Автор 2", "рік": 2018, "наявність": false}
]
Напиши програму, яка:
Завантажує JSON-файл.
Виводить список доступних книг (наявність True).
Додає нову книгу в цей файл."""

import json


def load_and_filter_books(file_path: str) -> None:
    """Load JSON and list available books"""
    with open(file_path, 'r', encoding='utf-8') as f:
        books = json.load(f)
    available_books = [book for book in books if book['наявність']]
    print("Доступні книги:")
    for book in available_books:
        print(f"- {book['назва']}. Автор -- {book['автор']}")


def add_book(file_path: str, title: str, author: str, year: int, available: bool) -> None:
    """Add new book to JSON"""
    with open(file_path, 'r+', encoding='utf-8') as f:
        books = json.load(f)
        books.append({"назва": title, "автор": author, "рік": year, "наявність": available})
        f.seek(0)
        json.dump(books, f, indent=4, ensure_ascii=False)
    print(f"Додано книгу -- {title}, Автор -- {author}")


if __name__ == "__main__":
    file_path = "books.json"
    load_and_filter_books(file_path)
    add_book(file_path, "Книга 3", "Автор 3", 2025, True)
