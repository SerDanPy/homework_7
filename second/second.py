"""Завдання 2: Робота з зовнішніми пакетами
Встанови пакет requests за допомогою pip.
Напиши скрипт, який завантажує сторінку з вказаного URL та зберігає її вміст у текстовий файл.
Додай обробку помилок на випадок, якщо сторінка недоступна."""

import requests


def download_page(url: str, output_file: str) -> None:
    """Download webpage and save to file"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"Успішно збережено у файл з іменем -- {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Помилка при завантаженні файлу -- {e}")


if __name__ == "__main__":
    download_page("https://google.com", "file.html")
