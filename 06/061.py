import string

while True:
    # Отримуємо введений рядок від користувача
    input_str = input("Enter two letters separated by a hyphen: ")

    all_letters = string.ascii_letters  # Всі літери

    # Розділяємо строку на дві літери
    start, end = input_str.split('-')

    # Отримуємо індекси початкової та кінцевої літери
    start_index = all_letters.index(start)
    end_index = all_letters.index(end)

    # Повертаємо всі символи між ними включно
    result = all_letters[start_index:end_index + 1]

    # Виводимо результат
    print(result)

    # Запитуємо у користувача, чи хоче він продовжити
    choice = input("Do you want to continue? (y/n): ")

    if choice.lower() != 'y':
        print("Completion of the program.")
        break
