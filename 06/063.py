# Отримуємо введене число від користувача
number = int(input("Enter a number:"))

# Поки число більше 9, продовжуємо перемножувати його цифри
while number > 9:
    result = 1
    for digit in str(number):
        result *= int(digit)
    number = result

# Виводимо кінцевий результат
print(number)
