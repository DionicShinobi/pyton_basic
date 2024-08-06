print("New version of the Calculator on Python")

while True:

    # Беремо основу прогруми відпрацьовану раніше та модифікуємо
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Select an operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error:Division by zero is impossible!")
            continue
    else:
        print("Error: Unknown operation!")
        continue

    print(f"Result: {result}")

    if input("Do you want to continue? (y/n): ").lower() != 'y':
        print("Goodbye!)")
        break
