"""Створи CSV-файл з даними про студентів, де кожен рядок містить:
Ім'я студента
Вік
Оцінку
Copy code
Ім'я,Вік,Оцінка
Петро,21,90
Марина,22,85
Андрій,20,88
Напиши програму, яка:
Читає дані з CSV-файлу.
Виводить середню оцінку студентів.
Додає нового студента до файлу."""

import csv


def read_and_process_csv(file_path: str) -> None:
    """Read CSV and calculate average"""
    total_grade = 0
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if 'Оцінка' not in reader.fieldnames:
            raise KeyError("Відсутня колонка 'Оцінка'")
        for row in reader:
            total_grade += int(row['Оцінка'])
            count += 1
    average = total_grade / count if count > 0 else 0
    print(f"Середня оцінка: {average:.2f}")


def add_student(file_path: str, name: str, age: int, grade: int) -> None:
    """Add new student"""
    with open(file_path, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, age, grade])
    print(f"Додано студента з іменем -- {name}. Вік -- {age}. Оцінка -- {grade}")


if __name__ == "__main__":
    file_path = "students.csv"
    add_student(file_path, "Петро", 21, 90)
    add_student(file_path, "Марина", 22, 85)
    add_student(file_path, "Андрій", 20, 88)
    read_and_process_csv(file_path)
