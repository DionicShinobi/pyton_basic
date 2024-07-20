# запитуємо у користувача 5-ти значне число
number = int(input("Enter a 5-digit number: "))

# перша цифра
digit1 = number // 10000

# друга цифра
digit2 = (number // 1000) % 10

# третя цифра
digit3 = (number // 100) % 10

# четверта цифра
digit4 = (number // 10) % 10

# п'ята цифра
digit5 = number % 10

# формуємо нове число,що складається з цифр у зворотному порядку
flipped_number = (digit5 * 10000) + (digit4 * 1000) + (digit3 * 100) + (digit2 * 10) + digit1

# виводимо перевернуте число
print(flipped_number)
