"""3. У файлі main.py імпортуй функції з модулів і продемонструй їх роботу, викликавши кожну з функцій."""


from math_utils import factorial, ncd
from string_utils import to_uppercase, trim_spaces

def main():
    """math_utils"""
    print(f"Факторіал 5: {factorial(4)}")
    print(f"НСД чисел 48 та 18: {ncd(40, 10)}")

    print("------------------")

    """string_utils"""
    print(f"Перетворення тексту в верхній регістр 'ithillel': {to_uppercase('ithillel')}")
    print(f"Видалення пробілів на початку та в кінці рядка '  hey  ': {trim_spaces('  hey  ')}")

if __name__ == "__main__":
    main()