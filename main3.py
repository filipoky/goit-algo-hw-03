

# clean = '   spacious   '.strip()
# print(clean) # spacious



# text = "Hello world"
# new_text = text.replace("world", "Python")
# print(new_text) 



# import re

# phone = """
#         Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612
#         """
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"\1\2\3"
# formatted_phone = (re.sub(pattern, replacement, phone)).strip()

# print(formatted_phone)


# one_line_text = "Textual data in Python is handled with str objects," \
#                 " or strings. Strings are immutable sequences of Unicode" \
#                 " code points. String literals are written in a variety " \
#                 " of ways: single quotes, double quotes, triple quoted."
# print(one_line_text)

# query = ("SELECT * "
#          "FROM some_table "
#          "WHERE condition1 = True "
#          "AND condition2 = False")
# print(query)


# text = "hello world"
# result = text.split()
# print(result)  # Виведе: ['hello', 'world']

# text = "apple,banana,cherry"
# result = text.split(',')
# print(result)  # Виведе: ['apple', 'banana', 'cherry']

# list_of_strings = ['Hello', 'world']
# result = ' '.join(list_of_strings)
# print(result)  # Виведе: 'Hello world'

# elements = ['earth', 'air', 'fire', 'water']
# result = ', '.join(elements)
# print(result)  # Виведе: 'earth, air, fire, water'


# text = "one fish, two fish, red fish, blue fish"
# new_text = text.replace("fish", "bird", 2)
# print(new_text)  

# text = "Hello, world!"
# new_text = text.replace(" world", "")
# print(new_text)

# html_text = "Hello &lt;user&gt;, welcome!"
# formatted_html = html_text.replace("&lt;", "<").replace("&gt;", ">")
# print(formatted_html)  
# # Виведе: Hello <user>, welcome!


# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)


# number = "12345"
# print(number.isdigit())  # Виведе: True

# text = "Number123"
# print(text.isdigit())  # Виведе: False

# user_input = input("Введіть число: ")
# if user_input.isdigit():
#     print("Це дійсно число!")
# else:
#     print("Це не число!")


# for char in "Hello 123":
#     if char.isdigit():
#         print(f"'{char}' - це цифра")
#     else:
#         print(f"'{char}' - не цифра")




# import re

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# def normalize_phone(phone_number):
    
#     return raw_numbers
# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# import re

# text = "Python - потужна, універсальна; мова!"
# pattern = r"[;,\-:!\.]"
# replacement = ""
# modified_text = re.sub(pattern, replacement, text)

# print(modified_text)  


# import re

# phone = "Михайло Куліш: 050-171-1634"
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"\1\2\3"
# formatted_phone = re.sub(pattern, replacement, phone)

# print(formatted_phone)



# import re

# phone_number = "    +38(050)123-32-34   "
# pattern = r"[^\d+]"
# replacement = ""
# cleaned_number = re.sub(pattern, replacement, phone_number.strip())
# print(cleaned_number)




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




