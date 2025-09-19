"""Завдання 5: Робота з XML
Створи XML-файл, що містить інформацію про продукти магазину:
Назва продукту
Ціна
Кількість на складі
Copy code
<products>
    <product>
        <name>Молоко</name>
        <price>25</price>
        <quantity>50</quantity>
    </product>
    <product>
        <name>Хліб</name>
        <price>10</price>
        <quantity>100</quantity>
    </product>
</products>
2.Напиши програму, яка:
Читає XML-файл і виводить назви продуктів та їхню кількість.
Змінює кількість товару та зберігає зміни в XML-файл."""

import xml.etree.ElementTree as ET


def read_and_display_products(file_path: str) -> None:
    """Read XML and display product names and quantities"""
    tree = ET.parse(file_path)
    root = tree.getroot()
    print("===Інформація===")
    for product in root.findall('product'):
        name = product.find('name').text
        quantity = product.find('quantity').text
        print(f"- {name}: {quantity}")


def update_product_quantity(file_path: str, product_name: str, new_quantity: int) -> None:
    tree = ET.parse(file_path)
    root = tree.getroot()
    for product in root.findall('product'):
        if product.find('name').text == product_name:
            product.find('quantity').text = str(new_quantity)
            break
    tree.write(file_path)
    print(f"Було оновлено к-сть {product_name} до {new_quantity}")


if __name__ == "__main__":
    file_path = "products.xml"
    read_and_display_products(file_path)
    update_product_quantity(file_path, "Молоко", 75)
