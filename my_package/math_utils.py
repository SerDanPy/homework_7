"""Реалізуй у файлі math_utils.py функцію, яка обчислює факторіал числа, а також функцію для знаходження найбільшого спільного дільника двох чисел. """

def factorial(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Число повинно бути позитивним")
    return 1 if n == 0 else n * factorial(n - 1)

def ncd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a