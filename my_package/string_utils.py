"""У файлі string_utils.py реалізуй функції для:
Перетворення тексту в верхній регістр.
Видалення пробілів на початку та в кінці рядка."""


def to_uppercase(text: str) -> str:
    return text.upper()


def trim_spaces(text: str) -> str:
    return text.strip()
