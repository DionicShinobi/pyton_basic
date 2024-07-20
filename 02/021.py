# запитуємо у користувача 4-х значне число
number = int(input("Enter a 4-digit number: "))

# перша цифра
digit1 = number // 1000

# друга цифра
digit2 = (number // 100) % 10

# третя цифра
digit3 = (number // 10) % 10

# Четверта цифра
digit4 = number % 10

# виводимо цифри у стовпець
print(digit1)
print(digit2)
print(digit3)
print(digit4)
