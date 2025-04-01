# import random

# dice_roll = random.randint(1, 49)
# print(f"Ви кинули {dice_roll}")

# numbers0 = [1, 2, 3, 4, 5]
# chosen_numbers1 = random.choices(numbers0, k=3)
# print(chosen_numbers1)


# import random

# seq = (1, 1000)
# numbers1 = random.choice(seq)
# print(numbers1)
# numbers2 = random.uniform(1, 1000)
# print(numbers2)
# population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# numbers3 = random.sample(population, 6)
# print(numbers3)



# import random

# my_set2 = set(range(1, 1001))  
# numbers4 = random.sample(my_set2, 6)  
# print(numbers4)

# for i in range(5):
#     print(i)

# nums = [3, 1, 4, 1, 5, 9, 2]
# nums.sort()
# print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]



# import random

# my_set = range(1, 1001)
# chosen_numbers = random.sample(my_set, 6)
# print(chosen_numbers)



# import random

# def get_numbers_ticket(min, max, quantity):
#     my_list = list(range(min, max))
#     chosen_list = random.sample(my_list, quantity)
#     return sorted(chosen_list)

# print(get_numbers_ticket(1, 1001, 20))
                         



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

         




# import random

# def get_numbers_ticket(min, max, quantity):
#     # Проверяем, являются ли параметры целыми числами
#     if not (isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)):
#         return []
    
#     # Проверяем, что min < max и quantity положительное число
#     if min >= max or quantity <= 0 or quantity > (max - min):
#         return []

#     try:
#         my_list = list(range(min, max))
#         chosen_list = random.sample(my_list, quantity)
#         return sorted(chosen_list)
    
#     except ValueError:
#         return []

# # Тесты
# print(get_numbers_ticket(1, 1001, 20))  # Ожидаемый результат: список из 20 случайных чисел от 1 до 1000
# print(get_numbers_ticket(1, 49, 6))     # Ожидаемый результат: список из 6 случайных чисел от 1 до 48
# print(get_numbers_ticket("Hello", "in", "here"))  # Ожидаемый результат: []
# print(get_numbers_ticket(50, 1, 5))  # Ожидаемый результат: []
# print(get_numbers_ticket(1, 10, 15))  # Ожидаемый результат: []
# print(get_numbers_ticket(1, 10, -3))  # Ожидаемый результат: []






# import random

# def get_numbers_ticket(min, max, quantity):
#     # Перевірка, що всі параметри є цілими числами
#     if not all(isinstance(i, int) for i in (min, max, quantity)):
#         return []

#     # Перевірка коректності вхідних даних
#     if not (1 <= min < 1000):  # Мінімум має бути в межах [1, 999]
#         return []
#     if not (1 < max <= 1000):  # Максимум має бути в межах [2, 1000]
#         return []
#     if not (min < max):  # Мінімум має бути менше за максимум
#         return []
#     if not (min <= quantity <= max):  # Кількість чисел має бути між min і max
#         return []

#     # Генерація унікальних випадкових чисел
#     numbers = random.sample(range(min, max + 1), quantity)

#     # Повернення відсортованого списку
#     return sorted(numbers)

# # Тести
# print(get_numbers_ticket(1, 49, 6))       # Валідний випадок
# print(get_numbers_ticket(10, 20, 5))      # Валідний випадок
# print(get_numbers_ticket(1, 1001, 5))     # Некоректний випадок (max > 1000)
# print(get_numbers_ticket(100, 50, 5))     # Некоректний випадок (min > max)
# print(get_numbers_ticket(1, 49, 50))      # Некоректний випадок (quantity > max)
# print(get_numbers_ticket(1, 49, 0))       # Некоректний випадок (quantity < min)
# print(get_numbers_ticket("Hello", 100, 5))  # Некоректний випадок (рядок замість числа)
# print(get_numbers_ticket(1, "test", 5))     # Некоректний випадок (рядок у max)
# print(get_numbers_ticket(1, 100, "abc"))    # Некоректний випадок (рядок у quantity)







