# Перше завдання

from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()    # Перетворюємо рядкове представлення дати в об'єкт datetime
        today = datetime.today().date()                            # Отримуємо поточну дату
        difference = today.toordinal() - input_date.toordinal()    # Розраховуємо різницю в днях
        # або difference = (today - input_date).days
        return difference
    
    except ValueError:
        # Якщо формат дати некоректний, повертаємо помилку
        return "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'."

# Тести
print(get_days_from_today("2026-10-09"))  # Приклад з датою в майбутньому
print(get_days_from_today("2022-02-24"))  # Приклад з датою в минулому
print(get_days_from_today("invalid-date"))  # Приклад з невірним форматом




# Друге завдання

import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка, що всі параметри є цілими числами
    if not (isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)):
        return []
    
    # Перевірка коректності вхідних даних
    if not (1 <= min < 1000):  # Мінімум має бути в межах [1, 999]
        return []
    if not (1 < max <= 1000):  # Максимум має бути в межах [2, 1000]
        return []
    if not (min < max):  # Мінімум має бути менше за максимум
        return []
    if not (1 <= quantity <= (max - min + 1)):  # Кількість чисел має бути в межах між 1 і загальною кількістю унікальних чисел у діапазоні
        return []
    
    # Генерація унікальних випадкових чисел
    try:
        my_list = list(range(min, max + 1))
        chosen_list = random.sample(my_list, quantity)
        # Повернення відсортованого списку
        return sorted(chosen_list)
    
    except ValueError:
        return []

# Тести
print(get_numbers_ticket(1, 1000, 20))
print(get_numbers_ticket(-1, 1000, 20))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket("Hello", "in", "here"))
print(get_numbers_ticket(50, 1, 5))  
print(get_numbers_ticket(1, 10, 15))  
print(get_numbers_ticket(1, 10, -3))
print(get_numbers_ticket(1, 1001, 5))     
print(get_numbers_ticket(100, 50, 5))    
print(get_numbers_ticket(1, 49, 50))      
print(get_numbers_ticket(1, 49, 0))       
print(get_numbers_ticket(999, 1000, 2))
print(get_numbers_ticket(999, 1000, 6))
print(get_numbers_ticket(990, 1000, 6))
print(get_numbers_ticket(800, 990, 5))





# Третє завдання

import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр і знака '+'
    pattern = r"[^\d+]"     # Набір будь-яких символів, які НЕ є цифрою (0-9) і НЕ є знаком +
    replacement = ""
    cleaned_number = re.sub(pattern, replacement, phone_number.strip())
    # cleaned_number = re.sub(r"[^\d+]", "", phone_number.strip())
    
    # Якщо номер вже починається з '+380', повертаємо його без змін
    if cleaned_number.startswith("+380"):
        return cleaned_number
    
    # Якщо номер починається з '380', додаємо '+' попереду
    if cleaned_number.startswith("380"):
        return "+" + cleaned_number
    
    # Якщо номер починається з '0', додаємо '+38' попереду
    if cleaned_number.startswith("0"):
        return "+38" + cleaned_number
    
    # В інших випадках вважаємо номер некоректним
    return ""

# Тестові номери
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

