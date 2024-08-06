import string
import keyword

variable_name = input("Введіть ім'я змінної: ")

# Перевірка 1, чи не є ім'я зареєстрованим словом
if variable_name in keyword.kwlist:
    print(False)

else:
    # Перевірка 2, чи починається ім'я з цифри
    if variable_name[0].isdigit():
        print(False)

    else:
        # Перевірка 3, на наявність заборонених символів та великих літер
        allowed_chars = string.ascii_lowercase + string.digits + "_"
        if any(char not in allowed_chars for char in variable_name):
            print(False)
            
        else:
            # Перевірка 4 на кількість нижніх підкреслень
            if variable_name.count('_') > 1:
                print(False)
            else:
                print(True)
