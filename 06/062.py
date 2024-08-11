while True:

    seconds_input = int(input("Введіть кількість секунд (від 0 до 8639999): "))

    # Розрахунок днів, годин, хвилин і секунд
    days = seconds_input // 86400
    hours = (seconds_input % 86400) // 3600
    minutes = (seconds_input % 3600) // 60
    seconds = seconds_input % 60

    # Правильне відмінювання для слова "день"
    if days == 1:
        days_str = f"{days} день"
    elif 2 <= days <= 4 or (days % 10 >= 2 and days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20)):
        days_str = f"{days} дні"
    else:
        days_str = f"{days} днів"

    # Виведення результату з форматуванням
    print(f"{days_str}, {hours:02}:{minutes:02}:{seconds:02}")

    # Запит на продовження або вихід
    choice = input("Бажаєте ввести ще одне число? (y/n): ").strip().lower()

    if choice != 'y':
        print("Завершення програми. Гарного дня!")
        break
