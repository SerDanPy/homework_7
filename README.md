# homework_7

Завдання 1: Створення власного пакету
Створи Python-пакет із наступною структурою:
Copy code
my_package/
├── __init__.py
├── math_utils.py
├── string_utils.py
└── main.py
Реалізуй у файлі math_utils.py функцію, яка обчислює факторіал числа, а також функцію для знаходження найбільшого спільного дільника двох чисел.
У файлі string_utils.py реалізуй функції для:
Перетворення тексту в верхній регістр.
Видалення пробілів на початку та в кінці рядка.
3. У файлі main.py імпортуй функції з модулів і продемонструй їх роботу, викликавши кожну з функцій.

Завдання 2: Робота з зовнішніми пакетами
Встанови пакет requests за допомогою pip.
Напиши скрипт, який завантажує сторінку з вказаного URL та зберігає її вміст у текстовий файл.
Додай обробку помилок на випадок, якщо сторінка недоступна.
2. Сховища даних (CSV, JSON, XML)

Завдання 3: Робота з CSV файлами
Створи CSV-файл з даними про студентів, де кожен рядок містить:
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
Додає нового студента до файлу.

Завдання 4: Робота з JSON
Створи JSON-файл з інформацією про книги, кожна книга повинна мати:
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
Додає нову книгу в цей файл.

Завдання 5: Робота з XML
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
Змінює кількість товару та зберігає зміни в XML-файл.
Додаткові завдання (реалізація паттерна "Адаптер" (Adapter)):
1) Перетворення між форматами:

Реалізуй класи, які перетворюватимуть CSV-файл до JSON та навпаки.
Додай функціонал для перетворення XML-файлу до JSON.
2) Уяви, що ти розробляєш систему для відправки повідомлень різними каналами: через SMS, Email та Push-повідомлення. Усі ці канали мають різні інтерфейси для відправки повідомлень, але ти хочеш уніфікувати їх, щоб використовувати один універсальний інтерфейс для відправки повідомлень незалежно від каналу.

Базова структура:
Створи інтерфейс MessageSender, який визначає метод для відправки повідомлення:
Copy code
class MessageSender:
    def send_message(self, message: str):
        pass
Існуючі класи:
Є три класи, кожен з яких реалізує власний метод для відправки повідомлень:
SMSService: має метод send_sms(phone_number, message).
EmailService: має метод send_email(email_address, message).
PushService: має метод send_push(device_id, message).
Створи ці класи з відповідними методами для відправки повідомлень.
Створення адаптерів:
Для кожного з класів (SMSService, EmailService, PushService) створи окремі адаптери, які будуть реалізовувати інтерфейс MessageSender. Адаптери мають використовувати відповідні методи існуючих класів для відправки повідомлень:
SMSAdapter: адаптує SMSService для використання через інтерфейс MessageSender.
EmailAdapter: адаптує EmailService.
PushAdapter: адаптує PushService.
Використання:
Напиши код, який створює екземпляри адаптерів для кожного типу сервісу (SMS, Email, Push) та відправляє повідомлення за допомогою універсального інтерфейсу MessageSender.
Додатково (опціонально):
Реалізуй систему відправки повідомлень, яка приймає список адаптерів і відправляє одне і те ж повідомлення через усі доступні сервіси.
Додай обробку помилок для кожного сервісу, якщо відправка повідомлення не вдалася.
Приклад коду:
Copy code
# Інтерфейс MessageSender
class MessageSender:
    def send_message(self, message: str):
        pass


# Існуючі класи для відправки повідомлень
class SMSService:
    def send_sms(self, phone_number, message):
        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    def send_email(self, email_address, message):
        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    def send_push(self, device_id, message):
        print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")


# Адаптери
class SMSAdapter(MessageSender):
    def __init__(self, sms_service, phone_number):
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str):
        self.sms_service.send_sms(self.phone_number, message)


class EmailAdapter(MessageSender):
    def __init__(self, email_service, email_address):
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str):
        self.email_service.send_email(self.email_address, message)


class PushAdapter(MessageSender):
    def __init__(self, push_service, device_id):
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str):
        self.push_service.send_push(self.device_id, message)


# Використання
sms_service = SMSService()
email_service = EmailService()
push_service = PushService()

sms_adapter = SMSAdapter(sms_service, "+380123456789")
email_adapter = EmailAdapter(email_service, "user@example.com")
push_adapter = PushAdapter(push_service, "device123")

# Відправка повідомлень через різні сервіси за допомогою адаптерів
message = "Привіт! Це тестове повідомлення."

sms_adapter.send_message(message)
email_adapter.send_message(message)
push_adapter.send_message(message)
Очікуваний результат:
Код має уніфікувати процес відправки повідомлень через різні сервіси, дозволяючи використовувати один загальний інтерфейс для роботи з різними типами повідомлень.
