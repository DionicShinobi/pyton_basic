import string
import keyword

while True:
    variable_name = input("Enter a variable name: ")

    # Перевірка на зареєстроване слово
    if variable_name in keyword.kwlist:
        print(False)

    # Перевірка на початок з цифри
    elif variable_name[0].isdigit():
        print(False)

    # Перевірка на великі літери
    elif any(char.isupper() for char in variable_name):
        print(False)

    # Перевірка на знаки пунктуації, крім "_"
    elif any(char in string.punctuation.replace("_", "") for char in variable_name):
        print(False)

    # Перевірка на те, що ім'я складається виключно з двох або більше підкреслень
    elif len(variable_name) > 1 and variable_name.strip('_') == "":
        print(False)

    else:
        print(True)

    continue_choice = input("Want to check another variable name? (y/n): ").strip().lower()

    if continue_choice != 'y':
        print("Completion of the program. Have a nice day!")
        break
