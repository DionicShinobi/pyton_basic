import random

# Створюємо список випадкових чисел із випадковою кількістю елементів від 3 до 10
list_length = random.randint(3, 10)
random_list = [random.randint(0, 10) for _ in range(list_length)]

print("Початковий список:", random_list)

# Створюємо новий список із першого, третього і другого з кінця елементів
new_list = [random_list[0], random_list[2], random_list[-2]]

print("Новий список:", new_list)
