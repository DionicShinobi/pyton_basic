while True:

    number = int(input("Enter a number: "))

    # Поки число більше 9, продовжуємо перемножувати його цифри
    while number > 9:
        result = 1
        for digit in str(number):
            result *= int(digit)
        number = result

    print(number)

    choice = input("Do you want to continue? (y/n): ").strip().lower()

    if choice != 'y':
        print("Completion of the program. Have a nice day!")
        break
