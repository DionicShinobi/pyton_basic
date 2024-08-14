def is_palindrome(text):
    # Залишаємо лише алфавітно-цифрові символи, перетворюємо в нижній регістр
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Перевірка паліндромності
    return cleaned_text == cleaned_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")
