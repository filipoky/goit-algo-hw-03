print("Hello World")


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
        # Перетворюємо рядкове представлення дати в об'єкт datetime
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Отримуємо поточну дату
        today = datetime.today().date()
        
        # Розраховуємо різницю в днях
        # difference = (today - input_date).days
        difference = today.toordinal() - input_date.toordinal()
        
        return difference
    
    except ValueError:
        # Якщо формат дати некоректний, повертаємо помилку
        return "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'."

# Тест
print(get_days_from_today("2026-10-09"))  # Приклад з датою в майбутньому
print(get_days_from_today("2022-02-24"))  # Приклад з датою в минулому
print(get_days_from_today("invalid-date"))  # Приклад з невірним форматом





