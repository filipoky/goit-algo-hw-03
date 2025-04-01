# print("Hello World")


# from datetime import datetime, date, timedelta

# def get_days_from_today(date):
#     def string_to_date(date_string):
#         return datetime.strptime(date_string, "%Y.%m.%d").date()
#     today = date.today()
#     return date.toordinal(today - date_string)


# from datetime import datetime, date

# def get_days_from_today(date_string):
#     input_date = datetime.strptime(date_string, "%Y.%m.%d").date()
#     today = date.today()
#     return today.toordinal() - input_date.toordinal()  
# # Тест
# print(get_days_from_today("2026.03.15"))  



from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()    # Перетворюємо рядкове представлення дати в об'єкт datetime
        today = datetime.today().date()                            # Отримуємо поточну дату
        difference = today.toordinal() - input_date.toordinal()    # Розраховуємо різницю в днях
        return difference
    
    except ValueError:
        # Якщо формат дати некоректний, повертаємо помилку
        return "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'."

# Тести
print(get_days_from_today("2026-10-09"))  # Приклад з датою в майбутньому
print(get_days_from_today("2022-02-24"))  # Приклад з датою в минулому
print(get_days_from_today("invalid-date"))  # Приклад з невірним форматом








# from datetime import datetime

# def get_days_from_today(date):
#     try:
#         input_date = datetime.strptime(date, "%Y-%m-%d").date()
#         today = datetime.today().date()
#         return (today - input_date).days  
#     except ValueError:
#         return "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'."

# # Тести
# print(get_days_from_today("2026-10-09"))  
# print(get_days_from_today("2022-02-24"))  
# print(get_days_from_today("invalid-date"))  



